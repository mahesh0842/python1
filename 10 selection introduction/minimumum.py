l1=['pizza','nuggets','pasta','noodels','burger','hotdog']
l2=['burger','hotdog','noodels','pasta','nuggets','pizza']
index1=10
index2=10
for i in range(len(l1)):
    indx=l2.index(l1[i])
    if i+indx< index1+index2:
        index1=i
        index2=indx
print(l1[index1],index1+index2)

