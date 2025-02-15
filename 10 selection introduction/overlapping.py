l1=[10,12,14,16,2,4,5]
l2=[1,23,22,4,5,6,7,99]
l3=[]
for x in l1:
    if x in l2:
        l3.append(x)
print(l3)
