#property methods
class Rectangle:
    def __init__(self,l,b):
       
        self.set_length(l)
        self.width = b


    def set_length(self,leng):
        #condition
        if leng>=0:
            self.length=leng
        else:
            self.length=1

    def get_length(self):
        return self.length



    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
r= Rectangle(15,8)
r.length=-9
print(r.get_length())
