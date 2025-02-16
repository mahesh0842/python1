l1=['a','b','c']
for item in enumerate(l1):
    print(item)
dict1=dict(enumerate(l1))
print(dict1)
#advanced
dict2={x:x**2 for x in range(1,5)}
print(dict2)
# if we wnat use tuple
dict3=dict((x,x**2)for x in range (1,5,2))
print(dict3)
#0r
l1=[1,2,3]
l2=['aaaaaaa','b','xxxxxcxxxxxxxx']
for x,y in zip(l1,l2):
    print(x,y)
dict5 = dict((x,y)for x,y in zip(l1,l2))
print(dict5)
#or
dict6 = {x:y for x,y in zip(l1,l2)}
print('m',dict6)

#enumrate
for x,y in enumerate(l2):
    print('k',x,y)
dict7={x:y for x,y in enumerate(l2)}
print('b',dict7)
dict8=((x,y) for x,y in enumerate(l2))
print(dict8)
