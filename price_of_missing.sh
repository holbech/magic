#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

NEEDS="$($DIR/parse.py $1 | cut -f1,3)"

HAVES="$( cat $2 | grep -v '^$' | awk -F $'\t' 'OFS=FS { print "-"$1,$2 }' )"

echo $1 `echo "$NEEDS"$'\n'"$HAVES" | sort -t $'\t' -k2 | $DIR/sum_field.py 0 | $DIR/enrich.py | awk -F $'\t' '{ print $1+$9 }' | $DIR/sum_field.py 0`


