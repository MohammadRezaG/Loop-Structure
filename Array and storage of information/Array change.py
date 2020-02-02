C=int(input())
l=[]
for x in range(C):
    i=input().split()
    if i[0]=='+':
        l.insert((int(i[1])-1),int(i[2]))
    else :
        del l[(int(i[1])-1)]
    if len(l)==0:
        print("EMPTY")
    else :
         for j in l:
            print (j,end=" ")
    print ()