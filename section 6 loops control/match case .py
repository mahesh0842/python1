# match case in python is like switch case in other laungauge
'''day = int(input("Enter day number"))
if day ==1:
    print("sunnday")
elif day ==2:
    print("Monday")
elif day ==3:
    print("Tuesday")
elif day ==4:
    print("Wednesday")
elif day ==5:
    print("Thursday")
elif day ==6:
    print("Friday")
elif day==7:
    print("saturday")
else:
    print("holiday")'''
day = int (input("Enter day number"))
match day: # we can take any input from here like list tuple stri ng also
    case 1:
        print("sunday")
    case 2:
        print("monday")
    case 3:
        print('Tuesday')
    case 4:
        print('Wednesday')
    case 5:
        print('Thirsday')
    case 6:
        print('Friday')
    case 7:
        print('Saturday')
    case _:
        print("Holiday")
    