def decorator(fun):
    def wrapper(msg):
        print('do something in wrapper')
        fun(msg)
        print('hello')
    return wrapper

@decorator
def my_fun(msg):
    print(msg)


#d= decorator(my_fun)
#d('decorator')
my_fun('welcome')