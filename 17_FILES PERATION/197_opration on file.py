file = open('mk.txt','w')

#print(type(file))
#print(dir(file))
#print(file.name)
#print(file.mode)

"""lines=file.readlines()
print(lines,type(lines))
for line in lines:
    print(line,end='')
file.close()"""
 
list1=['\npython is simplae as like c and c++ \n','python is object oriented programming\nin python everyting is object that helps to writes programme']

file.writelines(list1)