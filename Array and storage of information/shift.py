l,n = map(int, input().split())
i = list(map(int, input().split()))
c,pc=0,i[0]
for y in range(n):
    for x in range(1,l):
        c=i[x]
        i[x]=pc
        pc=c
    i[0]=pc
for x in i:
    print(x,end=' ')