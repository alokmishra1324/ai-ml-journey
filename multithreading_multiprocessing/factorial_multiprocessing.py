'''
Real-world Example: Multiprocessing for CPU bound Tasks
Scenario: Factorial Calculations
Factorial calculations, especially for large numbers,
involve significant computational work. Multiprocessing
can be used to distribute the workload across multiple CPU cores
improving performances

'''

import multiprocessing
import math
import sys
import time

#Increase the maximum number of digits for integr conversion
sys.set_int_max_str_digits(100000)

## function to compute factorial of a given number

def compute_factorial(number):
    print(f"Computing factorial of {{number}}")
    res = math.factorial(number)
    print(f"Factorial of {number} is {res}")
    return res

if __name__ == "__main__":
    numbers = [5000, 6000 , 700 , 8000]

    start_time = time.time()

    with multiprocessing.Pool() as pool:
        res = pool.map(compute_factorial, numbers)

    end_time = time.time()
    print(f"Results: {res}")
    print(f"Time Taken : {end_time - start_time} seconds")