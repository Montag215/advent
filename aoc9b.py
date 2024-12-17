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
while r>0:
    if disk[r]:
        size = 1
        while r>0 and disk[r-1]==disk[r]:
            size += 1
            r -= 1
        l = 0
        run = 0
        while l<r:
            if not disk[l]:
                run += 1
            else:
                run = 0
            if run == size:
                temp = disk[l-size+1:l+1]
                disk[l-size+1:l+1] = disk[r:r+size]
                disk[r:r+size] = temp
                #print(disk[l-size+1:l+1])
                break
            l += 1
    r -= 1
    '''
    if not disk[l]:
        while not disk[r] and r>l:
            r -= 1
        temp = disk[r]
        disk[r] = 0
        r -= 1
        disk[l] = temp
    l += 1
    '''
    #if r%10 == 0:
    #    print("10")

count = 0
for i in range(len(disk)):
    if disk[i]:
        count += i*(disk[i]-1)
print(count)
