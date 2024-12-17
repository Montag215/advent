import sys
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
val = 0
up = 0
down = 0
left = 0
right = 0
des = 0
asc = 0
for i in range(len(lines)):
    for j in range(len(lines[0])-3):
        if lines[i][j:j+4] == 'XMAS':
            right += 1
        if lines[i][j:j+4] == 'SAMX':
            left += 1
print(left)
print(right)
for i in range(len(lines)-3):
    for j in range(len(lines[0])):
        if (lines[i][j] == 'X') and (lines[i+1][j] == 'M') and (lines[i+2][j] == 'A') and (lines[i+3][j] == 'S'):
            down += 1
        if (lines[i][j] == 'S') and (lines[i+1][j] == 'A') and (lines[i+2][j] == 'M') and (lines[i+3][j] == 'X'):
            up += 1
print(down)
print(up)
for i in range(len(lines)-3):
    for j in range(len(lines[0])-3):
        if (lines[i][j] == 'X') and (lines[i+1][j+1] == 'M') and (lines[i+2][j+2] == 'A') and (lines[i+3][j+3] == 'S'):
            des += 1
        if (lines[i][j] == 'S') and (lines[i+1][j+1] == 'A') and (lines[i+2][j+2] == 'M') and (lines[i+3][j+3] == 'X'):
            des += 1
        if (lines[i+3][j] == 'X') and (lines[i+2][j+1] == 'M') and (lines[i+1][j+2] == 'A') and (lines[i][j+3] == 'S'):
            asc += 1
        if (lines[i+3][j] == 'S') and (lines[i+2][j+1] == 'A') and (lines[i+1][j+2] == 'M') and (lines[i][j+3] == 'X'):
            asc += 1
print(asc)
print(des)
print(up+down+left+right+asc+des)