#Writing static mthod
class Rectangle:
    def __init__(self,l,b):
       
        self.length = l
        self.width = b
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    #MAKES STATIC METHOD 
    @staticmethod
    def calc_area(length,breadth):
        return length*breadth
    
r1=Rectangle(15,8)
print(r1.area(),r1.perimeter())
#STATIC MTHOD CALLED USING CLASS NAME 
r2=Rectangle.calc_area(10,7)
print("STATIC METHOD = ",r2)
#STATIC METHOD CALLED WITHOUGHT CLASS NAME
print(r1.calc_area(11,7))
