# GLOBAL 
g=10
def fun1(a,b):
    c=a+b #local
    print('c',c)
    print(g)

def fun2(d):
    g=88
    print('fun2',d*g)

fun2(3)
fun1(4,5)
