class NegaiveAgeException(Exception):
    pass
def stage(age):
    if age < 0:
        raise NegaiveAgeException('age shold not be negative')
    elif age>=0 and age<13:
        print('kid')
    elif age >=13 and age < 20:
        print("tenn")
    elif age >= 20 and age <=50:
        print("young")
    else:
        print("old")

age = int(input("enter your age"))
try:
    stage(age)
except NegaiveAgeException as e:
    print(e)