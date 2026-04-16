def function_name(parameters):
    """Docstring describing the function."""
    # Function body
    return result

def even_or_odd(num):
    """This functions finds even or odd"""
    if num%2==0 :
        print("The number is even")
    else:
        print("The number is odd")    


even_or_odd(11)


def add(a,b):
    return a+b

res = add(4, 6)
print(res)

def greet(name = "Guest"):
    print(f"Hello {name} Welcome to Python programming!")

greet("Alok")
greet() ## will use default value

## Variable length arguments
## Postional and keywords arguments

def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1,2,3,4,5 , "Hello")

##keywords arguments

def print_details(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} :{value}")

print_details(name="Alok" , age=25 , country="India")

def print_details(*args , **kwargs):
    for val in args:
        print(f"Positional arguments:{val}")
    for key , value in kwargs.items():
        print(f"{key} :{value}")

print_details(1,2,3 , name="Alok" , age=25)

##Return statement

def multiply(a,b):
    return a*b

result = multiply(87, 67)
print(result)

##Return multiple paramenters

def calculate(a,b):
    sum_result = a+b
    product_result = a*b
    return sum_result , product_result

result = calculate(5, 10)
print(result)