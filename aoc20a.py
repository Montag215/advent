import sys
import copy
import os
sys.setrecursionlimit(10000)

f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
dp = []
chart = []

for i in range(len(lines)):
    chart.append(list(lines[i]))
    dp.append([2*10**5]*len(lines[i]))
#EWNS
for i in range(len(lines)):
    for j in range(len(lines)):
        if chart[i][j] == 'S':
            print('S',i,j)
            si, sj = i, j
        if chart[i][j] == 'E':
            ei, ej = i, j
            print('E',i,j)
dp[si][sj] = 0

def cost(ch,p,d,y,x):
    dir = [[0,1],[0,-1],[-1,0],[1,0]]
    for i in range(4):
        if ch[y+dir[i][0]][x+dir[i][1]] != '#' and p[y+dir[i][0]][x+dir[i][1]] > p[y][x] + 1:
            p[y+dir[i][0]][x+dir[i][1]] = p[y][x] + 1
            cost(ch,p,d,y+dir[i][0],x+dir[i][1])
    return

cost(chart,dp,0,si,sj)
'''
def mark(ch,p,d,y,x):
    dir = [[0,1],[0,-1],[-1,0],[1,0]]
    if ch[y][x] == '#':
        return
    ch[y][x] = 'O'
    if p[y][x]==0:
        return
    for i in range(4):
        if ch[y-dir[i][0]][x-dir[i][1]] != '#' and  p[y-dir[i][0]][x-dir[i][1]] == p[y][x] - 1:
            mark(ch,p,d,y-dir[i][0],x-dir[i][1])
    return

mark(chart,dp,0,ei,ej)
'''
count = 0
cheats = [[0,2],[2,0]]
#for i in range(21):
#    for j in range(21):
#        if i + j <= 20:
#            cheats.append([i,j])
for c in cheats:
    for i in range(len(chart)-c[0]):
        for j in range(len(chart[0])-c[1]):
            if chart[i][j] != '#' and chart[i+c[0]][j+c[1]] != '#' and abs(dp[i][j]-dp[i+c[0]][j+c[1]]) >= (100+c[0]+c[1]):
                count += 1

#for i in range(len(chart)-2):
#    for j in range(len(chart[0])):
#        if chart[i][j] != '#' and chart[i+2][j] != '#' and abs(dp[i][j]-dp[i+2][j]) >= 102:
#            count += 1

#for i in range(len(chart)):
#    for j in range(len(chart[i])):
#        print(chart[i][j],end='')
        #if chart[i][j]=='O':
        #    o += 1
#    print()
#print(dp)
#print(dp[ei][ej])
print(count)