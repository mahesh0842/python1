#class variable and class method
class Rectangel:
    count = 0
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
        #calling clas variable using class name 
        Rectangel.count += 1 
# if we using class variable we we want to create decorator
    @classmethod
    def get_count(cls):
        return cls.count
    

r1=Rectangel(15,3)
r2=Rectangel(13,2)
# Accesss using object name 
print(r1.count)
print(Rectangel.get_count())
print("Using instance or object to call ",r1.get_count())
