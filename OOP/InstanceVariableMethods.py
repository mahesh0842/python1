#instace variable and method takes self as keyword 
#variable  in init method used self keyword
#method use self keyword 
class Rectangel:
    def __init__(s,l,b):
        s.length=l
        s.breadth=b
    def area(s):
        return s.length*s.breadth
    def perimeter(s):
        return 2*(s.length+s.breadth)
    


r1=Rectangel(15,7)
r2=Rectangel(12,5)
print(r1.area(),r2.area())
    

