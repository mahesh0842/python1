pass1=input('enter a password')
pass2=input('Enter password again')
if pass1==pass2:
    print("password match successfully")
else:
    if pass1.casefold()== pass2.casefold():
        print("Passwor cases doesnt match")
    else:
        ("password doesnt match pls try again")
