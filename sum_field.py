#!/usr/bin/env python2

import sys 

total = 0
field = int(sys.argv[1])
head = []
tail = []
def totstr():
    pre,_,post = str(total).partition('.')
    if post.rstrip('0'):
        return str(total)
    else:
        return pre
    
for line in sys.stdin.readlines():
    line = line.rstrip('\n').split('\t')
    line_field = int(line[field]) if line[field].isdigit() else float(line[field])
    line_head = line[0:field]
    line_tail = line[field+1:]
    if line_head != head or line_tail != tail:
        if total > 0:
            print '\t'.join(head + [totstr()] + tail)
        head = line_head
        tail = line_tail
        total = line_field
    else:
        total += line_field
if total > 0:
    print '\t'.join(head + [totstr()] + tail)

