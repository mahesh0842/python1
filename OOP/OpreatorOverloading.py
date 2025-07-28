# Python program to overload
# a comparison operators

class A:
    def __init__(self, a):
        self.a = a
    def __gt__(self, other):
        if(self.a>other.a):
            return True
        else:
            return False
ob1 = A(2)
ob2 = A(3)
if(ob1>ob2):
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")




class Vector:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)
    def __str__(self):
        return f"({self.x},{self.y})"
v1 = Vector(1,2)
v2 = Vector(3,4)
print("Vector Sum :",v1 + v2)
