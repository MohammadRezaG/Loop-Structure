n,l = map(int, input().split()) 
c=0
for x in range(n):
    d,r,g = map(int, input().split())
    d=d+c
    while True:
        if d<=r:
            c=c+(r-d)
            break
        else:
            d=d-r
        if d>=g:
            d=d-g
        else:
            break
print(l+c)

