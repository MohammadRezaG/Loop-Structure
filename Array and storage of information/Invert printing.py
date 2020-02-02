NUM = []
while True :
    i=int(input())
    if (i==0):
        break
    NUM.append(i)
for x in range((len(NUM))-1,-1,-1):
    print(NUM[x])
