l1=[x for x in range(10)]
print(l1)
t1=(x for x in range(10))
print(t1)
# tuples comphrsion work

t1=tuple(x for x in range(10))
print(t1)
#or
t1=(*(x for x in range(10)),)
print(t1)
t1=(*(x for x in  'pYThon'if x.islower()),)
print(t1)
