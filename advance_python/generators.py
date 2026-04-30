# def square(n):
#     for i in range(3):
#         return i**2
    
# print(square(3))

def square(n):
    for i in range(3):
        yield i**2

print(square(3))

for i in square(3):
    print(i)


a = square(3)
print(a)

print(next(a))
print(next(a))
print(next(a))
# print(next(a))

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))

for val in gen:
    print(val)


##Practicle : Reading large files

def read_large_file(file_path) :
    with open(file_path , 'r') as file:
        for line in file:
            yield line

file_path = 'large_file.txt'

for line in read_large_file(file_path):
    print(line.strip())


def count_up_to(n):
    count =1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)

## Generator expression - creates a generator
gen_exp = (x*x for x in range(5))
print(gen)
print(list(gen_exp))

def fibonacci():
    a , b = 0, 1
    while True:
        yield a 
        a, b = b , a+b

gen = fibonacci()
for _ in range(100):
    print(next(gen))

## The send() method allows you to send a value to the generator:
def echo_gen():
    while True:
        received = yield
        print("Received:" , received)

gen =  echo_gen()
next(gen)

gen.send("Hello")
gen.send("World!")
gen.send(28)
gen.send(29.67)
gen.send(True)

def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()
print(next(gen))