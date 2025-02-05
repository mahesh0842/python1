rev = 0
n= int (input("Enter a number: "))
m = n
while n >0:
    r=n%10
    n=n//10
    rev=rev*10+r
if m == rev:
    print("The number is a palindrome")
else:       
    print("The number is not a palindrome")