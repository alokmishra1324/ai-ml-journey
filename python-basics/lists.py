lst = [];
print(type(lst))

mixed_lst = [1,2, "Alok" , "Mishra" , 3.155 , True]
print(mixed_lst)

print(mixed_lst[3])
print(mixed_lst[-1])
print(mixed_lst[2:])
print(mixed_lst[0:3])

## Modifiying the lst
fruits = ["apple" , "guava" , "cherry" , "mangoes" , "strawberry"]

fruits[1] = "watermelon"
fruits.append("orange")
fruits.insert(1 ,  "banana")
fruits.remove("orange")
popped_fruit = fruits.pop()
print(popped_fruit)
index = fruits.index("cherry")
print(index)
print(fruits)
fruits.insert(2, "banana")
print(fruits)
print(fruits.count("banana"))
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
# fruits.clear()
print(fruits)
# fruits[1:] = "apple"
# print(fruits)

##slicing list
numbers = [1,2, 3, 4, 5, 6, 7, 8, 9,10]
print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])
print(numbers[::-2])

for fruit in fruits:
    print(fruit)

for index , number in enumerate(numbers):
    print(index , number)
    
lst = []

for x in range(10):
    lst.append(x**2)
    
lst1 = []    
for i in range(10):
    if(i%2 == 0):
        lst1.append(i)
    
print(lst1)    

##lsit comprehension

# Basic Syntax - [expression for item in iterable]
# with condition - [expression for item in iterable if condition]
## Nested lsit comprehension
# [expression for item in iterable for item in iterable]
square = [x**2 for x in range(10)]
print(square)
even_num = [num for num in range(10) if num%2==0]
print(even_num)

lst1 = [1, 2, 3, 4]
lst2 = ["a" , "b" , "c" , "d"]

print([[i , j] for i in lst1 for j in lst2])

# list comprehension with function calls
words = ["hello" , "world" , "lst" , "comprehenion" , "functions"]
print([len(word) for word in words])
