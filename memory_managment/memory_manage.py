##Reference Counting 

import sys

a = []
## 1 (one reference from 'a' and one from getrefcount())
print(sys.getrefcount(a))

b = a
print(sys.getrefcount(b))

del b
print(sys.getrefcount(a))

## Garbage Collection
import gc

##enable garbage collection

gc.enable()

# gc.disable()

# gc.collect()

## Get garbage collection stats

# print(gc.get_stats())

## get unreachable objects
print(gc.garbage)


import gc

class MyObject:
    def __init__(self , name):
        self.name = name
        print(f"Object {self.name} created")

    def __del__(self):
        print(f"Object {self.name} deleted")

#create circular ref
obj1 = MyObject("obj1")
obj2 = MyObject("obj2")
obj1.ref = obj2
obj2.ref = obj1

del obj1
del obj2

## Manually trigger the garbage collection
# print(gc.collect())


##Generators for memory efficiency

def generate_numbers(n):
    for i in range(n):
        yield i

## using the generator
for num in generate_numbers(100000):
    print(num)
    if num>10:
        break


## Profiling memory usage with tracemalloc

import tracemalloc

def create_list():
    return [i for i in range(10000)]

def main():
    tracemalloc.start()

    create_list()

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print("[ Top 10 ]")
    for stat in top_stats[:10]:
        print(stat)

main()