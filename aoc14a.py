import sys
import copy
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
robots = []
for x in lines:
    nums = x.split(sep=',')
    nums1 = nums[1].split(sep=' v=')
    robots.append([[int(nums[0][2:]),int(nums1[0])],[int(nums1[1]),int(nums[-1])]])
print(robots[0])
print(robots[-1])

w = 101
h = 103

for i in range(len(robots)):
    robots[i][0][0] = (robots[i][0][0]+100*robots[i][1][0])%w
    robots[i][0][1] = (robots[i][0][1]+100*robots[i][1][1])%h

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
