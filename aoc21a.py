import sys
import copy
import os
import itertools

sys.setrecursionlimit(10000)

f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()

def keypad(a, b):
    pad = [['7','8','9'],
           ['4','5','6'],
           ['1','2','3'],
           ['.','0','A']]
    ai, aj = 0, 0
    bi, bj = 0, 0
    for i in range(len(pad)):
        for j in range(len(pad[i])):
            if a == pad[i][j]:
                ai, aj = i, j
            if b == pad[i][j]:
                bi, bj = i, j
    ii, jj = bi - ai, bj - aj
    vert = []
    if ii < 0:
        vert = (abs(ii)*['^'])
    else:
        vert = (abs(ii)*['v'])
    if jj < 0:
        vert = vert + (abs(jj)*['<'])
    else:
        vert = vert + (abs(jj)*['>'])
    #c = set(itertools.permutations(vert))
    c = [vert,vert[::-1]]
    if c[0]==c[1]:
        c = [vert]
    d = []
    for cc in c:
        if ( a=='7' or a=='4' or a=='1' ) and (b=='0' or b=='A'):
            if (a=='1' and cc[0]=='v') or (a=='4' and cc[0]=='v' and cc[1]=='v') or (a=='7' and cc[0]=='v' and cc[1]=='v' and cc[2]=='v'):
                continue
        if ( b=='7' or b=='4' or b=='1' ) and (a=='0' or a=='A'):
            if (a=='0' and cc[0]=='<') or (a=='A' and cc[0]=='<' and cc[1]=='<'):
                continue
        d.append(list(cc) + ['A'])
    return d

def dirpad(a, b):
    pad = [['.','^','A'],
           ['<','v','>']]
    ai, aj = 0, 0
    bi, bj = 0, 0
    for i in range(len(pad)):
        for j in range(len(pad[i])):
            if a == pad[i][j]:
                ai, aj = i, j
            if b == pad[i][j]:
                bi, bj = i, j
    ii, jj = bi - ai, bj - aj
    vert = []
    if ii < 0:
        vert = (abs(ii)*['^'])
    else:
        vert = (abs(ii)*['v'])
    if jj < 0:
        vert = vert + (abs(jj)*['<'])
    else:
        vert = vert + (abs(jj)*['>'])
    #c = set(itertools.permutations(vert))
    c = [vert,vert[::-1]]
    if c[0]==c[1]:
        c = [vert]
    d = []
    for cc in c:
        if ( a=='<' ) and (b=='^' or b=='A'):
            if cc[0]=='^':
                continue
        if ( b=='<' ) and (a=='^' or a=='A'):
            if (a=='^' and cc[0]=='<') or (a=='A' and cc[0]=='<' and cc[1]=='<'):
                continue
        d.append(list(cc) + ['A'])
    return d

count = []
for line in lines:
    x = list('A' + line)
    m = []
    moves = [[]]
    for i in range(len(x)-1):
        m.append(keypad(x[i],x[i+1]))
        #print(m)
    for mm in m:
        temp = []
        for mmm in mm:
            for move in moves:
                temp.append(move+mmm)
        moves = temp
    #print(moves)
    #exit()
    movez = moves
    sec = []
    for z in movez:
        x = ['A'] + z
        m = []
        moves = [[]]
        for i in range(len(x)-1):
            m.append(dirpad(x[i],x[i+1]))
        for mm in m:
            temp = []
            for mmm in mm:
                for move in moves:
                    temp.append(move+mmm)
            moves = temp
        #print(x,moves)
        #exit()
        sec.extend(moves)
    #print(sec)
    #movez = list(set(sec))
    #sec.sort()
    movez = sec#list(sec for sec,_ in itertools.groupby(sec))
    sec = []
    for z in movez:
        x = ['A'] + z
        m = []
        moves = [[]]
        for i in range(len(x)-1):
            m.append(dirpad(x[i],x[i+1]))
        for mm in m:
            temp = []
            for mmm in mm:
                for move in moves:
                    temp.append(move+mmm)
            moves = temp
        #print(x,moves)
        #exit()
        sec.extend(moves)
    #exit()
    #print(sec[0])
    val = 1000000000
    for s in sec:
        val = min(val,len(s))
    #print(val)
    count.append(val)

#print(count)
print(int(lines[0][:-1])*count[0]+int(lines[1][:-1])*count[1]+int(lines[2][:-1])*count[2]+int(lines[3][:-1])*count[3]+int(lines[4][:-1])*count[4])