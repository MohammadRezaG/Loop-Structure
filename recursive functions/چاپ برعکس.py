def f():
    a=int(input())
    if not a==0:
        f()
        print(a)
f()
