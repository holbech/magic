import json
import sys
from math import sqrt
from set_codes import set_codes
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

def mean(l):
  length = len(l)
  if length:
    return sum(l)/float(length)
  else:
    return None

def stddev(l):
  length = len(l)
  if length:
    m = mean(l)
    l = tuple( (v-m)*(v-m) for v in l )
    return sqrt(sum(l)/float(length))
  else:
    return None

unique_strings = {}
def unique(s):
  try:
    return unique_strings[s]
  except KeyError:
    unique_strings[s] = s
    return s


class Card(object):
  __slots__ = ('edition', 'name', 'rarity', 'cardmarket_url', 'price')

  def __init__(self, edition, card, price):
    self.edition = edition
    self.name = unique(card['name'])
    self.cardmarket_url = unique(card.get('purchaseUrls',{}).get('cardmarket',''))
    self.price = price if price else None
    self.rarity = unique(card['rarity'])

  def sort_price(self):
    return 0.0 if self.price is None else self.price.sort_price()

  def __str__(self):
    return u'%s (%s): %s - %s' % (self.name, self.edition, self.price, self.cardmarket_url)

class AggValue(object):
  __slots__ = ('min','avg','max','stddev','latest','trend')
  def __init__(self, price_list):
    self.min = min(price_list)
    self.max = max(price_list)
    self.avg = mean(price_list)
    self.stddev = stddev(price_list)
    self.latest = price_list[-1]
    m = len(price_list)/2
    a = mean(price_list[0:m])
    b = mean(price_list[m:])
    self.trend = (b-a)/a if a > 0.0 else 1.0

  def sort_price(self):
    return self.avg

  def __str__(self):
    return '%f / %f / %f / %f / %f / %f' % (self.min,self.avg,self.max,self.stddev,self.latest, self.trend)

class Price(object):
  __slots__ = ('foil','normal')
  def __init__(self, prices):
    self.foil = tuple( price for (_,price) in sorted(prices.get('foil',{}).iteritems()) )
    self.normal = tuple( price for (_,price) in sorted(prices.get('normal',{}).iteritems()) )

  def foil_price(self):
    return AggValue(self.foil) if self.foil else None

  def normal_price(self):
    return AggValue(self.normal) if self.normal else None

  def sort_price(self):
    return self.foil_price().sort_price() if not self.normal else self.normal_price().sort_price()

  def __str__(self):
    return '(F: %s, N: %s)' % (self.foil_price(), self.normal_price())

  def __nonzero__(self):
    return bool(self.normal or self.foil)

with open('./AllPrices.json') as infile:
  all_prices = { uuid: Price(content.get('retail',{}))
                 for (uuid,price) in json.load(infile)['data'].iteritems()
                 for (db,content) in price.get('paper',{}).iteritems()
                 if db == 'cardmarket' }

with open('./AllPrintings.json') as infile:
  all_cards = { edition: [ Card(edition,card,all_prices.get(card['uuid'],None)) for card in cards['cards'] ]
                for (edition,cards) in json.load(infile)['data'].iteritems() }

def print_cards(cards, filter_func, min_price, min_count=10):
  cards = sorted([ c for c in cards if filter_func(c)], key=lambda c: -c.sort_price())
  for i,card in enumerate(cards):
    if card.sort_price() < min_price and i > min_count:
      break
    output = unicode(card).encode('ascii', 'ignore')
    output = '%0.2f   ' % (card.sort_price(),) + output
    print output

def print_edition(edition):
  print '\n\n\n\n' + edition.name + '\n\nRares:'
  print_cards(all_cards[edition.code], lambda c: c.rarity in ('mythic','rare'), 10.0)
  print '\nUncommon:'
  print_cards(all_cards[edition.code], lambda c: c.rarity == 'uncommon', 3.0)
  print '\nCommon:'
  print_cards(all_cards[edition.code], lambda c: c.rarity == 'common', 1.0)


for ed in set_codes:
  if (ed.date > '2000-10-01' and ed.date < '2006-07-22') or ed.date > '2018-10-04':
    print_edition(ed)

