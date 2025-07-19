class Rectangle:
    def __init__(self,l,b):
        print("ID OF SELF",id(self))
        self.length = l
        self.width = b
    
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
#creating objects of class Rectangle and passing values to the 
r = Rectangle(15,20)
print("ID of r1",id(r))
r2= Rectangle(10,5)
print("ID of r2",id(r2))
r3 = Rectangle(12,8)
print("ID of r3",id(r3))
#calling methods of class Rectangle
r.area()
r.perimeter()
r3.area()
r3.perimeter()
r2.area()
r2.perimeter()


print("Area of rectangle is  ",r.area()) 
print("Perimeter of rectangle is ", r.perimeter())
print("Length of rectangle is ", r.length)
print("Width of rectangle is ", r.width)
print("Area of rectangle is  ",r2.area()) 
print("Perimeter of rectangle is ", r2.perimeter())
print("Area of rectangle is  ",r3.area()) 
print("Perimeter of rectangle is ", r3.perimeter())


