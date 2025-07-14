l=[10,20,30,40,50]
try:
    index=9
    print(l[index])
except IndexError:
    print('Invalid Index')
except TypeError:
    print("index should be integer")
except TypeError as msg:
    print(msg)
except:
    print("some error")
#or

print("end of programme")

