gmail=input("Enter your gmail address :")
atrate =gmail.find('@')
print(atrate)
userid=gmail[:atrate]
domain = gmail[atrate:]
print(userid)
print(domain)
