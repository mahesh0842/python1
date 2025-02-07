Str1=input("Enter the string")
lower=''
upeer =''
for x in Str1:
    if x.islower():
        lower+=x
    else:
        upeer+=x
str2= lower+upeer
print(str2)