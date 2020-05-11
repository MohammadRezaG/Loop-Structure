def function(a):
    if a==0:
        return 5
    elif a%2==0:
        return (function(a-1)-21)
    else:
        return function(a-1)*function(a-1)
a=int(input())
print(function(a))
