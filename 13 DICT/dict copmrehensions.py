dict2=dict(((1,2),(2,4),(5,6)))
print(dict2)
dict1={101:'john',102:'smith',103:"ajay"}
dict1[104]='david'
print(dict1)
dict1[101]='mark'
print(dict1)
del dict1[104]
print(dict1)
for i in dict1:
    print(i,dict1[i])