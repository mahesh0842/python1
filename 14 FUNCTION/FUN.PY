def add():
    result=a+b
    return result
a=5
b=6
add()
print(add())

#OR
def add1(a,b):
    result=a+b
    return result
print(add1(15,12))

#OR
result= add1(22,77)
print(result)
 #OR
def add2(a,b):
    print('INSIDE FUNCTION ADDRESS',id(a),id(b))
x,y= 4,8
print("outside function address",id(x),id(y))
add2(x,y)
print(add2(x,y))
