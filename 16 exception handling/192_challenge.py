class AccountBalenceEexception(Exception):
    pass


balence = 10000

def withdraw(amt):
    global balence

    if balence - amt <5000:
        raise AccountBalenceEexception("minimum balnce should be 5000")
    else:
        balance=balence-amt
        print("remining balnce is  : ",balance)
try:
    withdraw(6000)
except AccountBalenceEexception as e:
    print(e)