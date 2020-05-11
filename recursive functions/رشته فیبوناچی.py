def fib(n):
    l=[1,2]
    if n==1:
        l=[1]
    elif n==2:
        l=[1,2]
    else:
        for x in range(2,n):
           l.append(l[x-1]+l[x-2]) 
    return l
n=int(input())
lfib=fib(n)
for x in range(n):
    if (x+1) in lfib:
        print('+',end='')
    else:print('-',end='')

