#!/usr/bin/env python2

import sys 

fields = [ int(i) for i in sys.argv[1:] ]
totals = [ 0 for _ in fields ]
others = []


def to_string(tot):
    pre,_,post = str(tot).partition('.')
    if post.rstrip('0'):
        return str(tot)
    else:
        return pre
        
def print_tots():
    if any( t > 0 for t in totals):
        res = []
        totals_pointer = 0
        others_pointer = 0
        for i in range(len(totals)+len(others)):
            if i in fields:
                res.append(to_string(totals[totals_pointer]))
                totals_pointer += 1
            else:
                res.append(others[others_pointer])
                others_pointer += 1
        print '\t'.join(res)
        
    
for line in sys.stdin.readlines():
    org_line = line
    try:
        line = line.rstrip('\n').split('\t')
        line_totals = [ int(line[f]) if line[f].isdigit() else float(line[f]) for f in fields ]
        line_others = [ f for (i,f) in enumerate(line) if i not in fields ]
        if line_others != others:
            print_tots()
            others = line_others
            totals = line_totals
        else:
            totals = [ a+b for (a,b) in zip(totals,line_totals) ]
    except BaseException, ex:
        raise Exception("Error in line:\n"+ org_line + "\n\n" + ex.message)
print_tots()

