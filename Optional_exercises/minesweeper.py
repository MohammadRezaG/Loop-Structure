n,m = map(int,input().split())
k = int(input())
mines = []
for x in range(k):
    mines.append(tuple(map((lambda p: p-1),map(int,input().split()))))
r=[[0]*m for x in range(n)]
for mine in mines:
    for i in range(mine[0]-1,mine[0]+2):
        for j in range(mine[1]-1,mine[1]+2):
            if (i>=0 and i <= (n-1) ) and (j >= 0 and j <= (m-1)):
                if (i,j) == mine:
                    r[i][j] = '*'
                elif type(r[i][j]) == int : r[i][j] += 1
print (*r)


