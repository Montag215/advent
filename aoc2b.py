import sys
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
lizt = []
for x in lines:
    lizt.append(x.split())
print(lizt[0:5])
neolizt = []
for x in lizt:
    temp = []
    temp.append(x)
    temp.append(x[1:])
    for i in range(len(x)-1):
        temp.append(x[:i]+x[(i+1):])
    temp.append(x[:-1])
    neolizt.append(temp)

save = 0
for z in neolizt:
    safe = 0
    for x in z:
        valid = True
        inc = True
        dec = True
        prev = int(x[0])
        for y in x[1:]:
            cur = int(y)
            if cur>prev:
                dec = False
            else:
                inc = False
            if abs(cur-prev)<1 or abs(cur-prev)>3:
                valid = False
            prev = cur
        if valid and (inc or dec):
            safe += 1
        #    print("safe")
        #else:
        #    print("unsafe")
    if safe:
        save += 1
        print("safe")
    else:
        print("unsafe")
print(save)