class Parent:
    def show(self):
        print("Parent show")


class Child(Parent):
    def show(self):
        # the redefined function of parent class in child class is called MO using super keyword
        super().show()
        print("Child show")

c=Child()
c.show()