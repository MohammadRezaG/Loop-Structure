i=input()
i2=input()
t=0
for x in range(len(i)):
    t=i.find(i2,x)
    if not t==-1 and x==t:
       print(t+1,end=" ")
      

       
def full_find(i,i2):
    t=0
    rl=[]
    for x in range(len(i)):
        t=i.find(i2,x)
        if not t==-1 and x==t:
            rl.append(t+1)
    return {'counter' : len(rl),'start_of_ferst_index' : rl}