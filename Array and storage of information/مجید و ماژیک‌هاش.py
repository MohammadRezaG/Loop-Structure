Majick = [99999 for x in range(100)]
t=input()
i = list(map(int, input().split()))
for x in i:
    if  Majick[x-1]==99999:
        Majick[x-1]=0
    Majick[x-1]+=1
t=min(Majick)
print((Majick.index(t))+1)