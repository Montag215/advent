import sys
g = open('input.txt', 'r')
line = g.read()[:-1]
#print(line)
disk = []
cur_id = 1
f = True
for x in line:
    if f:
        for i in range(int(x)):
            disk.append(cur_id)
        cur_id += 1
    else:
        for i in range(int(x)):
            disk.append(0)
    f = not f
l = 0
r = len(disk)-1
while r>l:
    if not disk[l]:
        while not disk[r] and r>l:
            r -= 1
        temp = disk[r]
        disk[r] = 0
        r -= 1
        disk[l] = temp
    l += 1
count = 0
for i in range(len(disk)):
    if disk[i]:
        count += i*(disk[i]-1)
print(count)

