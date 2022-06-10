# coding=utf-8
import sys

def mean(l):
    length = len(l)
    if length:
        return sum(l)/float(length)
    else:
        return None
    
def standardize(name):
    return name.replace(u'æ','ae').replace(u'á','a').lower().partition('//')[0].strip()

def one_or_equal(a,b,attribute):
    va = getattr(a,attribute)
    vb = getattr(b,attribute)
    v = va or vb
    if va == vb or (not va) or (not vb):
        return v
    else:
        raise ValueError('%s differs: %s %s\n' % (attribute, str(a), str(b)))

def superset_or_equal(a,b,attribute):
    va = getattr(a,attribute)
    vb = getattr(b,attribute)
    if not (va and vb) or va == vb:
        return va or vb
    if isintance(va,(set,list)) and all( x in va for x in vb ):
        return vb
    else:
        raise ValueError('%s differs: %s %s\n' % (attribute, str(a), str(b)))

def set2str(thing):
    return u','.join(sorted( t for t in thing if t)) if isinstance(thing,set) else thing
    
class CardData(object):
    __slots__ = ('name','rarity','colours','types','subtypes','cmc','mc','price','editions','mvids')
    def __init__(self, cmc, name, mc, rarity, types, subtypes, mvids, editions,colours,price):
        self.cmc = cmc
        self.name = name
        self.mc = mc if isinstance(mc, set) else { x for x in (mc or '').split(',') if x }
        self.rarity = rarity if isinstance(rarity, set) else {rarity or ''}
        self.types = types if isinstance(types, set) else set(types)
        self.subtypes = subtypes if isinstance(subtypes, set) else set(subtypes)
        self.mvids = mvids if isinstance(mvids, set) else { mvids or '' }
        self.editions = editions if isinstance(editions, set) else { editions or '' }
        self.colours = colours if isinstance(colours, set) else { c for c in (colours or ()) if mc and c in mc }
        self.price = price or 100000.0

    def __getstate__(self):
        return [ getattr(self,k) for k in CardData.__slots__ ]
    def __setstate__(self, d):
        for x,k in zip(d,CardData.__slots__):
            setattr(self,k,x)
    def __add__(self, other):
        if other.name != self.name and other.name and self.name:
            if self.name in other.name:
                return other + self
            elif other.name in self.name:
                try:
                    return CardData(max(self.cmc or 0, other.cmc or 0), 
                                    self.name, 
                                    self.mc | other.mc,
                                    self.rarity | other.rarity, 
                                    self.types | other.types,
                                    self.subtypes | other.subtypes,
                                    self.mvids | other.mvids,
                                    self.editions | other.editions,
                                    self.colours | other.colours,
                                    min(self.price,other.price)
                                    )
                except ValueError,ve:
                    sys.stderr.write(ve.message + '\n')
                    return self
            else:
                sys.stderr.write('Name differs: ' + str(self) + " " + str(other) + '\n')
                return self
        else:
            try:
                return CardData(one_or_equal(self, other, 'cmc'), 
                                self.name, 
                                (self.mc or other.mc) if '//' in self.name else one_or_equal(self, other, 'mc'), 
                                self.rarity | other.rarity, 
                                self.types | other.types,
                                self.subtypes | other.subtypes,
                                self.mvids | other.mvids,
                                self.editions | other.editions,
                                self.colours | other.colours,
                                min(self.price,other.price)
                                )
            except ValueError,ve:
                sys.stderr.write(ve.message + '\n')
                return self
                
    def as_dict(self):
        return { k:set2str(getattr(self,k)) for k in CardData.__slots__ }
    def values(self):
        return tuple( self._colours2str() if k == 'colours' else set2str(getattr(self,k)) 
                      for k in CardData.__slots__ )
    def _colours2str(self):
        if len(self.colours) > 1:
            return 'MULTI'
        if not self.colours and 'Land' in self.types:
            return 'LAND'
        return set2str(self.colours)
    def __str__(self):
        return str(self.as_dict())

