t1=('jack',38.6,45,5+9j,45)
print(t1)
print(type(t1))
t2=(1,2,3,4,5)
t3=(10,)
print(type(t3))
t4=tuple((1,2,3,4))
print('t4',type(t4))
t5=tuple('python')
l1=(t5)
print(t5)
print(l1)
#packing and unpacking
t6=10
print(type(t6))
#automatically packing as tuple
t7=10,20,30,40,50
print("PACKING",type(t7))
#UN-PACKING
a,b,c,d,e=t7
print("UN-PACKING",a)
print("UN-PACKING",b)
print("UN-PACKING",c)
print("UN-PACKING",d)
print("UN-PACKING",e)
