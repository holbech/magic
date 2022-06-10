from collections import namedtuple

MtgSet = namedtuple('MtgSet',('name','code','date'))

set_codes = [ MtgSet(*l.split('\t')) for l in """
Arabian Nights	ARN	1993-12-17
Antiquities	ATQ	1994-03-04
Legends	LEG	1994-06-01
The Dark	DRK	1994-08-01
Fallen Empires	FEM	1994-11-01
Fourth Edition	4ED	1995-04-01
Ice Age	ICE	1995-06-03
Chronicles	CHR	1995-07-01
Renaissance	REN	1995-08-01
Rinascimento	RIN	1995-08-01
Homelands	HML	1995-10-01
Alliances	ALL	1996-06-10
Mirage	MIR	1996-10-08
Multiverse Gift Box	VIS	1996-11-01
Introductory Two-Player Set	X2PS	1996-12-31
Visions	VIS	1997-02-03
Fifth Edition	5ED	1997-03-24
Portal	POR	1997-05-01
Weatherlight	WTH	1997-06-09
Tempest	TMP	1997-10-14
Stronghold	STH	1998-03-02
Exodus	EXO	1998-06-15
Portal Second Age	P02	1998-06-24
Unglued	UGL	1998-08-11
Urza's Saga	USG	1998-10-12
Anthologies	ATH	1998-11-01
Urza's Legacy	ULG	1999-02-15
Urza's Destiny	UDS	1999-06-07
Starter 1999	S99	1999-07-01
Portal Three Kingdoms	PTK	1999-07-06
Mercadian Masques	MMQ	1999-10-04
Nemesis	NEM	2000-02-14
Starter 2000	S00	2000-04-01
Prophecy	PCY	2000-06-05
Invasion	INV	2000-10-02
Planeshift	PLS	2001-02-05
Seventh Edition	7ED	2001-04-11
Apocalypse	APC	2001-06-04
Odyssey	ODY	2001-10-01
Deckmasters	DKM	2001-12-01
Torment	TOR	2002-02-04
Judgment	JUD	2002-05-27
Onslaught	ONS	2002-10-07
Legions	LGN	2003-02-03
Scourge	SCG	2003-05-26
Eighth Edition	8ED	2003-07-28
Mirrodin	MRD	2003-10-02
Darksteel	DST	2004-02-06
Fifth Dawn	5DN	2004-06-04
Champions of Kamigawa	CHK	2004-10-01
Unhinged	UNH	2004-11-19
Betrayers of Kamigawa	BOK	2005-02-04
Saviors of Kamigawa	SOK	2005-06-03
Ninth Edition	9ED	2005-07-29
Ravnica: City of Guilds	RAV	2005-10-07
Guildpact	GPT	2006-02-03
Dissension	DIS	2006-05-05
Coldsnap	CSP	2006-07-21
Coldsnap Theme Decks	CSP	2006-07-21
Time Spiral	TSP	2006-10-06
Resale Promos	PMEI	2007-01-01
Planar Chaos	PLC	2007-02-02
Pro Tour Promos	PMEI	2007-02-09
Grand Prix Promos	PMEI	2007-02-24
Future Sight	FUT	2007-05-04
Tenth Edition	10E	2007-07-13
Lorwyn	LRW	2007-10-12
Duel Decks: Elves vs. Goblins	DD1	2007-11-16
Morningtide	MOR	2008-02-01
Shadowmoor	SHM	2008-05-02
Eventide	EVE	2008-07-25
From the Vault: Dragons	DRB	2008-08-29
Shards of Alara	ALA	2008-10-03
Duel Decks: Jace vs. Chandra	DD2	2008-11-07
Conflux	CON	2009-02-06
Duel Decks: Divine vs. Demonic	DDC	2009-04-10
Alara Reborn	ARB	2009-04-30
Magic 2010	M10	2009-07-17
From the Vault: Exiled	V09	2009-08-28
Planechase	HOP	2009-09-04
Zendikar	ZEN	2009-10-02
Duel Decks: Garruk vs. Liliana	DDD	2009-10-30
Premium Deck Series: Slivers	H09	2009-11-20
Worldwake	WWK	2010-02-05
Duel Decks: Phyrexia vs. the Coalition	DDE	2010-03-19
Rise of the Eldrazi	ROE	2010-04-23
Archenemy	ARC	2010-06-18
Magic 2011	M11	2010-07-16
From the Vault: Relics	V10	2010-08-27
Duel Decks: Elspeth vs. Tezzeret	DDF	2010-09-03
Scars of Mirrodin	SOM	2010-10-01
Mirrodin Besieged	MBS	2011-02-04
Duel Decks: Knights vs. Dragons	DDG	2011-04-01
New Phyrexia	NPH	2011-05-13
Magic 2012	M12	2011-07-15
From the Vault: Legends	V11	2011-08-26
Duel Decks: Ajani vs. Nicol Bolas	DDH	2011-09-02
Innistrad	ISD	2011-09-30
Premium Deck Series: Graveborn	PD3	2011-11-18
Dark Ascension	DKA	2012-02-03
Duel Decks: Venser vs. Koth	DDI	2012-03-30
Avacyn Restored	AVR	2012-05-04
Planechase 2012	PC2	2012-06-01
Magic 2013	M13	2012-07-13
From the Vault: Realms	V12	2012-08-31
Duel Decks: Izzet vs. Golgari	DDJ	2012-09-07
Return to Ravnica	RTR	2012-10-05
Commander's Arsenal	CM1	2012-11-02
Gatecrash	GTC	2013-02-01
Duel Decks: Sorin vs. Tibalt	DDK	2013-03-15
Dragon's Maze	DGM	2013-05-03
Modern Masters	MMA	2013-06-07
Magic 2014	M14	2013-07-19
From the Vault: Twenty	V13	2013-08-23
Duel Decks: Heroes vs. Monsters	DDL	2013-09-06
Theros	THS	2013-09-27
Commander 2013	C13	2013-11-01
Born of the Gods	BNG	2014-02-07
Duel Decks: Jace vs. Vraska	DDM	2014-03-14
Journey into Nyx	JOU	2014-05-02
Modern Event Deck 2014	MD1	2014-05-30
Conspiracy	CNS	2014-06-06
Magic 2015	M15	2014-07-18
From the Vault: Annihilation	V14	2014-08-22
Duel Decks: Speed vs. Cunning	DDN	2014-09-05
Khans of Tarkir	KTK	2014-09-26
Commander 2014	C14	2014-11-07
Fate Reforged	FRF	2015-01-23
Duel Decks: Elspeth vs. Kiora	DDO	2015-02-27
Dragons of Tarkir	DTK	2015-03-27
Modern Masters 2015	MM2	2015-05-22
Magic Origins	ORI	2015-07-17
From the Vault: Angels	V15	2015-08-21
Duel Decks: Zendikar vs. Eldrazi	DDP	2015-08-28
Battle for Zendikar	BFZ	2015-10-02
Zendikar Expeditions	EXP	2015-10-02
Commander 2015	C15	2015-11-13
Oath of the Gatewatch	OGW	2016-01-22
Duel Decks: Blessed vs. Cursed	DDQ	2016-02-26
Shadows over Innistrad	SOI	2016-04-08
Welcome Deck 2016	W16	2016-04-08
Eternal Masters	EMA	2016-06-10
Eldritch Moon	EMN	2016-07-22
From the Vault: Lore	V16	2016-08-19
Conspiracy: Take the Crown	CN2	2016-08-26
Duel Decks: Nissa vs. Ob Nixilis	DDR	2016-09-02
Kaladesh	KLD	2016-09-30
Kaladesh Inventions	MPS	2016-09-30
Commander 2016	C16	2016-11-11
Planechase Anthology	PCA	2016-11-25
Aether Revolt	AER	2017-01-20
Modern Masters 2017	MM3	2017-03-17
Duel Decks: Mind vs. Might	DDS	2017-03-31
Welcome Deck 2017	W17	2017-04-15
Amonkhet	AKH	2017-04-28
Amonkhet Invocations	MP2	2017-04-28
Commander Anthology	CMA	2017-06-09
Archenemy: Nicol Bolas	E01	2017-06-16
Hour of Devastation	HOU	2017-07-14
Commander 2017	C17	2017-08-25
Ixalan	XLN	2017-09-29
Duel Decks: Merfolk vs. Goblins	DDT	2017-10-24
Iconic Masters	IMA	2017-11-17
Explorers of Ixalan	E02	2017-11-24
From the Vault: Transform	V17	2017-11-24
Unstable	UST	2017-12-08
Rivals of Ixalan	RIX	2018-01-19
Masters 25	A25	2018-03-16
Duel Decks: Elves vs. Inventors	DDU	2018-04-06
Dominaria	DOM	2018-04-27
Battlebond	BBD	2018-06-08
Signature Spellbook: Jace	SS1	2018-06-15
Global Series Jiang Yanggu & Mu Yanling	GS1	2018-06-22
Core Set 2019	M19	2018-07-13
Commander 2018	C18	2018-08-09
Guilds of Ravnica	GRN	2018-10-05
Ultimate Masters	UMA	2018-12-07
Ravnica Allegiance	RNA	2019-01-25
War of the Spark	WAR	2019-05-03
Modern Horizons	MH1	2019-06-14
Signature Spellbook: Gideon	SS2	2019-06-28
Core Set 2020	M20	2019-07-12
Commander 2019	C19	2019-08-23
Throne of Eldraine	ELD	2019-10-04
Ponies: The Galloping	PTG	2019-10-22
Mystery Booster	MB1	2019-11-07
Game Night 2019	GN2	2019-11-15
Theros Beyond Death	THB	2020-01-24
Unsanctioned	UND	2020-02-29
Ikoria: Lair of Behemoths	IKO	2020-04-24
Secret Lair: Ultimate Edition	PMEI	2020-05-29
Signature Spellbook: Chandra	SS3	2020-06-26
Core Set 2021	M21	2020-07-03
Jumpstart	JMP	2020-07-17
Double Masters	2XM	2020-08-07
Zendikar Rising Expeditions	ZNE	2020-09-25
Zendikar Rising	ZNR	2020-09-25
The List	MB1	2020-09-26
Commander Legends	CMR	2020-11-20
Commander Collection: Green	CC1	2020-12-04
Kaldheim	KHM	2021-02-05
Time Spiral Remastered	TSR	2021-03-19
Strixhaven: School of Mages	STX	2021-04-23
Modern Horizons 2	MH2	2021-06-18
Adventures in the Forgotten Realms	AFR	2021-07-23
Innistrad: Midnight Hunt	MID	2021-09-24
Innistrad: Crimson Vow	VOW	2021-11-19
Commander Collection: Black	CC2	2022-01-28
Innistrad: Double Feature	PMEI	2022-01-28
Kamigawa: Neon Dynasty	NEO	2022-02-18
Unfinity	UNF	2022-04-01
""".splitlines()
              if l.strip() ]
