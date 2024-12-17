import sys
import copy
sys.setrecursionlimit(3500)
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
data = []
for i in range((len(lines)+1)//4):
    a = lines[4*i].split(sep=', Y')
    b = lines[4*i+1].split(sep=', Y')
    c = lines[4*i+2].split(sep=', Y')
    data.append([[int(a[0][-2:]),int(a[1][-2:])],[int(b[0][-2:]),int(b[1][-2:])],[int(c[0][9:]),int(c[1][1:])]])
print(data[0])
print(data[-1])
print(len(data))
count = 0
for x in data:
    moves = 100000
    for i in range(205):
        for j in range(i+1):
            a = x[0][0]*j + x[1][0]*(i-j)
            b = x[0][1]*j + x[1][1]*(i-j)
            if a==x[2][0] and b==x[2][1]:
                moves = min(moves,(3*j)+(i-j))
                #break
        #if moves:
            #break
    if moves<90000:
        count += moves
print(count)
