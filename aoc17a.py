import sys
import copy
reg = [61657405,0,0]
program = [2,4,1,2,7,5,4,3,0,3,1,7,5,5,3,0]

def combo(r,c):
    if c==4 or c==5 or c==6:
        return r[c-4]
    return c

i = 0
while i>=0 and i<len(program)-1:
    if program[i]==0:
        reg[0] //= 2**combo(reg,program[i+1])
        i += 2
    elif program[i]==1:
        reg[1] ^= program[i+1]
        i += 2
    elif program[i]==2:
        reg[1] = combo(reg,program[i+1])%8
        i += 2
    elif program[i]==3:
        if reg[0]:
            i = program[i+1]
        else:
            i += 2
    elif program[i]==4:
        reg[1] ^= reg[2]
        i += 2
    elif program[i]==5:
        print(combo(reg,program[i+1])%8)
        i += 2
    elif program[i]==6:
        reg[1] = reg[0] // 2**combo(reg,program[i+1])
        i += 2
    elif program[i]==7:
        reg[2] = reg[0] // 2**combo(reg,program[i+1])
        i += 2
    else:
        print('error')
