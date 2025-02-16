s=set()
s1={x for x in range(10)}
print(s1)
s2 ={x**2 for x in range(5)}
print(s2)
s3 ={x**2 for x in[-2,-1,0,1,2]}
print(s3)
s4={x for x in (10,5,7,8,12,3) if x%2==0}
print(s4)
s5={x.upper() for x in 'philippines'}
print(s5)
s={1,12.5,'hello',('tuple'),1,2,3}
print(s)