l1=[]
for i in range(10):
    l1.append(i)
print(l1)
#or
l2=[i for i in range(12)]
print(l2)
#or
l3=[x**2 for x in range(1,8)]
print(l3)
#or
l4=[x for x in (10,12,13,15,16)if x%2==0]
print(l4)
#0r
l5=[x.lower() for x in 'pytHon']
print(l5)
#or
l6=[x for x in 'abc%412345de@fgh' if x.isalpha()]
print(l6)
ata=input("enter the input")
l7=ata.split()
print(l7)