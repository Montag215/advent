import sys
sys.setrecursionlimit(7500)
z = 2948
f = open('input.txt', 'r')
instructions = f.read()
#print(instructions)
lines = instructions.splitlines()
dp = []
chart = []
for i in range(73):
    if i==0 or i==72:
        chart.append(list('#'*73))
    else:
        chart.append(list('#'+'.'*71+'#'))
    dp.append([5000]*73)
for i in range(z):
    y = lines[i].split(sep=',')
    chart[int(y[0])+1][int(y[1])+1] = '#'
#EWNS
dp[1][1] = 0

def cost(ch,p,y,x):
    dir = [[0,1],[0,-1],[-1,0],[1,0]]
    for d in dir:
        if ch[y+d[0]][x+d[1]] != '#' and p[y+d[0]][x+d[1]] > p[y][x] + 1:
            p[y+d[0]][x+d[1]] = p[y][x] + 1
            cost(ch,p,y+d[0],x+d[1])
    return

cost(chart,dp,1,1)

for x in lines[z:]:
    y = x.split(sep=',')
    chart[int(y[0])+1][int(y[1])+1] = '#'
    for i in range(73):
        for j in range(73):
            dp[i][j] = 5000
    dp[1][1] = 0
    cost(chart,dp,1,1)
    print(x,dp[71][71])


print(dp[71][71])