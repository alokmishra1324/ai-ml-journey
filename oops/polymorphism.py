##Methos overiding

class Animal:
    def speak(self):
        return "Sound of the animal"
    
##Derive class

class Dog(Animal):
    def speak(self):
        return "woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())

## Function that demostrates polymorphism

def animal_speak(animal):
    print(animal.speak())

animal_speak(dog)


## Polymorphism with Functions and Methods

class Shape:
    def area(self):
        return "The area of the figure"
    
class Rectangle(Shape):
    def __init__(self , width , height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius* self.radius
    
## Function that demonstrtate polymorphism

def print_area(shape):
    print(f"The area is {shape.area()}")

rectangle = Rectangle(4,5)
circle = Circle(3)

print_area(rectangle)
print_area(circle)


## Polymorphism with Abstract base class

from abc import ABC , abstractmethod

##Define an abstract class

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"
    

# Function that demonstrates polymorphism
def start_vehicle(vehicle):
    print(vehicle.start_engine())

## create objects of car and motorcycle

car = Car()
motorcycle = Motorcycle() 
start_vehicle(car)