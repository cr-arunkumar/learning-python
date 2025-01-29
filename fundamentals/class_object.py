class Animal:
    # __init__ is a special method in Python classes. 
    # It is called when an object is created from the class.
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def sound(self):
        if self.sound=="cat":
            return "Meow!"
        elif self.sound=="dog":
            return "Woof!"
        else:
            return "Unknown sound."
    
    # This method is called when an object is printed.
    def __str__(self):
        return f"{self.name} makes {self.sound} sound."

my_animal=Animal("Lion", "Roar")   
print(my_animal.name)

# del my_animal.name
# print(my_animal.name) # Raises AttributeError: 'Animal' object has no attribute 'name'

print(my_animal)  # Calls __str__ method
print("----------------------------------------------------------------")

# Example of inheritance
class Cat(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color
    
    def __str__(self):
        return f"{self.name} is a {self.color} cat.it makse {self.sound} sound."
  
my_cat = Cat("Whiskers", "Meow", "Black")
print(my_cat)
my_dog = Animal("Buddy","Woof")
print(my_dog.sound)
print("----------------------------------------------------------------")


class Vehicle:

    def __init__(self):
        self.default_wheels = 4
        self.default_color = "White"
    def general_usage(self):
        print("general use: transporation")

class Car(Vehicle):
    def __init__(self):
        self.wheels =44
        super().__init__()  # This will call the parent's __init__() function.
        print(self.default_wheels, self.default_color)
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("specific use: driving")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm motor cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("specific use: road trip, racing")

c = Car()
m = MotorCycle()

print(issubclass(Car,Vehicle))
print(issubclass(Car,MotorCycle))


# The child's __init__() function overrides the inheritance of the parent's __init__() function.
