import math

a = 12
b = 6
c = 1

discriminant = b**2 - 4*a*c

if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Roots of the equation are:", root1, root2)
else:
    print("The equation has no real roots")
