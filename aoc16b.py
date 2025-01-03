import sys
import copy
import os
sys.setrecursionlimit(7500)

f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
dp = [[],[],[],[]]
chart = []
for i in range(len(lines)):
    chart.append(list(lines[i]))
    for j in range(4):
        dp[j].append([2*10**5]*len(lines[i]))
#EWNS
dp[0][len(chart)-2][1] = 0

def cost(ch,p,d,y,x):
    dir = [[0,1],[0,-1],[-1,0],[1,0]]
    if ch[y+dir[d][0]][x+dir[d][1]] != '#' and p[d][y+dir[d][0]][x+dir[d][1]] > p[d][y][x] + 1:
        p[d][y+dir[d][0]][x+dir[d][1]] = p[d][y][x] + 1
        cost(ch,p,d,y+dir[d][0],x+dir[d][1])
    for i in range(4):
        if p[i][y][x] > p[d][y][x] + 1000:
            p[i][y][x] = p[d][y][x] + 1000
            cost(ch,p,i,y,x)
    return

cost(chart,dp,0,len(chart)-2,1)

def mark(ch,p,d,y,x):
    dir = [[0,1],[0,-1],[-1,0],[1,0]]
    if ch[y][x] == '#':
        return
    ch[y][x] = 'O'
    if p[d][y][x]==0:
        return
    if ch[y-dir[d][0]][x-dir[d][1]] != '#' and  p[d][y-dir[d][0]][x-dir[d][1]] == p[d][y][x] - 1:
        mark(ch,p,d,y-dir[d][0],x-dir[d][1])
    for i in range(4):
        if p[i][y][x] == p[d][y][x] - 1000:
            mark(ch,p,i,y,x)
    return

mark(chart,dp,2,1,len(chart[i])-2)

o = 0
for i in range(len(chart)):
    for j in range(len(chart[i])):
        print(chart[i][j],end='')
        if chart[i][j]=='O':
            o += 1
    print()

print(dp[0][1][len(chart[0])-2])
print(dp[1][1][len(chart[0])-2])
print(dp[2][1][len(chart[0])-2])
print(dp[3][1][len(chart[0])-2])

print(o)