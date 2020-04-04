def prime_number(num):
    # Python program to check if  
    # given number is prime or not 
    # If given number is greater than 1 
    if num == 2:
        return True
    elif (num > 1) and not ((num %2) == 0): 
       # Iterate from 2 to n / 2  
       for i in range(2, num//2): 
             
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
           if (num % i) == 0: 
               return False 
               
       else: 
        return True
      
    else: 
       return False
i=int(input())
r=0
for x in range(i):
    n=int(input())

    if prime_number(n):
        for x in range(n-1, 1, -1):
            if prime_number(x):
                r+=1
    else:
        for x in range(n-1, 1, -1):
            if n%x==0:
                if prime_number(x):
                    r+=1
d=0
if prime_number(r):
        for x in range(r-1, 1, -1):
            if prime_number(x):
                d+=1
else:
    for x in range(r-1, 1, -1):
        if r%x==0:
            if prime_number(x):
                d+=1
print(r-d)