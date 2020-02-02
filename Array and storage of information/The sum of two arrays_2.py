n,l = map(int, input().split())
a,b = [[[int(j) for j in input().split()] for i in range(n)]for g in range(2)]
for i in range(n):
    for j in range(l):
        print (a[i][j]+b[i][j],end=" ")
    print()