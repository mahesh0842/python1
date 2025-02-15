l1=[[1,2,3,4],[5,6,7,8],[7,8,9,0]]
l2=[]
for i in range(4):
    s=[]
    for j in range(3):
        s.append(l1[j][i])
    l2.append(s)
print(l2)