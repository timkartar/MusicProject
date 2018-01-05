#!/bin/bash
rm txts/$1
for f in $2/*.txt
do
s=$(basename -a $f)
echo ${s%.txt} >> txts/$1
done
