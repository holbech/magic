#!/usr/bin/env python2
# coding=utf-8

import sys 
import codecs
import cPickle as pickle
from magic import CardData,standardize
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser(description='Reads a file of cards needed and calculates expected value of a display. Each line in the file needs to be either a triple of ' +
                                             '(quantity,mvid,name) or a pair of (quanty,name) separated by tabs. Result is written to stdout')
parser.add_argument('-i', '--input', default='<stdin>', help='File to read')
parser.add_argument('-d', '--database', default='cards.db', help='Database to get properties from')
parser.add_argument('-c', '--commons', action='store_true', help='Only calculate for commons')
parser.add_argument('-u', '--uncommons', action='store_true', help='Only calculate for commons and uncommons')

args = parser.parse_args()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

with open(args.database, 'rb') as infile:
    (editions,database) = pickle.load(infile)

values = defaultdict(float)

def process(line):
    if line.strip():
        qt, id, name = (None,None,None)
        parts = line.strip().split('\t')
        if len(parts) == 3:
            qt, id, name = parts
        elif len(parts) == 2:
            qt, name = parts
            id = -1
        else:
            raise ValueError("Error parsing line: " + line)
        matches = ( database.get(x) for x in (standardize(name),id) )
        try:
            card_info = next( c for c in matches if c )
        except StopIteration:
            debug_keys()
            raise ValueError("No match for %s: (%d)" % (standardize(name),id))
        if 'common' in card_info.rarity:
            multiplier = min(int(qt),4)
        elif 'uncommon' in card_info.rarity and not args.commons:
            multiplier = min(int(qt),2)
        elif not (args.commons or args.uncommons):
            multiplier = 1
        else:
            multiplier = 0
        if multiplier:
            for ed in card_info.editions:
                values[ed] += multiplier*card_info.price
        
if args.input == '<stdin>':
    for line in sys.stdin.readlines():
        process(line)
else:
    with open(args.input) as infile:
        for line in infile.readlines():
            process(line)
        
for ed,value in sorted(values.iteritems(), key=lambda x: -x[1]):
    if ed:
        print '%s: %f' % (editions[ed],value)
    
