import sys
import copy
import os
import itertools
import functools

sys.setrecursionlimit(10000)

def char_pos(letter):
    return ord(letter) - ord('a')

def ptc(pos):
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
     for l in range(k):
      if graph[l][j] and graph[l][k] and graph[i][l]:
       for ii in range(l):
        if graph[ii][j] and graph[ii][k] and graph[ii][l] and graph[ii][i]:
         for jj in range(ii):
          if graph[jj][j] and graph[jj][k] and graph[jj][l] and graph[jj][i] and graph[jj][ii]:
           for kk in range(jj):
            if graph[kk][j] and graph[kk][k] and graph[kk][l] and graph[kk][i] and graph[kk][ii] and graph[kk][jj]:
             for ll in range(kk):
              if graph[ll][j] and graph[ll][k] and graph[ll][l] and graph[ll][i] and graph[ll][ii] and graph[ll][jj] and graph[ll][kk]:
               for a in range(ll):
                if graph[a][j] and graph[a][k] and graph[a][l] and graph[a][i] and graph[a][ii] and graph[a][jj] and graph[a][kk] and graph[a][ll]:
                 for b in range(a):
                  if graph[b][j] and graph[b][k] and graph[b][l] and graph[b][i] and graph[b][ii] and graph[b][jj] and graph[b][kk] and graph[b][ll] and graph[b][a]:
                   for c in range(b):
                     if graph[c][j] and graph[c][k] and graph[c][l] and graph[c][i] and graph[c][ii] and graph[c][jj] and graph[c][kk] and graph[c][ll] and graph[c][a] and graph[c][b]:
                      for d in range(c):
                       if graph[d][j] and graph[d][k] and graph[d][l] and graph[d][i] and graph[d][ii] and graph[d][jj] and graph[d][kk] and graph[d][ll] and graph[d][a] and graph[d][b] and graph[d][c]:
                        for e in range(d):
                         if graph[e][j] and graph[e][k] and graph[e][l] and graph[e][i] and graph[e][ii] and graph[e][jj] and graph[e][kk] and graph[e][ll] and graph[e][a] and graph[e][b] and graph[e][c] and graph[e][d]:
                          count += 1
                          for val in [i,j,k,l,ii,jj,kk,ll,a,b,c,d,e]:
                           print(ptc(val//26),ptc(val%26))

print(count)