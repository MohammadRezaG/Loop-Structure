def gcd(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 
def lcm(a , b):
    return a * b / gcd(a , b)
n=int(input())
answer = 1
for i in range(1,n):
    if gcd(i , n) == 1 :
        answer = lcm(answer , i)
print(int(answer))