import sys
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
for i in range(len(lines)):
    lines[i] = list(lines[i])
    

w, h = len(lines[0]), len(lines)
x, y = 0, 0
for i in range(h):
    for j in range(w):
        if lines[i][j] == '^':
            x, y = i, j
            lines[i][j] = 'X'
d = 0
ds = [[-1,0],[0,1],[1,0],[0,-1]]
while(1):
    if (x+ds[d][0]>=0) and (x+ds[d][0]<h) and (y+ds[d][1]>=0) and (y+ds[d][1]<w) and (lines[x+ds[d][0]][y+ds[d][1]]!='#'):
        x += ds[d][0]
        y += ds[d][1]
        lines[x][y] = 'X'
    elif (x+ds[d][0]>=0) and (x+ds[d][0]<h) and (y+ds[d][1]>=0) and (y+ds[d][1]<w):
        d = (d+1)%4
    else:
        break
count = 0
for i in range(h):
    for j in range(w):
        if lines[i][j] == 'X':
            count += 1
#print(lines)
print(count)
