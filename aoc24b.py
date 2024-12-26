import sys
import copy
import os
import itertools
import functools
import random

sys.setrecursionlimit(10000)

def keyf(a):
    if (a[0][0]=='x' or a[0][0] == 'y') and (a[0][2]=='x' or a[0][2] == 'y'):
        return 0
    if a[0][0]=='x' or a[0][0] == 'y':
        return 1
    return 2

f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
div = 90

for i in range(len(lines)):
    lines[i] = lines[i].split(sep=' ')

def trial(lines, newlines=[], doit=False):
    thisdict = dict()
    x = random.randint(0, 2**45-1)
    y = random.randint(0, 2**45-1)
    for i in range(45):
        if x & 2**i:
            if i<10:
                thisdict['x0' + str(i)] = 1
            else:
                thisdict['x' + str(i)] = 1
        else:
            if i<10:
                thisdict['x0' + str(i)] = 0
            else:
                thisdict['x' + str(i)] = 0
        if y & 2**i:
            if i<10:
                thisdict['y0' + str(i)] = 1
            else:
                thisdict['y' + str(i)] = 1
        else:
            if i<10:
                thisdict['y0' + str(i)] = 0
            else:
                thisdict['y' + str(i)] = 0

    endval = len(lines)-1+91
    counter = 0
    while len(thisdict) < endval:
        for xy in lines:
            if xy[0] in thisdict and xy[2] in thisdict and xy[4] not in thisdict:
                if xy[1]=='XOR':
                    thisdict[xy[4]] = thisdict[xy[0]] ^ thisdict[xy[2]]
                elif xy[1]=='OR':
                    thisdict[xy[4]] = thisdict[xy[0]] | thisdict[xy[2]]
                elif xy[1]=='AND':
                    thisdict[xy[4]] = thisdict[xy[0]] & thisdict[xy[2]]
                else:
                    print('error')
                if doit:
                    newlines.append(xy)
        #print(len(thisdict))
        counter += 1
        #if counter >30:
            #print('error')
        #    return 1
    countz = 0
    #countx = 0
    #county = 0
    for i in range(50):
        if i<10:
            z = 'z0' + str(i)
            #x = 'x0' + str(i)
            #y = 'y0' + str(i)
        else:
            z = 'z' + str(i)
            #x = 'x' + str(i)
            #y = 'y' + str(i)
        if z in thisdict:
            #print(z,thisdict[z])
            countz += (thisdict[z])*2**i
        #if x in thisdict:
        #    countx += (thisdict[x])*2**i
        #if y in thisdict:
        #    county += (thisdict[y])*2**i

    #print(thisdict)
    #print(x+y)
    #print(countz)
    return countz^(y+x)

wires = lines[(div+1):]
wires.sort(key=keyf)
val = 0
neww = []
trial(wires,neww,True)
for zz in range(100):
    val |= trial(wires)
score = 0
for i in range(48):
    if (val)&(2**i):
        print(1,end='')
    else:
        print(0,end='')
print()
for i in range(48):
    if (val)&(2**i):
        break
    else:
        score += 1
print(score)

nscore = 0
'''
for i in range(len(neww)):
    for j in range(i):
        ii = neww[i][4]
        jj = neww[j][4]

        neww[i][4] = jj
        neww[j][4] = ii
        #if neww[i][4] == neww[i][2] or neww[i][4] == neww[i][0]:
        #    continue
        #if neww[j][4] == neww[j][2] or neww[j][4] == neww[j][0]:
        #    continue
        val = 0
        for zz in range(20):
            val |= trial(neww)
        nscore = 0
        for i in range(48):
            if (val)&(2**i):
                break
            else:
                nscore += 1
        if nscore>score:
            print(ii, jj)
            print(nscore)
            exit()
        else:
            neww[i][4] = ii
            neww[j][4] = jj
print(nscore)

'''
