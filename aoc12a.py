import sys
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
for i in range(len(lines)):
    lines[i] = list(lines[i])

def price(x, y, plots):
    w = len(plots)
    h = len(plots[0])
    temp = plots[x][y]
    plots[x][y] = '1'
    area = 1
    perim = 0
    dirs = [[1,0],[0,1],[-1,0],[0,-1]]
    for d in dirs:
        if x+d[0]<w and x+d[0]>=0 and y+d[1]<h and y+d[1]>=0:
            if temp == plots[x+d[0]][y+d[1]]:
                ar, pe = price(x+d[0], y+d[1], plots)
                area += ar
                perim += pe
            elif plots[x+d[0]][y+d[1]] != '1':
                perim += 1
        else:
            perim += 1
    return area, perim

def clear(x, y, plots):
    w = len(plots)
    h = len(plots[0])
    plots[x][y] = '0'
    dirs = [[1,0],[0,1],[-1,0],[0,-1]]
    for d in dirs:
        if x+d[0]<w and x+d[0]>=0 and y+d[1]<h and y+d[1]>=0:
            if '1' == plots[x+d[0]][y+d[1]]:
                clear(x+d[0], y+d[1], plots)

count = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] != '0':
            a, b = price(i,j,lines)
            #print(a,b)
            #print(lines[:5])
            #exit()
            count += (a*b)
            clear(i,j,lines)
#print(lines)
print(count)
