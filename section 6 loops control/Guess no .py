import random
n = random.randint(1,10)
guess = 0
while guess != n:
    guess= int(input("enter the nuber"))
    if guess <n:
        print("its smaller")
    elif guess > n:
        print("Its larger")
    else:
        print("correct guess") 


