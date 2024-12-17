import sys
g = open('input.txt', 'r')
line = g.read()
stones = line.split()
#print(stones)
stonez = []
stones.sort()
i = 0
while i<len(stones):
    stonez.append([stones[i],0])
    while i<len(stones) and stones[i] == stonez[-1][0]:
        stonez[-1][1] += 1
        i += 1
stones = stonez

def dsrt(arr):
    return arr[0]

for i in range(75):
    new = []
    for stone in stones:
        if stone[0] == '0':
            new.append(['1',stone[1]])
        elif len(stone[0])%2 == 0:
            new.append([str(int(stone[0][:len(stone[0])//2])),stone[1]])
            new.append([str(int(stone[0][len(stone[0])//2:])),stone[1]])
        else:
            new.append([str(int(stone[0])*2024),stone[1]])
    new.sort(key=dsrt)
    stones = []
    j = 0
    while j<len(new):
        stones.append([new[j][0],0])
        while j<len(new) and new[j][0] == stones[-1][0]:
            stones[-1][1] += new[j][1]
            j += 1
        
count = 0
for x in stones:
    count += x[1]

print(count)