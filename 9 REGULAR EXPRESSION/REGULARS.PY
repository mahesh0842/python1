words = 'narayan'
l = len(words)
for i in range(0, l):
    count = 1
    for j in range(i + 1, l):

        if words[i] == words[j]:
            count += 1
            print(f"Duplicate character '{words[i]}' found at indices {i} and {j}")
            print(f"Duplicate character '{words[i]}' found {count} times")
print('HELLO')
print('heloo')















































































