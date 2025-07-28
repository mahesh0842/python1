class Duck:
    def talk(self):
        print(" Duck talk")
    def walk(self):
        print("Duck walk")


class Dog:
    def talk(self):
        print(" dog talk")



def person(pet):
        pet.talk()
        if hasattr(pet, "walk"):
            pet.walk()

dog = Dog()
person(dog)