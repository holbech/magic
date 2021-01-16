#!/usr/bin/env python2

import sys 

current = None
with open(sys.argv[1]) as infile:
    for (index,line) in enumerate(infile.readlines()):
        if line.strip():
            try:
                if line.startswith('///') and index % 2 == 0:
                    id, qt, name = line.lstrip('/').split('loc:')[0].strip().split(' ',2)
                    current = (qt.partition(':')[2].strip(),
                               id.partition(':')[2].strip(),
                               name.partition(':')[2].strip())
                elif index % 2 == 1:
                    qt, _, name = line.strip().partition(' ')
                    assert (qt == current[0] and name == current[2])
                    print '\t'.join(current)
            except Exception as e:
                sys.stderr.write("Error processing " + sys.argv[1] + " - '" + str(index) + " " + line + "': " + e.message)
                raise e
