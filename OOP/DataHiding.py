#hiding data public private and p[rotected]
#name mangling use to acces private data
#                       public  private  protected 
# inside class          Y           Y       Y
#Child class            Y           Y       N
#using object           Y           Y       N
class Person:
    def __init__(self):
        self.name = "Mahesh"         # public variable
        self._email = "mahesh@gmail.com"  # protected variable
        self.__password = "1234"     # private variable

    def show(self):
        print("Name:", self.name)        # ✅ allowed
        print("Email:", self._email)     # ✅ allowed
        print("Password:", self.__password)  # ✅ allowed (within class)

class Student(Person):
    def access(self):
        print("Name:", self.name)        # ✅ public, allowed
        print("Email:", self._email)     # ✅ protected, allowed in child class
        # print("Password:", self.__password)  ❌ Error (private, not accessible in child)

# 🧪 Now using object
obj = Student()

obj.show()          # ✅ calls method from parent class
obj.access()        # ✅ access public + protected from child class

print(obj.name)     # ✅ public - accessible
print(obj._email)   # ⚠️ technically accessible, but not recommended
# print(obj.__password)  ❌ Error - private variable can't access directly

# ✅ Accessing private using name mangling
print(obj._Person__password)  # ✅ this works (name mangling)