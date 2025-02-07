s1= 'decimalS'
s2 ='medical'
if len(s1)!=len(s2):
    print('Not anagram')
else:
    for x in s1:
        if x not in s2:
            print("not anaghram")
    else:
        print('anagram')
