dict1={101:'john',102:'smith',103:'ajay'}
for x in dict1:
    print(x,dict1[x],)
print('new')
#or
for x in dict1:
    print(x,dict1.get(x))
print('new')
print(dict1.keys())
print('new')
print(dict1.values())
print('new')
print(dict1.items())
#or
for k in dict1.keys():
    print(k)
for(x,y) in dict1.items():
    print(x,y)