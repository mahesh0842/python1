class Outer:
    def __init__(self):
        #creating an object of inner class
        self.in_obj= self.Inner()


    def show(self):
        self.in_obj.display()


    class Inner:

        def __init__(self):
            self.idata='Inner Data'
        def display(self):
            print(self.idata)


o=Outer()
o.show()