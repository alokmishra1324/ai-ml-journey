##Encapsulation with Getter and Setter Methods
## Public Protected and Private

# class Person:
#     def __init__(self , name , age):
#         self.name = name  ## public variables
#         self.age = age

# def get_name(person):
#     return person.name

# person = Person("Alok" , 25)

# print(person.name)

# # print(dir(person))

# get_name(person)


# class Person:
#     def __init__(self , name , age , gender):
#         self.__name = name  ## Private variables
#         self.__age =  age    ## Private variables
#         self.gender = gender

# # person = Person("Alok" , 25 , "Male")
# # print(dir(person))


# def get_name(person):
#     return person.__name


# person = Person("Alok" , 25 , "Male")
# get_name(person)




# class Person:
#     def __init__(self , name , age , gender):
#         self._name = name  ## Protected variables
#         self._age =  age    ## Protected variables
#         self.gender = gender

# # person = Person("Alok" , 25 , "Male")
# # print(dir(person))
# class Employee(Person):
#     def __init__(self , name , age , gender):
#         super().__init__(name ,age , gender)

# employee= Employee("Alok" , 25 , "Male")
# print(employee._name)



##Encapsulation with Getter and Setter Methods

class Person:
    def __init__(self , name , age):
        self.__name= name  ## Private
        self.__age = age
    
    ##getter method 
    def get_name(self):
        return self.__name
    ##setter method
    def set_name(self ,name):
        self.__name = name

    def get_age(self):
        return self.__age
    
    def set_age(self , age):
        if age > 0:
            self.__age = age
        else:
            print("Age cannot be negative") 


person = Person("Alok" , 25)

## Access and modify private variables using using getter and setter
print(person.get_name())
print(person.get_age())

person.set_age(35)
print(person.get_age())

person.set_age(-5)