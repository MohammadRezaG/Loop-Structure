#FUNCTION >>> find(l , r , x)
#return '1' if x is equal to one of a[l], ..., a[r-1]
#and otherwise return '0'
#----------------------------------------------------
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
a=[]
def findl(l , r , x):
    if r-l == 1:
        if a[l] == x :
            return 1
        else :
            return 0
    mid=(r + l) // 2
    if a[mid] == x :
            return 1
    elif x < a[mid] :
        return findl(l , mid , x)
    else :
        return findl(mid , r , x)
n,q=map(int,input().split())
a=list(map(int,input().split()))
for chr in range(q):
    t,x=input().split()
    x= int(x)
    r=len(a)
    l=0
    print(int(findl(l , r, x)))
    