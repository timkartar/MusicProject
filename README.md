This repository contains all the code for the distance computation between music pieces using IR model.

Check the folders demo, demogenome, democsv, demomodel for steps. Demo contains for each music note sequence and their strike time extracted from midi tracks using DryWetMidi in c# on visual-studio.

to run the demo use: ./run.sh demo

The distance matrices calculated will be in csvs folder. One using devision and one using substraction weights. 

For details of calculation refer distance.py(with devision weights), sub_wi_dist.py(with sub weights), timestamp.c, ir.c and model.py.

MidiFile names will be generated in txts folder.

2dplot.py is the python code that takes the csv and generates the plot.
