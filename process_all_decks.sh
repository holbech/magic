#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

NEEDS="$(ls *.dec | xargs -i $DIR/parse.py {})"

HAVES="$( cat $1 | grep -v '^$' | awk -F $'\t' 'OFS=FS { print "-"$1,$2 }' )"

echo "$NEEDS"$'\n'"$HAVES" | $DIR/enrich.py | sort -t $'\t' -k2 | $DIR/sum_field.py 0


