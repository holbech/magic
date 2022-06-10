#!/usr/bin/env python2
# coding=utf-8

import sys 
import json
from itertools import chain,groupby
from operator import itemgetter
import re
import codecs
import cPickle as pickle
from magic import standardize,CardData

import argparse

parser = argparse.ArgumentParser(description='Reads mtgjson-files and create a .db file for other tools to read')
parser.add_argument('-o', '--output', default='cards.db', help='File to write database to')
parser.add_argument('-c', '--cards', default='AllPrintings.json', help='Append new column rather than replace existing one')
parser.add_argument('-p', '--prices', default='AllPrices.json', help='Append new column rather than replace existing one')

args = parser.parse_args()


sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

def mean(l):
    length = len(l)
    if length:
        return sum(l)/float(length)
    else:
        return None
    

def process_card(ed,card,price):
    try:
        is_special = (ed in ('PLIST',) or 
                      any( card.get(x,False) for x in ('isTimeshifted','isPromo','isOversized','isOnlineOnly','isStarter') ) or 
                      not card.get('hasNonFoil',False))
        data = CardData(card['convertedManaCost'],
                        card['name'],
                        card.get('manaCost'),
                        '' if is_special else card['rarity'],
                        card['types'],
                        [ s for s in card.get('subtypes') or () if s in ('Aura', 'Vehicle', 'Equipment') ],
                        card['identifiers'].get('multiverseId'),
                        '' if is_special else ed,
                        [] if card['types'] == ['Land'] else card['colorIdentity'],
                        price,
                        card.get('side'))
        name = standardize(card['name'])
        ids = [card['identifiers'].get('multiverseId'),name] + ([ n.strip() for n in name.split('//') ] if '//' in name else [])
        return ( (x,data) for x in ids if x and x != '534948' )
    except Exception, e:
        raise ValueError('Cannot parse card: ' +  str(card) + ":\n" + (e.message or str(e)))

def debug(conditions):
    with open(args.cards) as infile:
        database = ( json.dumps([card,[ (i,c.as_dict()) for (i,c) in process_card(ed,card) ]])
                     for ed,set in json.load(infile)['data'].iteritems() 
                     for card in set['cards']
                     if set['type'] != 'funny' )
        matches = ( k for k in database if any( c in k for c in conditions ) )
        for l in matches:
            print l
    exit(0)
    
def get_price(price_obj):
    try:
        return mean(price_obj['paper']['cardmarket']['retail']['normal'].values())
    except KeyError:
        return None

with open(args.prices) as infile:
    prices = ( (uuid,get_price(prices)) for uuid,prices in json.load(infile)['data'].iteritems() )
    prices = { uuid: price for uuid,price in prices if price is not None }

with open(args.cards) as infile:
    content = json.load(infile)['data']
    editions = { ed: set['name'] for ed,set in content.iteritems() 
                 if set['type'] != 'funny' and ed not in ('TBTH',) }
    database = list(chain.from_iterable( process_card(ed,card,prices.get(card['uuid']))
                                         for ed,set in content.iteritems() 
                                         for card in set['cards']
                                         if set['type'] != 'funny' and ed not in ('TBTH',) ) )
    database.sort()
    database = { key: reduce(lambda x,y: x + y, ( c for (_,c) in cards )) for key,cards in groupby(database,itemgetter(0)) }   

def debug_keys():
    for key in sorted( k for k in database.keys() if isinstance(k,basestring) ):
        print key
        
with open(args.output, 'wb') as outfile:
    pickle.dump((editions,database), outfile)

