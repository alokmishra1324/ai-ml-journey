
'''
__init__ : Initializes a new instance of a class
__str__:Return a string represetation of an object
__repr__: Returns an official string representation of an object
__len__:Returns the length of an object
__getitem: Gets an item from a container
__setitem__: Sets an item in a container

'''

# class Person:
#     pass

# person =  Person()

# # print(dir(person))
# print(person)

## Basic magic methods
class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age}"
    def __repr__(self):
        return f"Person(name={self.name} , age={self.age})"
person = Person("Alok" , 25)
print(person)
print(repr(person))




