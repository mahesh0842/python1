L=[10,20,30,40,50]
try:  
    index=int(input("enter a index"))
    print(L[index])
    print('end of try block')
except:
    print('invalid index')
    print("terminated gracefully")