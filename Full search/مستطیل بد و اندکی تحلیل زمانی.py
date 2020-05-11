#1. answer <- 0
#2. for a:1 to [n/3] do
#3.     answer <- answer + [(n-3*a)/2] - max(0 , [n/2]-2a+1) +‌ 1
n=int(input())
answer=0
for a in range(1,(n//3)+1):
    answer = answer + ((n-(3*a))//2) - max(0 , (n//2)-(2*a)+1) +  1
print(answer)
i=input()
print(round(1))