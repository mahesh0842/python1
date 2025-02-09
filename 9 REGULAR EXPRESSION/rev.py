
mytext=input("Ether the digit")
len1=len(mytext)
s=''
for i in range(len1-1,-1,-1):
    s=s+mytext[i]
    
print(s)
s=mytext[::-1]
print(s)