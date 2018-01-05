#!/bin/bash
for f in *.txt
do
s=$(basename -a $f)
echo ${s%.txt} >> ../demonames.txt
done
