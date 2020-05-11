#01. if r-l = 1 then
#02.     if a[l] = x then
#03.         return 1
#04.     else then
#05.         return 0
#06. mid <- (r + l) / 2
#07. if x < a[mid] then
#08.     return find(l , mid , x)
#09. else then
#10.     return find(mid , r , x)
n,q=map(int,input().split())
a=list(map(int,input().split()))
for chr in range(q):
    t,x=input().split()
    x= int(x)
    r=len(a)
    l=0
    bo=False
    while r - l >1:
        mid = (l+r)//2
        if a[mid] == x:
            bo=True
            break
        elif x < a[mid]:
            r = mid
        else:l = mid
        if a[l] == x:
            bo=True
            break
    print(int(bo))