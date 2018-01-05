#!/bin/bash
rm -rf $1
mkdir $1 #destination csv folder
#chmod 0777 abhijcsv
for f in $2/*.txt #source genome folder
do
s=$(basename -a $f)
s=${s%.txt}
s=$s".csv"
cd $1
> "${s}"
echo motifs,time >> "${s}"
cd ..
cut -f1 $f > temp1
cut -f2 $f | cut -d ' ' -f1 > temp2
paste -d ',' temp1 temp2 >> $1/"${s}"
done

#for f in piano_left_genome/*.txt
#do
#s=$(basename -a $f)
#s=${s%.txt}
#s=$s".csv"
#cd leftcsv
#> "${s}"
#echo motifs,time >> "${s}"
#cd ..
#cut -f1 $f > temp1
#cut -f2 $f | cut -d ' ' -f1 > temp2
#paste -d ',' temp1 temp2 >> leftcsv/"${s}"
#done

