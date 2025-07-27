class Rectangle:
    def __init__(self,l,b):
        print("ID OF SELF",id(self))
        self.length = l
        self.width = b
    
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    
r= Rectangle(15,5)
p1=r.area()
p2=r.perimeter()
print(p1,p2)
