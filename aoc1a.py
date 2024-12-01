import sys

f = open('aoc1a.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
print(lines[0][0:5])
print(lines[0][8:13])
val = 0
list1 = []
list2 = []
for i in range(len(lines)):
	list1.append(int(lines[i][0:5]))
	list2.append(int(lines[i][8:13]))
list1.sort()
list2.sort()
for i in range(len(lines)):
	val += abs(list1[i]-list2[i])
print(val)
neoval = 0
freq = []
for i in range(max(list2)+max(list1)):
	freq.append(0)
for i in range(len(list2)):
	freq[list2[i]] += 1
for i in range(len(list1)):
	neoval += (list1[i]*freq[list1[i]])
print(neoval)
