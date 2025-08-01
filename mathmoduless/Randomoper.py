import random
r=random.random()
print(r)
r1=random.randint(1,100)
print(r1)
r2=random.choice([1,2,3,4,5])
print(r2)
r3=random.sample([1,2,3,4,5], 3)
print(r3)
r4=random.shuffle([1,2,3,4,5]) # Note: shuffle modifies the list in place and returns None
print(r4)