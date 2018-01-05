#!/bin/bash
gcc -o ir ir.c -lm
rm -rf $1
mkdir $1 #input destination genome folder
for f in $2/*.txt #input txt folder
do
s=$(basename -a $f)
cd $1 #destination genome folder
> "${s}"
cd ..
n=$(grep -c ^ $f)
echo $n > input
cut -d ' ' -f 1 $f >> input
./ir < input > temp1
cut -d ' ' -f 2,3 $f > temp2
tail -n +3 temp2 > temp3
paste temp1 temp3 > $1/"${s}" 
#sed 's/ /	/g' temp4 > piano_right_genome/"${s}"
rm input  temp1 temp2 temp3
done

#for f in lefttexts/*.txt
#do
#d=$(basename -a $f)
#cd piano_left_genome
#> "${d}"
#cd ..
#n=$(grep -c ^ $f) 
#echo $n > input
#cut -d ' ' -f 1 $f >> input
#./ir < input > temp1
#cut -d ' ' -f 2,3 $f > temp2
#tail -n +3 temp2 > temp3
#paste temp1 temp3 > piano_left_genome/"${d}"
#sed 's/ /	/g' temp4 > piano_left_genome/"${s}" 
#rm input  temp1 temp2 temp3
#done
