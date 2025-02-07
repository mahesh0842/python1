#checkin stringis palidrone or not
str1 = input("Enter the string")
str2 = input("enter the second string")
rev1= str1[::-1]
rev2= str2[::-1]
if str1==rev1:
    print('its a plaindrone')
else:
    print('its not a palidrone') 
print(str2+rev2)