import sys
import copy
import os
sys.setrecursionlimit(7500)

f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
dp = []
chart = []
for i in range(73):
    if i==0 or i==72:
        chart.append(list('#'*73))
    else:
        chart.append(list('#'+'.'*71+'#'))
    dp.append([2*10**5]*73)
for i in range(1024):
    y = lines[i].split(sep=',')
    chart[int(y[0])+1][int(y[1])+1] = '#'
#EWNS
dp[1][1] = 0

def cost(ch,p,d,y,x):
    dir = [[0,1],[0,-1],[-1,0],[1,0]]
    for i in range(4):
        if ch[y+dir[i][0]][x+dir[i][1]] != '#' and p[y+dir[i][0]][x+dir[i][1]] > p[y][x] + 1:
            p[y+dir[i][0]][x+dir[i][1]] = p[y][x] + 1
            cost(ch,p,d,y+dir[i][0],x+dir[i][1])
    return

cost(chart,dp,0,1,1)

#for x in 

print(dp[71][71])