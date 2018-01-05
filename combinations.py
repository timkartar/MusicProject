import itertools
#with open('pianofrenchnames.txt') as f:
#	colors = ', '.join(f.read().splitlines()).split(', ')
#with open('pianofrenchnames.txt') as f:
#	for i in f:
#		for car in i.strip().split('\n'):
#			for j in f:
#				for color in j.strip().split('\n'):
#					print(car, color)
#for r in itertools.permutations(colors,2):
#a	print(r[0] + "," + r[1])
x = []
while(1):
	try:
		x.append(input())
	except EOFError:
		break
y = [p for p in itertools.product(x, repeat=2)]
for i in y:
	print(i[0] + "," + i[1])
