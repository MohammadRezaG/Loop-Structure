NUM = []
while True :
    i=int(input())
    if (i==0):
        break
    NUM.append(i)
for x in NUM:
    for y in range(x):
        print(x)