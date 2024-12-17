import sys
import copy
import os
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
robots = []
for x in lines:
    nums = x.split(sep=',')
    nums1 = nums[1].split(sep=' v=')
    robots.append([[int(nums[0][2:]),int(nums1[0])],[int(nums1[1]),int(nums[-1])]])
#print(robots[0])
#print(robots[-1])

w = 101
h = 103

def key(r):
    return r[0][0]*200 + r[0][1]
#t = 1200
def metric(r):
    q = [1,1,1,1]
    #r.sort(key=key)
    #for i in range(len(r)-1):
    #    if r[i][0][0] == r[i+1][0][0] and r[i][0][1] == r[i+1][0][1]:
    #        q[0] += 1
    for x in r:
        #if x[0][1] == 26:
        #    q[0] += 1
        #if x[0][1] == 58:
        #    q[1] += 1
        q[0] += abs(x[0][0]-50)
        q[1] += abs(x[0][1]-51)
        '''
        if x[0][0] < 50:
            if x[0][1] < 16:
                q[0] += 1
            elif x[0][1] > 68:
                q[1] += 1
        elif x[0][0] > 50:
            if x[0][1] < 16:
                q[2] += 1
            elif x[0][1] > 68:
                q[3] += 1
                '''
    return (q[0]+q[1]+q[2]+q[3])

count = 100000000000


for t in range(11000):
    for i in range(len(robots)):
        robots[i][0][0] = (robots[i][0][0]+robots[i][1][0])%w
        robots[i][0][1] = (robots[i][0][1]+robots[i][1][1])%h
    board = []
    for i in range(103):
        line = []
        for j in range(101):
            line.append('.')
        board.append(line)
    for x in robots:
        board[x[0][1]][x[0][0]] = '*'
    val = metric(robots)
    if val<=18000:
        print(t)
        count = val
        for i in range(len(board)):
            print(i,end='  ')
            for y in board[i]:
                print(y,end='')
            print()

'''
count = 0
q = [0,0,0,0]
for x in robots:
    if x[0][0] < 50:
        if x[0][1] < 51:
            q[0] += 1
        elif x[0][1] > 51:
            q[1] += 1
    elif x[0][0] > 50:
        if x[0][1] < 51:
            q[2] += 1
        elif x[0][1] > 51:
            q[3] += 1
print(q[0]*q[1]*q[2]*q[3])
'''