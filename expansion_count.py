#!/usr/bin/env python2

import sys 
from collections import defaultdict
from itertools import chain

expansions = dict( ( x.strip() for x in l.split(' ',1) ) for l in
'''
10E    Tenth Edition
2ED    Unlimited Edition
2XM    Double Masters
3ED    Revised Edition
4BB    Fourth Edition Foreign Black Border
4ED    Fourth Edition
5DN    Fifth Dawn
5ED    Fifth Edition
6ED    Classic Sixth Edition
7ED    Seventh Edition
8ED    Eighth Edition
9ED    Ninth Edition
A25    Masters 25
AER    Aether Revolt
AKH    Amonkhet
AKR    Amonkhet Remastered
ALA    Shards of Alara
ALL    Alliances
APC    Apocalypse
ARB    Alara Reborn
ARN    Arabian Nights
ATQ    Antiquities
AVR    Avacyn Restored
BBD    Battlebond
BFZ    Battle for Zendikar
BNG    Born of the Gods
BOK    Betrayers of Kamigawa
CHK    Champions of Kamigawa
CHR    Chronicles
CMR    Commander Legends
CN2    Conspiracy: Take the Crown
CNS    Conspiracy
CON    Conflux
CSP    Coldsnap
DGM    Dragon's Maze
DIS    Dissension
DKA    Dark Ascension
DOM    Dominaria
DRK    The Dark
DST    Darksteel
DTK    Dragons of Tarkir
ELD    Throne of Eldraine
EMA    Eternal Masters
EMN    Eldritch Moon
EVE    Eventide
EXO    Exodus
FBB    Foreign Black Border
FEM    Fallen Empires
FMB1    Mystery Booster Retail Edition Foils
FRF    Fate Reforged
FUT    Future Sight
GPT    Guildpact
GRN    Guilds of Ravnica
GTC    Gatecrash
HML    Homelands
HOU    Hour of Devastation
ICE    Ice Age
IKO    Ikoria: Lair of Behemoths
IMA    Iconic Masters
INV    Invasion
ISD    Innistrad
JMP    Jumpstart
JOU    Journey into Nyx
JUD    Judgment
KHM    Kaldheim
KLD    Kaladesh
KLR    Kaladesh Remastered
KTK    Khans of Tarkir
LEA    Limited Edition Alpha
LEB    Limited Edition Beta
LEG    Legends
LGN    Legions
LRW    Lorwyn
M10    Magic 2010
M11    Magic 2011
M12    Magic 2012
M13    Magic 2013
M14    Magic 2014
M15    Magic 2015
M19    Core Set 2019
M20    Core Set 2020
M21    Core Set 2021
MB1    Mystery Booster
MBS    Mirrodin Besieged
ME1    Masters Edition
ME2    Masters Edition II
ME3    Masters Edition III
ME4    Masters Edition IV
MH1    Modern Horizons
MIR    Mirage
MM2    Modern Masters 2015
MM3    Modern Masters 2017
MMA    Modern Masters
MMQ    Mercadian Masques
MOR    Morningtide
MRD    Mirrodin
NEM    Nemesis
NPH    New Phyrexia
ODY    Odyssey
OGW    Oath of the Gatewatch
ONS    Onslaught
ORI    Magic Origins
PCY    Prophecy
PLC    Planar Chaos
PLIST    The List
PLS    Planeshift
RAV    Ravnica: City of Guilds
REN    Renaissance
RIN    Rinascimento
RIX    Rivals of Ixalan
RNA    Ravnica Allegiance
ROE    Rise of the Eldrazi
RTR    Return to Ravnica
SCG    Scourge
SHM    Shadowmoor
SOI    Shadows over Innistrad
SOK    Saviors of Kamigawa
SOM    Scars of Mirrodin
STH    Stronghold
SUM    Summer Magic / Edgar
THB    Theros Beyond Death
THS    Theros
TMP    Tempest
TOR    Torment
TPR    Tempest Remastered
TSB    Time Spiral Timeshifted
TSP    Time Spiral
TSR    Time Spiral Remastered
UDS    Urza's Destiny
ULG    Urza's Legacy
UMA    Ultimate Masters
USG    Urza's Saga
VIS    Visions
VMA    Vintage Masters
WAR    War of the Spark
WTH    Weatherlight
WWK    Worldwake
XLN    Ixalan
ZEN    Zendikar
ZNR    Zendikar Rising
'''.strip().splitlines() )

totals = defaultdict(lambda : defaultdict(int))

for line in sys.stdin.readlines():
    if line.strip():
        qt,_,rarity,_,_,_,_,exp,_ = line.rstrip('\n').split('\t')
        for e in exp.split(','):
            totals[e][rarity] += int(qt)

rarity_codes = sorted(set(chain.from_iterable( vs.keys() for vs in totals.itervalues() )))

print '\t'.join(['expansion'] + rarity_codes)

for exp,ts in totals.iteritems():
    counts = [ str(ts[r]) for r in rarity_codes ]
    print '\t'.join([expansions.get(exp,exp)] + counts)



