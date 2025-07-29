#importing Abstarct Method

from abc import ABC, abstractmethod
class Parent(ABC):
    def meth1(self):
        print("Parent method called")

#Using abstract method to creating abstract method only passes the reference

    @abstractmethod
    def meth2(self):
        pass


class Child(Parent):
    def meth3( self):
        print("Child method called")

#oveeride the abstract method in child class

    def meth2(self):
        print("Child  imported method called")

c = Child()

c.meth2()