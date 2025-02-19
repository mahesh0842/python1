#MIXED POSITINAL OR KEYWORD ARGUMENT
def add1(a,b,c,d,e):
    print(a,b,c,d,e)
    return a+b+c+d+e
r = add1(2,3,4,5,3)
print(r)

def add2(a,b,/,c,d,e):
    print(a,b,c,d,e)
    return a+b+c+d+e
r = add2(2,3,e=4,d=5,c=3)
print(r)

def add3(a,b,/,c,d,*,e):
    print(a,b,c,d,e)
    return a+b+c+d+e
r = add3(22,3,4,11,e=3)
print(r)