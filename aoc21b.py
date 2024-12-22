import sys
import copy
import os
import itertools
import functools

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
        #break
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
    if len(d)==2:
        if ii < 0:
            if jj < 0:
                d = [d[1]]
            else:
                d = [d[1]]
        else:
            if jj< 0:
                d = [d[1]]
            else:
                d = [d[1]]
    return d

@functools.cache
def rec_key(a, b, d):
    if d==0:
        return 1
    
    if a=='A':
        if b=='A':
            return 1
        if b=='^':
            return rec_key('A','<',d-1) + rec_key('<','A',d-1)
        if b=='>':
            return rec_key('A','v',d-1) + rec_key('v','A',d-1)
        if b=='v':
            return min(rec_key('A','v',d-1)+rec_key('v','<',d-1)+rec_key('<','A',d-1),rec_key('A','<',d-1)+rec_key('<','v',d-1)+rec_key('v','A',d-1))
        if b=='<':
            return rec_key('A','v',d-1) + rec_key('v','<',d-1) + rec_key('<','<',d-1) + rec_key('<','A',d-1)
    if a=='^':
        if b=='A':
            return rec_key('A','>',d-1) + rec_key('>','A',d-1)
        if b=='^':
            return 1
        if b=='>':
            return min(rec_key('A','v',d-1)+rec_key('v','>',d-1)+rec_key('>','A',d-1),rec_key('A','>',d-1)+rec_key('>','v',d-1)+rec_key('v','A',d-1))
        if b=='v':
            return rec_key('A','v',d-1) + rec_key('v','A',d-1)
        if b=='<':
            return rec_key('A','v',d-1) + rec_key('v','<',d-1) + rec_key('<','A',d-1)
    if a=='>':
        if b=='A':
            return rec_key('A','^',d-1) + rec_key('^','A',d-1)
        if b=='^':
            return min(rec_key('A','<',d-1)+rec_key('<','^',d-1)+rec_key('^','A',d-1),rec_key('A','^',d-1)+rec_key('^','<',d-1)+rec_key('<','A',d-1))
        if b=='>':
            return 1
        if b=='v':
            return rec_key('A','<',d-1) + rec_key('<','A',d-1)
        if b=='<':
            return rec_key('A','<',d-1) + rec_key('<','<',d-1) + rec_key('<','A',d-1)
    if a=='v':
        if b=='A':
            return min(rec_key('A','>',d-1)+rec_key('>','^',d-1)+rec_key('^','A',d-1),rec_key('A','^',d-1)+rec_key('^','>',d-1)+rec_key('>','A',d-1))
        if b=='^':
            return rec_key('A','^',d-1)+rec_key('^','A',d-1)
        if b=='>':
            return rec_key('A','>',d-1) + rec_key('>','A',d-1)
        if b=='v':
            return 1
        if b=='<':
            return rec_key('A','<',d-1) + rec_key('<','A',d-1)
    if a=='<':
        if b=='A':
            return rec_key('A','>',d-1) + rec_key('>','>',d-1) + rec_key('>','^',d-1) + rec_key('^','A',d-1)
        if b=='^':
            return rec_key('A','>',d-1) + rec_key('>','^',d-1) + rec_key('^','A',d-1)
        if b=='>':
            return rec_key('A','>',d-1) + rec_key('>','>',d-1) + rec_key('>','A',d-1)
        if b=='v':
            return rec_key('A','>',d-1) + rec_key('>','A',d-1)
        if b=='<':
            return 1
    print("error")
    return 1

def itera(z):
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
    return moves

def keyf(a):
    return len(a)

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
    sec = moves
    m_min = 1000000000000000
    for x in sec:
        z = ['A'] + x
        m = 0
        for i in range(len(z)-1):
            m += rec_key(z[i],z[i+1],25)
        if m<m_min:
            m_min = m
    #print(m_min)
    count.append(m_min)

#print(count)
print(int(lines[0][:-1])*count[0]+int(lines[1][:-1])*count[1]+int(lines[2][:-1])*count[2]+int(lines[3][:-1])*count[3]+int(lines[4][:-1])*count[4])