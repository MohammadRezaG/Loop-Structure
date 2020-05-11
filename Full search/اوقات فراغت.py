y,x=map(int,input().split())
wt=[input() for z in range(y)]
key=input()
c=0

def full_find(i,i2):
    t=0
    rl=[]
    for x in range(len(i)):
        t=i.find(i2,x)
        if not t==-1 and x==t:
            rl.append(t+1)
    return len(rl)
for z in wt:
    c+=full_find(z,key)
for j in range(x):
    s=''
    for i in range(y):
        s+=str(wt[i][j]) 
    c+=full_find(s,key)
print(c)
