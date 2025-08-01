l=["mk","ab","abhi","maj","abhi","mk"]
from collections import Counter
c=Counter(l)
print(c)
c.update({"ajay":4})
print(c)
for i in c.elements():
    print(i)
c.pop("abhi")
print(c)
c.most_common(2)
print("most common",c)