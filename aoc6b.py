import sys
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
linez = instructions.splitlines()
for i in range(len(linez)):
    linez[i] = list(linez[i])

ww, hh = len(linez[0]), len(linez)
xx, yy = 0, 0
for i in range(hh):
    for j in range(ww):
        if linez[i][j] == '^':
            xx, yy = i, j
            linez[i][j] = 'X'

def test(lines, w, h, x, y):
    d = 0
    ds = [[-1,0],[0,1],[1,0],[0,-1]]
    count = 0
    while(count<25000):
        if (x+ds[d][0]>=0) and (x+ds[d][0]<h) and (y+ds[d][1]>=0) and (y+ds[d][1]<w) and (lines[x+ds[d][0]][y+ds[d][1]]!='#'):
            x += ds[d][0]
            y += ds[d][1]
            #lines[x][y] = 'X'
        elif (x+ds[d][0]>=0) and (x+ds[d][0]<h) and (y+ds[d][1]>=0) and (y+ds[d][1]<w):
            d = (d+1)%4
        else:
            return False
        count += 1
    return True

val = 0
for i in range(hh):
    for j in range(ww):
        if linez[i][j] == '.':
            linez[i][j] = '#'
            if test(linez, ww, hh, xx, yy):
                val += 1
            linez[i][j] = '.'
    print("row")
print(val)


#print(lines)
#print(count)
