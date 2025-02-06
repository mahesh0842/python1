s='hello how are you'
print(s.find('how'))
print(s.find('k'))
print(s.find('o'))
print(s.find('o',5))
print(s.find('o',8,16))
print(s.rfind('o'))#its start from right to left
print(s.index('how'))
print("it comes how many times",s.rindex('l'))
print(s.count('o'))
s2= "python"
print(s2.ljust(20))
print(s2.rjust(20))
print(s2.center(10,'*'))
print(s2.center(20,'+'))
print(s2.rjust(10,'*'))
s3= "        alpha"
s4="......+Alpha"
print(s3.lstrip())
print(s3.rstrip())
print(s4.lstrip())
print(s4.rstrip())
print(s4.lstrip('. +'))
#output
'''
6
-1
4
7
15
15
6
it comes how many times 3
3
python              
              python
**python**
+++++++python+++++++
****python
alpha
        alpha
......+Alpha
......+Alpha
Alpha
'''
