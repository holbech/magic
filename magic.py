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
    if thing is None:
        return u''
    if isinstance(thing,tuple):
        return u' // '.join( set2str(x) for x in thing if x is not None )
    if isinstance(thing,(set,list)):
        return u','.join(sorted( t for t in thing if t)) 
    return unicode(thing)
    
def byside(side,val):
    if side is None:
        return val
    elif side == 'a':
        return (val,None)
    elif side == 'b':
        return (None,val)
    else:
        raise ValueError('Odd side: ' + side)


def addsides(sides1,sides2):
    if isinstance(sides1,tuple) and isinstance(sides2,tuple):
        return tuple( addsides(a,b) for a,b in zip(sides1,sides2) )
    elif sides1 is None:
        return sides2
    elif sides2 is None:
        return sides1
    elif sides1 == sides2:
        return sides1
    elif isinstance(sides1,tuple) and sides2 in sides1:
        return sides1
    elif isinstance(sides2,tuple) and sides1 in sides2:
        return sides2
    else:
        raise ValueError('Cannot combine %s and %s' % (sides1,sides2))
        
    
class CardData(object):
    __slots__ = ('name','rarity','colours','types','subtypes','cmc','mc','price','editions','mvids')
    def __init__(self, cmc, name, mc, rarity, types, subtypes, mvids, editions,colours,price,side=None):
        self.cmc = byside(side,cmc)
        self.name = name
        self.mc = byside(side,mc)
        self.rarity = rarity if isinstance(rarity, set) else {rarity or ''}
        self.types = types if isinstance(types, set) else set(types)
        self.subtypes = subtypes if isinstance(subtypes, set) else set(subtypes)
        self.mvids = mvids if isinstance(mvids, set) else { mvids or '' }
        self.editions = editions if isinstance(editions, set) else { editions or '' }
        self.colours = byside(side,colours)
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
                    return CardData(addsides(self.cmc, other.cmc), 
                                    self.name, 
                                    addsides(self.mc,other.mc),
                                    self.rarity | other.rarity, 
                                    self.types | other.types,
                                    self.subtypes | other.subtypes,
                                    self.mvids | other.mvids,
                                    self.editions | other.editions,
                                    addsides(self.colours,other.colours),
                                    min(self.price,other.price)
                                    )
                except ValueError,ve:
                    sys.stderr.write(self.name + ': ' + ve.message + '\n')
                    return self
            else:
                sys.stderr.write('Name differs: ' + str(self) + " " + str(other) + '\n')
                return self
        else:
            try:
                return CardData(addsides(self.cmc, other.cmc), 
                                self.name, 
                                addsides(self.mc, other.mc), 
                                self.rarity | other.rarity, 
                                self.types | other.types,
                                self.subtypes | other.subtypes,
                                self.mvids | other.mvids,
                                self.editions | other.editions,
                                addsides(self.colours,other.colours),
                                min(self.price,other.price)
                                )
            except ValueError,ve:
	        sys.stderr.write(self.name + ': ' + ve.message + '\n')
                return self
                
    def as_dict(self):
        return { k:set2str(getattr(self,k)) for k in CardData.__slots__ }
    def values(self):
        return tuple( self._colours2str() if k == 'colours' else set2str(getattr(self,k)) 
                      for k in CardData.__slots__ )
    def _colours2str(self):
        if self.colours is None: 
            sys.stderr.write(str(self))
        if len(self.colours) > 1:
            return 'MULTI'
        if not self.colours and 'Land' in self.types:
            return 'LAND'
        return set2str(self.colours)
    def __str__(self):
        return str(self.as_dict())

