john = float(input("Enter john age : "))
smith = float(input("Enter smith age : "))
ajay = float(input("Enter ajay age : "))
if john > smith and john > ajay:
    print("john is older")
elif smith > ajay:
    print("smith is older")
else:
    print("ajay is older")
    
