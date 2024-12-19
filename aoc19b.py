import sys
sys.setrecursionlimit(7500)
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
options = lines[0].split(sep=', ')
count = 0
for x in lines[2:]:
    #print(x)
    #break
    possible = [1]
    for i in range(len(x)):
        possible.append(0)
    for i in range(len(possible)-1):
        if possible[i]:
            for option in options:
                if x[i:].startswith(option):
                    possible[i+len(option)] += possible[i]
    if possible[-1]:
        count += possible[-1]
print(len(lines))
print(count)