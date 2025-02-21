def pascal(n):
    r=[1]
    for i in range(n):
        print(r)
        temp1=[0]+r
        r=r+[0]
        new_row=[x+y for x,y in zip(r,temp1)]
        r=new_row
pascal(60)