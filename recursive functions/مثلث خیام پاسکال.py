#1. for i:0 to n-1 do
#2.     for j:0 to i do
#3.         output "C(i , j) "
#4.     go to the next line of output
import sys,datetime
sys.setrecursionlimit(10**8)
cl=[]
def c(i,j):
    if len(cl)<=i:
        cl.append([0]*(i+1))
    if i==j or j==0:
        cl[i][j]=1
        return 1
    else: 
        if cl[i][j]==0:
            cl[i][j]=c(i-1,j)+c( i-1,j-1)
        return cl[i][j]
bche=True
def inputc():
    mrgt=10
    n=int(input('enter a number : \n'))
    time=datetime.datetime.now()
    if n==0:
        bche=False
        return 0
    b=True
    for i in range(n):
        l=[]
        tl=[]
        j=0
        while b and j<=(i):
            t=c(i,j)
            try:
                if l[len(l)-1]==t and j>=1:
                 tl.extend(l)
                 tl.reverse()
                 l.extend(tl)
                 b=False
                elif l[len(l)-2]==t and j>=1:
                 tl.extend(l)
                 tl.reverse()
                 tl.pop(0)
                 l.extend(tl)
                 b=False
                else:
                    l.append(t)
                    j+=1
            except :
                l.append(t)
                j+=1
        #if i>=mrgt:
        #    print(*l,' ',end='')
        #    print()
        #    mrgt+=100
        #print(*l,' ',end='')
        #print()
        b=True
    print((datetime.datetime.now()-time))
while(bche):

    inputc()
