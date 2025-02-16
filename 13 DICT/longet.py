dict1={'long':'abc',
       'short':'ab',
       'verylong':'abcdef'}
keys=list(dict1.keys())

values=list(dict1.values())

len=[len(x) for x in values]

print(keys)
print(values)
print(len)

max_len=max(len)
min_len=min(len)

max_index=len.index(max_len)
min_index=len.index(min_len)

print('max',keys[max_index],values[max_index])
print('min',keys[min_index],values[min_index])
