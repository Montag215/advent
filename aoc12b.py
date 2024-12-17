import sys
sys.setrecursionlimit(3500)
f = open('output.txt', 'r')
instructions = f.read()
#print(instructions)
global lines
lines = instructions.splitlines()
for i in range(len(lines)):
    lines[i] = list(lines[i])
linez = []
for i in range(len(lines)):
    sub = []
    for j in range(len(lines[i])):
        sub.extend([lines[i][j]])
    linez.extend([sub])
print(len(lines),len(lines[i]))
lines = linez
print(len(lines),len(lines[i]))
#for i in range(19):
#    print(lines[i][0:19])

def price(x, y, plots):
    w = len(plots)
    h = len(plots[0])
    temp = plots[x][y]
    plots[x][y] = '1'
    area = 1
    perim = 0
    dirs = [[0,1],[-1,0],[0,-1],[1,0]]
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

def wallhug(x, y, plots):
    w = len(plots)
    h = len(plots[0])
    dirs = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]]
    plots[x][y] = '2'
    sim = 0
    corner = 0
    for d in dirs:
        if x+d[0]<w and x+d[0]>=0 and y+d[1]<h and y+d[1]>=0:
            if '1' == plots[x+d[0]][y+d[1]] or '2' == plots[x+d[0]][y+d[1]]:
                sim += 1
    if sim==7 or sim==3 or sim==4:
        corner += 1
    dirs = [[1,0],[0,1],[-1,0],[0,-1]]
    for d in dirs:
        if x+d[0]<w and x+d[0]>=0 and y+d[1]<h and y+d[1]>=0:
            if '1' == plots[x+d[0]][y+d[1]]:
                corner += wallhug(x+d[0], y+d[1], plots)
    return corner


def clear(x, y, plots):
    w = len(plots)
    h = len(plots[0])
    plots[x][y] = '0'
    dirs = [[1,0],[0,1],[-1,0],[0,-1]]
    for d in dirs:
        if x+d[0]<w and x+d[0]>=0 and y+d[1]<h and y+d[1]>=0:
            if '2' == plots[x+d[0]][y+d[1]]:
                clear(x+d[0], y+d[1], plots)

count = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] != '0':
            a, b = price(i,j,lines)
            #print(a,b)
            #print(lines[:5])
            #exit()
            #if i>-1:
            #    for i in range(19):
            #        print(lines[i][0:49])
            #    exit()
            count += (a*wallhug(i,j,lines))
            clear(i,j,lines)
#for i in range(19):
#    print(lines[i][0:19])
print(count//9)
