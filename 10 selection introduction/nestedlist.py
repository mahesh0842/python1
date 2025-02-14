l1=[['john','smith','ajay'],[1,2,3],['john','ajay','smith']]
print(l1)
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
c=[]
for i in range(len(a)):
    sum=[]
    for j in range(len(a[0])):
        sum.append(a[i][j]*b[i][j])
    c.append(sum)
print(c)
