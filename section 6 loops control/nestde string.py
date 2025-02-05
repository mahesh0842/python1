#print prime number from 1-100
for n in range(1,100+1):
    n=0
    count = 0
for i in range (1,n+1):
    if n%i==0:
        count+=1
if count ==2:
    print(n)


