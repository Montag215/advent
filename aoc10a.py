import sys
import copy
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
for i in range(len(lines)):
    lines[i] = list(lines[i])
count = 0

def score(x, y, trail):
    if trail[x][y] == '9':
        #trail[x][y] = 'X'
        return 1
    w = len(trail)
    h = len(trail[0])
    retVal = 0
    dirs = [[0,1],[1,0],[0,-1],[-1,0]]
    for d in dirs:
        if x+d[0]<w and x+d[0]>=0 and y+d[1]<h and y+d[1]>=0:
            if trail[x+d[0]][y+d[1]] == str(int(trail[x][y])+1):
                retVal += score(x+d[0], y+d[1], trail)
    return retVal

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == '0':
            #print(i,j)
            count += score(i,j,copy.deepcopy(lines))

print(count)
