import sys
import copy
import os
import itertools
import functools

sys.setrecursionlimit(10000)

f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
keys = []
locks = []
for i in range((len(lines)+1)//8):
    neww = []
    for j in range(5):
        newww = -1
        for k in range(7):
            if lines[8*i+k][j] == '#':
                newww += 1
        neww.append(newww)
    if lines[8*i][0] == '#':
        locks.append(neww)
    else:
        keys.append(neww)
print(keys[0],keys[-1],locks[0],locks[-1])
count = 0
for k in keys:
    for l in locks:
        if k[0]+l[0]<6 and k[1]+l[1]<6 and k[2]+l[2]<6 and k[3]+l[3]<6 and k[4]+l[4]<6:
            count += 1
print(count)
