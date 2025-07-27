class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.width = b
    
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Cuboid(Rectangle):
    def __init__(self,l,b,h):
        self.height=h
        #if we write init method in child class then super keyword required
        super().__init__(l,b)
    def volume(self):
        return self.length*self.height*self.height
    
c = Cuboid(3,10,5)
print(c.volume())