import sys
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()

rules = []
lim = 0
for i in range(len(lines)):
    if len(lines[i])<3:
        lim = i
        break
    elif lines[i][2] == '|':
        rules.append([int(lines[i][:2]),int(lines[i][3:])])
#print(rules)
updates = []
for x in lines[lim+1:]:
    temp = []
    for y in x.split(sep=','):
        temp.append(int(y))
    updates.append(temp)
#print(updates)
retval = 0

def tezt(r, u):
    pos1 = -1
    pos2 = -1
    for i in range(len(u)):
        if r[0] == u[i]:
            pos1 = i
        if r[1] == u[i]:
            pos2 = i
    if (pos1!=-1) and (pos2!=-1) and (pos1>pos2):
        u[pos1], u[pos2] = u[pos2], u[pos1]
        return False
    return True
            
for x in updates:
    valid = 1
    for y in rules:
        if not tezt(y, x):
            valid = 0
    for y in rules:
        if not tezt(y, x):
            valid = 0
    for y in rules:
        if not tezt(y, x):
            valid = 0
    for y in rules:
        if not tezt(y, x):
            valid = 0
    for y in rules:
        if not tezt(y, x):
            valid = 0
    for y in rules:
        if not tezt(y, x):
            valid = 0
    for y in rules:
        if not tezt(y, x):
            valid = 0
    for y in rules:
        if not tezt(y, x):
            valid = 0
    for y in rules:
        if not tezt(y, x):
            valid = 0
    for y in rules:
        if not tezt(y, x):
            valid = 0
    for y in rules:
        if not tezt(y, x):
            valid = 0
    if not valid:
        retval += x[len(x)//2]
print(retval)