## Define a recursive function to calculate the nth Fibonacci number using memoization. Test the function with different inputs.
def factorial(n, memo = None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    memo[n] =  n * factorial(n-1, memo)

    return memo[n]

print(factorial(9))

## Define a function that takes two arguments, a and b, where b is a dictionary with a default value 
## of an empty dictionary. The function should add a new key-value pair to the dictionary and return it. Test the function with different inputs.

def funcdict(a,b={}):
    b[a] = len(b) +1
    return b

print(funcdict("m"))
print(funcdict("n"))
print(funcdict("o"))

## Problem:The dictionary keeps growing across function calls, even though you didn’t pass it
## Why This Happens
## Default arguments are evaluated only once
## So b={} is created once and reused every time

def funcdict1(a, b=None):
    if b is None:
        b= {}
    b[a] = len(b)+1
    return b

print(funcdict1("x"))
print(funcdict1("y"))
print(funcdict1("z"))


## Define a function that takes a variable number of keyword arguments and returns a dictionary containing only those key-value pairs where the value is an integer. Test the function with different inputs.
def filter_integers(**kwargs):
    result = {}
    for key , values in kwargs.items():
        if isinstance(values , int):
            result[key] = values
    return result

## one liner
# def filter_integers(**kwargs):
#     return {k:v for k,v in kwargs.items() if isinstance(v, int)}
   

print(filter_integers(a=1, b=2.5, c="hello", d=4))

 
##Define a function that takes another function as a callback and a list of integers. The function should apply the callback to each integer in the list and return a new list with the results. Test with different callback functions.
def funcwithcallback(callback , list1):
    result = []

    for i in list1:
        result.append(callback(i))
    return result

def square(x):
    return x**2

print(funcwithcallback(square , [1,2,3]))

## Define a function that returns another function. The returned function should take an integer and return its square. Test the returned function with different inputs.

def return_func():
    def square(x):
        return x**2
    return square

square_func = return_func()
print(square_func(12))

## Define a function that calculates the time taken to execute another function. Apply this decorator to a function that performs a complex calculation. Test the decorated function with different inputs.
import time 
def time_func(func):
    def wrapper(*args ,**kwargs):
        start_time = time.time()
        result = func(*args , **kwargs)
        end_time = time.time()

        print(f"Execution in {end_time - start_time:.6f}")

        return result
    return wrapper

@time_func
def complex_cal(n):
    total = 0
    for i in range(n):
        total += i*i
    return total


print(complex_cal(10000))


##Define a higher-order function that takes two functions, a filter function and a map function, along with a list of integers. The higher-order function should first filter the integers using the filter function and then apply the map function to the filtered integers. Test with different filter and map functions.

def filter_map_function(filter_func , map_func , numbers):
    filtered = []
    for num in numbers:
        if filter_func(num):
            filtered.append(num)
    
    result =[]

    for num in filtered:
        if map_func(num):
            result.append(map_func(num))
    return result

def is_even(x):
    return x%2==0

def square1(x):
    return x**2

print(filter_map_function(is_even , square1 , [1,2,3,4,5,6]))

##Define a function that composes two functions, f and g, such that the result is f(g(x)). Test with different functions f and g.
def compose_func(f , g):
    def result(x):
        return f(g(x))
    return result


def increment(x):
    return x+1

composed = compose_func(increment , square1)
print(composed(9))


## Use the functools.partial function to create a new function that multiplies its input by 2. Test the new function with different inputs.
from functools import partial

def multiply(x,y):
    return x*y

double = partial(multiply , 2)

print(double(5))


def power(a , b):
    return a**b

pow2 = partial(power , b=2)
pow4 = partial(power , b=4)

print(power(2, 3))
print(pow2(3))
print(pow4(2))
print(pow2.func)
print(pow4.args)
print(pow4.keywords)

## Define a function that takes a list of integers and returns their average. The function should handle any errors that occur (e.g., empty list) and return None in such cases. Test with different inputs.

def avg(numbers):
    try:
        avg = 0
        if len(numbers)==0:
            raise ValueError("Empty List")
        tsum = sum(numbers)
        avg = tsum / (len(numbers))
        return avg
    except Exception as e:
        return None



num1 = [1,3,4,5,6,7]
print(avg(num1))