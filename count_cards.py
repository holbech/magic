#!/usr/bin/env python2

import sys 



total = 0
with open(sys.argv[1]) as infile:
    for line in infile.readlines():
        if line.strip():
            if not line.startswith('//'):
                try:
                    total += int(line.split()[0])
                except Exception as e:
                    sys.stderr.write("Error processing " + sys.argv[1] + " - '" + line + "': " + e.message)
                    raise e
print sys.argv[1], total
