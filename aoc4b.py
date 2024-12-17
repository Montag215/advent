import sys
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()

val = 0
for i in range(len(lines)-2):
    for j in range(len(lines[0])-2):
        if (lines[i][j]=='M') and (lines[i+2][j]=='M') and (lines[i][j+2]=='S') and (lines[i+2][j+2]=='S') and (lines[i+1][j+1]=='A'):
            val += 1
        if (lines[i][j]=='S') and (lines[i+2][j]=='S') and (lines[i][j+2]=='M') and (lines[i+2][j+2]=='M') and (lines[i+1][j+1]=='A'):
            val += 1
        if (lines[i][j]=='S') and (lines[i+2][j]=='M') and (lines[i][j+2]=='S') and (lines[i+2][j+2]=='M') and (lines[i+1][j+1]=='A'):
            val += 1
        if (lines[i][j]=='M') and (lines[i+2][j]=='S') and (lines[i][j+2]=='M') and (lines[i+2][j+2]=='S') and (lines[i+1][j+1]=='A'):
            val += 1
print(val)