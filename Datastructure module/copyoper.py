import copy
l1 = [1, 2, 3, 4, 5]
l2 = copy.copy(l1)
print(l1)
print(l2)
print(id(l1))
print(id(l2))
l3 = copy.deepcopy(l1)
print(l3)
print(id(l3))
l4=["a", "b", "c"]
deep= copy.deepcopy(l4)
for i in l4:
    print(i," ",id(i))

for i in deep:
    print(i," deep copy",id(i))