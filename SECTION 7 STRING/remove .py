#remove puctuation from string
Str1=input("Enter the string")
newstr=''
punct='''!()-[]{}.;:\<>./?@#$%^&*~'''
for x in Str1:
    if x not in punct:
        newstr=newstr+x
print(newstr)