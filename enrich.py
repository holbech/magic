#!/usr/bin/env python2
# coding=utf-8

import sys 
import json
from itertools import chain,groupby
from operator import itemgetter
import re
import codecs
import cPickle as pickle
from magic import CardData,standardize
import argparse

parser = argparse.ArgumentParser(description='Enriches a file of cards with properties. Each line in the file needs to be either a triple of ' +
                                             '(quantity,mvid,name) or a pair of (quanty,name) separated by tabs. Result is written to stdout')
parser.add_argument('-i', '--input', default='<stdin>', help='File to read')
parser.add_argument('-d', '--database', default='cards.db', help='Database to get properties from')

args = parser.parse_args()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

with open(args.database, 'rb') as infile:
    (_,database) = pickle.load(infile)

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
            for k in sorted(database.keys()):
                print k
            raise ValueError("No match for %s (%s)" % (standardize(name),id))
        try:
            print u'\t'.join( (s if isinstance(s,basestring) else str(s)).strip() for s in ((qt,) + card_info.values()) )
        except Exception:
            print u"Error in " + line
            print u'CI:' + json.dumps(card_info.as_dict())
            raise
        
if args.input == '<stdin>':
    for line in sys.stdin.readlines():
        process(line)
else:
    with open(args.input) as infile:
        for line in infile.readlines():
            process(line)
        
