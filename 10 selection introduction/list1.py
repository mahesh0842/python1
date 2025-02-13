#index operator
list1=[1,2,3,4,5,55,7]
print(list1)
print(list1[-5])
x=list1[3]
list1[4]=88#modified the list
print(x)
print(list1)
#slicing of list
print(list1[2:5])
print(list1[0:8:2],'START,END,STEP')
print(list1[1:-1],'reverse list printing')
print(list1[-1:-3:-1],'rev')
for i in list1:
    print('loop',i)
for item in range(len(list1)-1,-1,-1):
    print(list1[item])