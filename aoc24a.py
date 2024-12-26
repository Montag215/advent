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
div = 90
thisdict = dict()
for line in lines[:div]:
    x = line.split(sep=': ')
    thisdict[x[0]] = int(x[1])
endval = len(lines)-1
while len(thisdict) < endval:
    for line in lines[(div+1):]:
        x = line.split(sep=' ')
        if x[0] in thisdict and x[2] in thisdict:
            if x[1]=='XOR':
                thisdict[x[4]] = thisdict[x[0]] ^ thisdict[x[2]]
            elif x[1]=='OR':
                thisdict[x[4]] = thisdict[x[0]] | thisdict[x[2]]
            elif x[1]=='AND':
                thisdict[x[4]] = thisdict[x[0]] & thisdict[x[2]]
            else:
                print('error')
count = 0
for i in range(100):
    if i<10:
        z = 'z0' + str(i)
    else:
        z = 'z' + str(i)
    if z in thisdict:
        count += (thisdict[z])*2**i

#print(thisdict)
print(count)