 ## Function copy , Closures and Decorators

## Function copy

def welcome():
    return "Welcome to the advance python"

print(welcome())

wel = welcome
print(wel())

del welcome

print(wel())


## closures

# def main_welcome(msg):
#     # msg ="Welcome"
#     def sub_welcome_method():
#         print("Welcome to the advance python course")
#         print(msg)
#         print("Please learn these concepts properly")
#     return sub_welcome_method()

# # main_welcome()
# main_welcome("Welcome everyone")


def main_welcome(func):
    def sub_welcome_method():
        print("Welcome to the advance python course")
        func("Hello everyone")
        print("Please learn these concepts properly")
    return sub_welcome_method()

main_welcome(print)

def main_welcome2(func , lst):
    def sub_welcome_method():
        print("Welcome to the advance python course")
        print(func(lst))
        print("Please learn these concepts properly")
    return sub_welcome_method()

main_welcome2(len, [1,2,3,4,5,6])


## Decorators

def main_welcome3(func):
    def sub_welcome_method():
        print("Welcome to the advance python course")
        func()
        print("Please learn these concepts properly")
    return sub_welcome_method()

# def course_intro():
#     print("This is an python course ")

# course_intro()

# main_welcome3(course_intro)

@main_welcome3
def course_intro():
    print("This is adv python course ")


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper

@my_decorator
def say_hello():
    print("Helloo!!")

say_hello()

## Decorators with arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args , **kwargs):
            for _ in range(n):
                func(*args , **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi")

say_hi()



def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def addgreeting(func):
  def myinner2():
    return "Hello " + func() + " Have a good day!"
  return myinner2

@changecase
@addgreeting
def myfunc():
    return "Alok"

print(myfunc())

print(myfunc.__name__)

