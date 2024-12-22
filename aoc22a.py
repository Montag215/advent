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
for line in lines:
    val = int(line)
    for i in range(2000):
        val = process(val)
    count += val

print(count)