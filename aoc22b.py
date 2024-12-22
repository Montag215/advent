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

def process(snum):
    nnum = ((snum*64)^snum)%16777216
    nnum = ((nnum//32)^nnum)%16777216
    nnum = ((nnum*2048)^nnum)%16777216
    return nnum

#print(process(process(123)))
#val = 2024
count = 0
nums = []
for line in lines:
    val = int(line)
    buyer = [val]
    for i in range(2000):
        val = process(val)
        buyer.append(val)
    #count += val
    nums.append(buyer)

for i in range(len(nums)):
    for j in range(len(nums[i])):
        nums[i][j] = int(str(nums[i][j])[-1])

d = copy.deepcopy(nums)

for i in range(len(nums)):
    for j in range(len(nums[i])-1):
        d[i][j] = nums[i][j+1] - nums[i][j]

delta = []
valid = []

for i in range(19):
    a = []
    for j in range(19):
        b = []
        for k in range(19):
            b.append([0]*19)
        a.append(b)
    delta.append(a)

valid = copy.deepcopy(delta)

for i in range(len(nums)):
    for j in range(len(nums[i])-4):
        if not valid[d[i][j]+9][d[i][j+1]+9][d[i][j+2]+9][d[i][j+3]+9]:
            valid[d[i][j]+9][d[i][j+1]+9][d[i][j+2]+9][d[i][j+3]+9] = 1
            delta[d[i][j]+9][d[i][j+1]+9][d[i][j+2]+9][d[i][j+3]+9] += nums[i][j+4]
    for ii in range(19):
        for jj in range(19):
            for kk in range(19):
                for ll in range(19):
                    valid[ii][jj][kk][ll] = 0

for ii in range(19):
    for jj in range(19):
        for kk in range(19):
            for ll in range(19):
                count = max(count,delta[ii][jj][kk][ll])

print(count)