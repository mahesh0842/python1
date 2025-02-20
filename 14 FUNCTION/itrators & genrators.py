#ITRATOR
l=[1,2,3,4,5,6]
r=iter(l)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))


# GENRATOR
def days():
    l=['sun','mon','tue','wen','thu','fri','sat']
    i=0
    while True:
        x=l[i]
        i=(i+1)%7
        yield x

d=days()
print(next(d))
print(next(d))

print(next(d))

print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))




