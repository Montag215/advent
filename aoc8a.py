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
                        coords.append([2*i-k,2*j-l])
                        coords.append([2*k-i,2*l-j])
for x in coords:
    if x[0]>=0 and x[0]<len(lines) and x[1]>=0 and x[1]<len(lines[0]):
        lines[x[0]][x[1]] = '#'
for x in lines:
    for y in x:
        if y=='#':
            count += 1
print(count)