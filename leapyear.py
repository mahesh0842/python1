year = int(input("Ener a YEAR :"))
if year % 4 == 0 and  year % 100 ==0 and year % 400 ==0:
    print("Leap year")
else:
    print("Not a Leap year")