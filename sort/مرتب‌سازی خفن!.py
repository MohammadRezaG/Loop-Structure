from functools import cmp_to_key
from math import trunc
def mrg_sort(object1,object2):
    if object1[1]>object2[1]:
       return 1
    elif object1[1]==object2[1]:
        if object1[2]>object2[2]:
            return 1
        elif object1[2]==object2[2]:
            return 0
        else : return -1
    else: return -1
mrg_s = cmp_to_key(mrg_sort)
n=int(input())
sl=[]
for x in range(n):
    name=input()
    m,*l=map(float,input().split())
    m=int(m)
    m=int(trunc(sum(l)//m))
    c,*l=input().split()
    sl.append((name,m,c))
sl.sort(key=mrg_s,reverse=True)
for x in sl:
    print(x[0])