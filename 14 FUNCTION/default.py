def add(a,b=0,c=0):
    return a+b+c

#print(add(1,2,3))
#print(add(a=2,b=5,c=10))

def additem(item,l=[]):
    l.append(item)
    return l


l=[1,2,3,4,5]
additem(15,l)
print(l)
#if we not passing list
print(additem(22)) 


