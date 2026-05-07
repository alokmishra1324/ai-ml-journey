## Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_numbers(number):
    time.sleep(2)
    return f"Square: {number * number}"

numbers = [1,2,3,4,5,6,7,8,9,10]

if  __name__ == "__main__":
    t = time.time()
    with ProcessPoolExecutor(max_workers =3) as executor:
        results = executor.map(square_numbers , numbers)

    for res in results:
        print(res)

    finished_time  = time.time() -t
    print(finished_time)