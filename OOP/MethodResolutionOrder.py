class Parent:
    def show(self):
        print("Parent method called")


class Child(Parent):
    def show(self):
        print("Child method called")


c = Child()
c.show()
print(Child.mro())