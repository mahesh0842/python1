n = int(input("enter the no tht you want to check :"))
count = 0
for i in range(1,n+1):
    if n%i==0:
        count+=1 
if count ==2:
    print("its a prime")
else:
    print("its not a prime")

    