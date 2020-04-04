t,w=map(int, input().split())
towel=["0" for x in range(t+1)]
worker=["0" for x in range(w+1)]
while True:
    il=input().split()
    if "['put', 'an', 'end', 'to', 'my', 'misery']"== str(il):
        break
    elif int(worker[int(il[0])])==0 and il[1]!="track":
        print("no towel has been assigned to me.")
    elif il[1]=="track":
        worker[int(il[0])]=int(il[2])
    elif il[1]=="dry":
        if int(worker[int(il[0])])>0:
            towel[worker[int(il[0])]]=str(int(towel[worker[int(il[0])]])-int(il[2]))
            if int(towel[worker[int(il[0])]])<0:
                towel[worker[int(il[0])]]="0"
    elif il[1]=="give":
        if int(towel[worker[int(il[0])]])>0:
            print("impossible")
        else:
            towel[worker[int(il[0])]]="10"
            print("ok")
            worker[int(il[0])]="0"
        #worker[int(il[0])]="0"
    elif il[1]=="output":
       print(towel[worker[int(il[0])]])