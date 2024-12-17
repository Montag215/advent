import sys
import copy
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
data = []
for i in range((len(lines)+1)//4):
    a = lines[4*i].split(sep=', Y')
    b = lines[4*i+1].split(sep=', Y')
    c = lines[4*i+2].split(sep=', Y')
    #data.append([[int(a[0][-2:]),int(a[1][-2:])],[int(b[0][-2:]),int(b[1][-2:])],[int(c[0][9:]),int(c[1][1:])]])
    data.append([[int(a[0][-2:]),int(a[1][-2:])],[int(b[0][-2:]),int(b[1][-2:])],[int(c[0][9:])+10000000000000,int(c[1][1:])+10000000000000]])
print(data[0])
print(data[-1])
print(len(data))
count = 0

def solver(d):
    pitch = (d[0][1] * d[1][0] > d[1][1] * d[0][0])
    l = 0
    r = 10000000000000
    '''
    for m in range(300):
        xnew = d[2][0] - m * d[1][0]
        ynew = d[2][1] - m * d[1][1]
        if xnew%d[0][0]==0 and ynew%d[0][1]==0 and xnew/d[0][0]==ynew/d[0][1]:
            return 3*(xnew//d[0][0]) + m
'''
    
    while r>=l:
        m = (l+r)//2
        xnew = d[2][0] - m * d[1][0]
        ynew = d[2][1] - m * d[1][1]
        if xnew<0 or ynew<0:
            r = m - 1
        elif xnew%d[0][0]==0 and ynew%d[0][1]==0 and xnew//d[0][0]==ynew//d[0][1]:
            return 3*(xnew//d[0][0]) + m
        elif xnew * d[0][1] > ynew * d[0][0]:
            if pitch:
                l = m + 1
            else:
                r = m - 1
        elif xnew * d[0][1] < ynew * d[0][0]:
            if pitch:
                r = m - 1
            else:
                l = m + 1
        else:
            return 0

    return 0

for x in data:
    count += solver(x)
print(count)