import sys
import copy
import os
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
chart = []
z = 0
for i in range(50):
    line = []
    for x in lines[i]:
        if x=='#':
            line.append('#')
            line.append('#')
        elif x=='O':
            line.append('[')
            line.append(']')
        elif x=='.':
            line.append('.')
            line.append('.')
        elif x=='@':
            line.append('@')
            line.append('.')
        else:
            print("error")
    chart.append(line)
#print(chart)
x = 48
y = 24

def push(ch,yy,xx,d):
    if not d[0]:
        n = 1
        while ch[yy][xx+n*d[1]]==']' or ch[yy][xx+n*d[1]]=='[':
            n += 1
        if ch[yy][xx+n*d[1]]=='.':
            while n:
                ch[yy][xx+n*d[1]] = ch[yy][xx+(n-1)*d[1]]
                n -= 1
            ch[yy][xx] = '@'
            return True
    else:
        if ch[yy][xx] == '.':
            return True
        elif ch[yy][xx] == ']':
            return push(ch,yy,xx-1,d)
        elif ch[yy][xx] == '#':
            return False
        return push(ch,yy+d[0],xx,d) and push(ch,yy+d[0],xx+1,d)
    return False

def pushup(ch,yy,xx,d):
    if ch[yy][xx] == '.':
        return
    elif ch[yy][xx] == ']':
        pushup(ch,yy,xx-1,d)
        return
    pushup(ch,yy+d[0],xx,d)
    pushup(ch,yy+d[0],xx+1,d)
    ch[yy+d[0]][xx] = ch[yy][xx]
    ch[yy+d[0]][xx+1] = ch[yy][xx+1]
    ch[yy][xx] = '.'
    ch[yy][xx+1] = '.'

print(chart[y][x])
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
        elif chart[y+d[0]][x+d[1]]=='[' or chart[y+d[0]][x+d[1]]==']':
            if not d[0]:
                if push(chart,y+d[0],x+d[1],d):
                    chart[y][x] = '.'
                    y, x = y+d[0], x+d[1]
            else:
                if push(chart,y+d[0],x+d[1],d):
                    pushup(chart,y+d[0],x+d[1],d)
                    chart[y][x] = '.'
                    chart[y+d[0]][x+d[1]] = '@'
                    y, x = y+d[0], x+d[1]
        #z += 1
        if z>114:
            break
    if z>114:
        break

count = 0
for i in range(len(chart)):
    for j in range(len(chart[i])):
        if chart[i][j] == '[':
            count += (100*i + j)

for i in range(len(chart)):
    for j in range(len(chart[i])):
        print(chart[i][j],end='')
    print()

print(count)
