s='abc1234'
print(s.isalnum())
print(s.isalpha())
print(s.isascii())
s1='/u03b1\u03b2\u03b3' 
print(s1)
print(s1.isalnum())
s2='\n'
print(s.isprintable(),"==")
s3='123'
print(s3.isdecimal())
print(s3.isdigit())
s4='8\u00b2'
print=(s4.isdecimal())