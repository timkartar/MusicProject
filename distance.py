import numpy as np
import matplotlib.pyplot as plt
#import math
def KL(a, b):
	a = np.asarray(a, dtype=np.float)
	b = np.asarray(b, dtype=np.float)
	if(len(a) == 0):
		return float('inf')
	weight = (np.count_nonzero(a) / (np.count_nonzero(b)+1))
	b = np.add(b,0.000001)
	return abs(weight)*np.sum(np.where(a != 0, a * np.log(a / b), 0))
print("song1,song2,distance")
name = input()
while(1):
	s1 = input()
	s2 = input()
	l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
	path_to_csv1 = name + "/"+ s1 + ".csv"
	path_to_csv2 = name + "/"+ s2 + ".csv"
	try:
		song1 = np.genfromtxt(path_to_csv1, dtype=None, delimiter=',', names=True)
		song2 = np.genfromtxt(path_to_csv2, dtype=None, delimiter=',', names=True)
		#print(s1,s2)
	except OSError:
		continue
	#print(song1,song2)
	#plt.ylim((0,1))
	#plt.plot(song1['timestamp'],song1[l[3]])
	#plt.show()
	try:
		minlen = min([len(song1),len(song2)])
		total_distance = 0
		for i in l:
			sum1 = sum(song1[i][:minlen])
			if(sum1 != 0):
				l1 = np.divide(song1[i][:minlen],sum1)
			else:
				l1 = song1[i][:minlen]
			#print(l1, sum(l1))
			sum2 = sum(song2[i][:minlen])
			if(sum2 != 0):
				l2 = np.divide(song2[i][:minlen],sum2)
			else:
				l2 = song2[i][:minlen]
			#l2 = np.multiply(l2,0)
			#print(l2)
			distance = abs(KL(l2,l1)*0.5 + KL(l1,l2)*0.5)
			#print('motif:',i)
			#print('motif_distance:',distance)
			total_distance += distance
		print(str(s1) + "," + str(s2) + "," + str(total_distance))
	except ValueError:
		pass

