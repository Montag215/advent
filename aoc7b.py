import sys
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
val = 0

def test(fin, ops):
    if len(ops) == 1:
        return fin == ops[0]
    temp = ops[1]
    ops[1] = temp * ops[0]
    a = test(fin, ops[1:])
    ops[1] = temp + ops[0]
    b = test(fin, ops[1:])
    ops[1] = int(str(ops[0]) + str(temp))
    c = test(fin, ops[1:])
    ops[1] = temp
    return a or b or c

for line in lines:
    x = line.split(sep=': ')
    final = int(x[0])
    nums = x[1].split(sep=' ')
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    if test(final,nums):
        val += final

print(val)