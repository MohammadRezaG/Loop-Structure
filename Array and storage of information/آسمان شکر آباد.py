r,c=map(int, input().split())
counter=0
for x in range(r):
    sky=input().split()
    counter += sky.count("*")
print(counter)