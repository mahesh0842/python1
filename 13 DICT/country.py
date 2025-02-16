countries ={}
for i in range(5):
    name= input('enter country name ')
    if name[0].upper() not in countries:
        countries[name[0].upper()]=[name]
    else:
        countries[name[0].upper()].append(name)

print('output is ')
print(countries)
