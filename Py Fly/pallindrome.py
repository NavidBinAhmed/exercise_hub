'''examples are from Krish Naik uDemy course on GenAI'''


# Polymorphism
class Animal:
    def speak(self):
        return "Sound of animal"
    

class Dog(Animal):
    def speak(self):
        return "Gheu"
    
class Cat(Animal):
    def speak(self):
        return "Meaw"    

# function demonstrating polymorphism
def animal_speak(animal):
    print(animal.speak())

# inherited to the child class from the base Animal class
dog = Dog()
print(dog.speak())

cat = Cat()
print(cat.speak())

print(Animal().speak())

animal_speak(cat)


# polymorphism with functions and methods
# base class

class Shape:
    def area(self):
        return "The area of the figure"
    
# derived class 1
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
# derived class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# function that demonstrates polymorphism
def print_area(shape):
    print(f"The area is {shape.area()} square units")

rectangle = Rectangle(4,5)
circle = Circle(3)

print_area(rectangle)
print_area(circle)


# Polymorphism with abstract base class
from abc import ABC, abstractmethod

# define an abstract class: complete empty class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# derived class 1
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
# derived class 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"
    

# function demostrating polumorphism
def start_vehicle(vehicle):
    print(vehicle.start_engine())

# create objects of car and motorcycle
car = Car()
motorcycle = Motorcycle()
start_vehicle(car)
start_vehicle(motorcycle)