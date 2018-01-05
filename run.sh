#!/bin/bash
notetxt="$1"

echo got input 

echo generating genome .....

suf="genome"
genometxt="$1$suf"
./ir.sh $genometxt $notetxt

echo genome generated
echo generating csv .....
suf="csv"
csv="$notetxt$suf"
./csvgen.sh $csv $genometxt


echo csv generated
echo generating list of names .....
suf="names.txt"
names="$1$suf"
./filenames.sh $names $genometxt

echo list of names  generated
echo generating model .....

suf="model"
model="$1$suf"
./model.sh $csv txts/$names $model

echo model generated

echo $model > input
python combinations.py < txts/$names | sed 's/,/\n/g' >> input
suf="dist.csv"
distances="$1$suf"
echo computing ditance with devision weight at csvs/$distances

python distance.py < input > csvs/$distances

echo distance with devision weights calculated
echo plotting 2D representation......

echo csvs/$distances > temp
cat txts/$names >> temp
python 2dplot.py < temp

echo 2D representation plotted

suf="dist_sub.csv"
distances="$1$suf"
echo computing distance with subtraction weight at csvs/$distances
python sub_wt_dist.py < input > csvs/$distances 

echo distances with subtraction weights calculated
echo plotting 2D representation......

echo csvs/$distances > temp
cat txts/$names >> temp
python 2dplot.py < temp

echo 2D representation plotted

