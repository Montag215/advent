import sys
import copy
import os
import itertools
import functools

sys.setrecursionlimit(10000)

def char_pos(letter):
    return ord(letter) - ord('a')

def pos_to_char(pos):
    return chr(pos + ord('a'))

f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()

graph = []
for i in range(26*26):
    graph.append([0]*26*26)

for line in lines:
    graph[26*char_pos(line[0])+char_pos(line[1])][26*char_pos(line[3])+char_pos(line[4])] = 1
    graph[26*char_pos(line[3])+char_pos(line[4])][26*char_pos(line[0])+char_pos(line[1])] = 1

count = 0
for i in range(26*26):
    for j in range(i):
        if graph[i][j]:
            for k in range(j):
                if graph[j][k] and graph[i][k]:
                    if i//26==19 or j//26==19 or k//26==19:
                        count += 1

print(count)