def add(a,b):
    if b!=0:
        c=a//b
        return c
    else:
        raise ZeroDivisionError
try:
    res = add(10,0 )
    print(res)
except:
    print("division by zero")

