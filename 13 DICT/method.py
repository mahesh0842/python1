dict1={1:'jphn',2:'smith',3:'ajay'}
#copy
dict2=dict1.copy()
dict3={105:'mk',106:'kk'}
print(dict2)
dict2[2]='mark'
print(id(dict1[2]))
print(id(dict2[2]))
#update
dict1.update(dict3)
print(dict1)
#set default
print(dict1.setdefault(105))
print(dict1.setdefault(109))
#formkeys
dict1.pop(1)
print(dict1)
dict1.pop(108,None)
print('k ==',dict1)




