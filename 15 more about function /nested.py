# function as objec
#nested function

'''def display():
    print("hello")
d=display()
d('joseph')'''

#nested function
'''def outer():
    def inner():
        print("inner")

    inner()
outer()'''

#function as parameter
'''def display():
    print("hello  display ")
def fun(d):
    d()
fun(display)'''

 
 #function returning a function

def add(x,y):
    print(x+y)
def sub(a,b):
    print(a-b)
def fun(f,x,y):
    f(x,y)
fun (add,10,17)
fun(sub,12,55)