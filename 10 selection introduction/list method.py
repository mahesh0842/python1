l1=[1,2,3,4666,8,88]
print(len(l1))
l1.append(111)
print(l1)
print(id(l1))#print address of list
print(len(l1))
l1.extend([1,11,23,43])
print(l1,'extend')
l1.insert(-5,1000)
print(l1,'INSERT AT INDEX -5')
print(id(l1))#print address of list
#copy method like cloning
l2=l1.copy()
print(l2)
print(id(l2))