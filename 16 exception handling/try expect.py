l=[1,2,30,40,50,60]
try:
    index = int(input("enter index"))
    print(l[index])
    print('end try block')
except (IndexError,ValueError) as msg:
    print('invalid index',msg)