import sys
g = open('input.txt', 'r')
line = g.read()
stones = line.split()
#print(stones)

for i in range(25):
    new = []
    for stone in stones:
        if stone == '0':
            new.append('1')
        elif len(stone)%2 == 0:
            new.append(str(int(stone[:len(stone)//2])))
            new.append(str(int(stone[len(stone)//2:])))
        else:
            new.append(str(int(stone)*2024))
    stones = new

print(len(stones))