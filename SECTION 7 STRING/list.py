n= int(input("Enter the number"))
if n<=1:
    prime=True
else:
    prime=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
           prime=False
           break             
if prime:
    print("Prime")
else:
    print("Not Prime")