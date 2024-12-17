import sys
import copy
import os
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
chart = []
for i in range(50):
    chart.append(list(lines[i]))
#print(chart)
x = 24
y = 24
print(chart[x][y])
for ii in lines[51:]:
    for jj in ii:
        if jj == '^':
            d = [-1,0]
        elif jj == '>':
            d = [0,1]
        elif jj == '<':
            d = [0,-1]
        elif jj == 'v':
            d = [1,0]
        else:
            print("error")
        if chart[y+d[0]][x+d[1]]=='.':
            chart[y+d[0]][x+d[1]] = '@'
            chart[y][x] = '.'
            y, x = y+d[0], x+d[1]
        elif chart[y+d[0]][x+d[1]]=='O':
            n = 1
            while chart[y+n*d[0]][x+n*d[1]]=='O':
                n += 1
            if chart[y+n*d[0]][x+n*d[1]]=='.':
                chart[y+n*d[0]][x+n*d[1]] = 'O'
                chart[y+d[0]][x+d[1]] = '@'
                chart[y][x] = '.'
                y, x = y+d[0], x+d[1]

count = 0
for i in range(len(chart)):
    for j in range(len(chart[i])):
        if chart[i][j] == 'O':
            count += (100*i + j)

for i in range(len(chart)):
    for j in range(len(chart[i])):
        print(chart[i][j],end='')
    print()

print(count)
