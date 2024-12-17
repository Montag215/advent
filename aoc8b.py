import sys
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
for i in range(len(lines)):
    lines[i] = list(lines[i])
count = 0
coords = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] != '.':
            for k in range(len(lines)):
                for l in range(len(lines[0])):
                    if lines[i][j] == lines[k][l] and not (i==k and j==l):
                        a = i-k
                        b = j-l
                        for n in range(100):
                            while a%(n+2)==0 and b%(n+2)==0:
                                #print("d")
                                a //= (n+2)
                                b //= (n+2)
                        d = int((i-k)//a)
                        for n in range(210):
                            coords.append([int(i+n*(i-k)//d),int(j+n*(j-l)//d)])
                            coords.append([int(k+n*(k-i)//d),int(l+n*(l-j)//d)])
for x in coords:
    if x[0]>=0 and x[0]<len(lines) and x[1]>=0 and x[1]<len(lines[0]):
        lines[x[0]][x[1]] = '#'
#print(lines)
for x in lines:
    for y in x:
        if y=='#':
            count += 1
print(count)