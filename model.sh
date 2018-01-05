#!/bin/bash
rm -rf $3
mkdir $3
for f in $1/*.csv #input csv eg abhijcsv
do
s=$(basename -a $f)
cd $3 #input destination folder
> "${s}"
echo timestamp,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P > "${s}"
cd ..
done
echo $1 > temp
echo $3 >> temp
cat $2 >> temp
python3 model.py < temp #input test names txt

