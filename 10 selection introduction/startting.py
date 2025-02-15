food=['pzza','buger','noodels','nuggets']
letter=input("Enter a letter")
for x in food:
    if x.startswith(letter):
        print(x)