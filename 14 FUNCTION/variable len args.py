"""def fun1(*args):
    print(type(args),args)

fun1()
fun1(10,11)
fun1(10,20,30,40,50)
fun1(10,'hello',22.5,True)"""



def fun2(a,b,*args):
    print(type(args),args)

#fun2()

fun2(10,20,30,40,50)
