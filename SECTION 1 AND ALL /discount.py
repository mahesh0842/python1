amount = int (input("Enter amount: "))
if amount <= 1000:
    discount = amount * 10/100
elif amount > 1001 and amount <= 5000:
    discount = amount * 20/100
elif amount > 5001 and amount <= 10000:
    discount = amount * 30/100
else :
    discount = amount * 40/100
discounted_amount = amount - discount
print (" After discount  amount is: ", discounted_amount)
 

