import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as hcl
import matplotlib

s=input()
data = pd.read_csv(s)
#for i in data:
#if(i['song1'] == i['song2']):
#print(i['distance'])

data_piv = data.pivot("song1", "song2", "distance").fillna(0)
piv_arr = data_piv.as_matrix()
dist_mat = piv_arr + np.transpose(piv_arr)
for i in range(len(dist_mat)):
	for j in range(len(dist_mat[i])):
		if(i == j):
			dist_mat[i][j] = 0
#dist_mat = np.fill_diagonal(dist_mat, 0)
print(dist_mat)

from sklearn.preprocessing import normalize
from sklearn import manifold
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.patches as dots
import time

model = manifold.TSNE(n_components=2, random_state=0, metric='precomputed')
coords = model.fit_transform(dist_mat)

cmap = plt.get_cmap('Set1')
#colors = [cmap(i) for i in numpy.linspace(0, 1, simulations)]
ls = []
colors = []
while(1):
	try:
		ls.append(input()[:10])
		if(ls[-1][:4]=="guit"):
			colors.append("r")
		else:
			colors.append("b")
	except EOFError:
		break

#plt.figure(figsize=(7, 7))
fig, ax = plt.subplots()
#colors = []
#for i in coords[:,0]:
#    if(i > 7):
#        colors.append("r")
#    else:
#        colors.append("b")
plt.scatter(coords[:, 0], coords[:, 1], marker='o', c=colors, edgecolor='None')
#for label, x, y in zip(ls, coords[:, 0], coords[:, 1]):
#	plt.annotate(label,xy=(x, y), xytext=(-20, 20),
#textcoords='offset points')

#labels = [str(n+1) for n in range(simulations)]
#for i in range(simulations):
 #   markers.append(Line2D([0], [0], linestyle='None', marker="o", markersize=10, markeredgecolor="none", markerfacecolor=colors[i]))
#lgd = plt.legend(markers, labels, numpoints=1, bbox_to_anchor=(1.17, 0.5))
red_dots = dots.Patch(color='red',label='Foreign_Classical_Guitar')
blue_dots = dots.Patch(color='blue',label='Bengali')
plt.legend(handles=[red_dots,blue_dots])
plt.tight_layout()
plt.axis('equal')
plt.show()
