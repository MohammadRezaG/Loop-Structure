i=int(input())
counter=0
for x in range(i):
    i2=input()
    if counter < len(set(i2)) :
        counter = len(set(i2))
print(counter)