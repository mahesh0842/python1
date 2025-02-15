l1=['a','b','c','d','e','a','c','e']
result=[]
for item in l1:
    if item not in result:
        result.append(item)
        count=l1.count(item)
        result.append(count)
print(result)