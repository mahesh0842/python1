

class Duck:
    def talk(self):
        print(" Duck talk")
    def walk(self):
        print("Duck walk")


class Dog:
    def talk(self):
        print(" dog talk")
    def walk(self):
        print(" dog walk")


    def person(pet):
        pet.talk()
        pet.walk()

dog = Dog()
dog.talk()
dog.walk()
duck = Duck()
duck.talk()
duck.walk()

"""class Duck:
    def talk(self):
        print(" Duck talk")
    def walk(self):
        print("Duck walk")


class Dog:
    def talk(self):
        print(" dog talk")
    

    def person(pet):
        pet.talk()
        #inbuilt function has attribute
        if hasattr(pet, "walk"):
            pet.walk()
        
dog = Dog()
person(dog)
        """