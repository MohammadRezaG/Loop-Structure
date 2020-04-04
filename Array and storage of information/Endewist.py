C=int(input())
l=[0 for x in range(200)]
for x in range(C):
    i=input().split()
    if i[0]=='+':
        l[(int(i[1])-1)]+=1
    else :
        print (l[(int(i[1])-1)])
