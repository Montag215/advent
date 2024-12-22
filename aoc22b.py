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

dnums = copy.deepcopy(nums)

for i in range(len(nums)):
    for j in range(len(nums[i])-1):
        dnums[i][j] = nums[i][j+1] - nums[i][j]

delta = []
#for i in range(5):
#    for j in range(5):
#        for k in range(5):
#            for l in range(5):
#                delta.append([i,j,k,l])

for i in range(19):
    for j in range(19):
        for k in range(19):
            for l in range(19):
                delta.append([i-9,j-9,k-9,l-9])

for d in delta:
    if abs(d[0]+d[1]+d[2]+d[3])>9 or abs(d[1]+d[2]+d[3])>9 or abs(d[0]+d[1]+d[2])>9 or abs(d[0]+d[1])>9 or abs(d[1]+d[2])>9 or abs(d[2]+d[3])>9:
        continue
    total = 0
    for i in range(len(nums)):
        for j in range(len(nums[i])-4):
            if d[0]==dnums[i][j] and d[1]==dnums[i][j+1] and d[2]==dnums[i][j+2] and d[3]==dnums[i][j+3]:
                total += nums[i][j+4]
                break
    count = max(count,total)



print(count)