"""index error
value error or type error 
key error
zerodivison error"""
#l=[10,20,30,40,50]
#Index=int(input('enter index'))
#print(l[Index])

"""value error"""
#val=int('abc')
#print(val,type(val))
"""type error"""
#a=10
#s='number'
#print(s+a)

'''line 15, in <module>
print(s+a)
TypeError: can only concatenate str (not "int") to str'''
#key error
'''d={1:'a',2:'b',3:'c'}
key = int(input('enter a key'))
print(d[key])'''

#zero division error
a=int(input("enter first number"))
b=int(input("enter second number"))
res=a//b
print(res)