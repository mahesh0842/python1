class Car:
    def __init__(self, color, brand):
        # Properties (डेटा)
        self.color = color
        self.brand = brand

    # Methods (फंक्शन्स)
    def start_engine(self):
        print("Engine started broom broooom !")

# Object बनाना
my_car = Car("red", "Tata")
#obj name = class name for creating object

# Property एक्सेस करना
print(my_car.color)  # "red"

# Method को चलाना
my_car.start_engine()  # "Engine started!"