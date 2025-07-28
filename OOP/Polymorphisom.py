#poly = many morphism = form one name many form
#its support method overloading, method overriding, operator overloading, duck typing
a=1+2j
b=2+3j
print("operator overloading " ,a+b)

#the same function name action is different is called method overloading
l=[1,2,3,4,5,6]
print(len(l))
m=len({1,2,3,4,5,6})
print(m)
len("hello")
print(len("hello"))

def count(seq):
    s=0
    for x in seq:
        s=s+x
    return s
print(count([1, 2, 3, 4, 5, 6]))

