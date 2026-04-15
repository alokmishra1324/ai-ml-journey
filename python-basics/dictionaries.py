empty_dict = {}
print(empty_dict)
print(type(empty_dict))

student = {"name":"Alok" , "age" : 25 , "city" :"Hyd"}
print(student)
print(type(student))

##single key is always used
# student1 = {"name":"Alok" , "age" : 25 , "name" :"Hyd"}
# print(student1)


## accessing values in a dictionary
print(student["age"])
print(student["city"])

print(student.get("city"))
print(student.get("last_name"))
print(student.get("last_name", "Not Found"))


##modifying values in a dictionary
print(student)
student["age"] = 26
print(student)

student["country"] = "India"
print(student)

## removing key-value pairs from a dictionary
del student["age"]
print(student)

keys = student.keys()
print(keys)
values = student.values()
print(values)
items = student.items()
print(items)


#shallow copy

student_copy= student
print(student_copy)
print(student)


student_copy["name"] = "Bunty"
print(student_copy)
print(student)


student_copy1 = student.copy()
print(student_copy1)
print(student)

student_copy1["name"] = "Alok"
print(student_copy1)
print(student)

##Iterating over dictionaries

## Iterate over keys

for keys in student.keys():
    print(keys)

## Iterate over values
for values in student.values():
    print(values)

## Iterate over key-value pairs
for key , value in student.items():
    print(f"{key} : {value}")


#Nested Dictionaries
students ={
    "student1":{"name" :"Alok" , "age":25 },
    "student2":{"name" :"Bunty" , "age":24 }
}

print(students)

## Access nested dictionaries elements
print(students["student1"]["age"])
print(students["student2"]["name"])  

## Iterating over nested dictionaries

for student_id , student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key , val in student_info.items():
        print(f"{key} : {val}") 

## Dictionary comprehension
squares = {x:x**2 for x in range(1, 11) }
print(squares)


evens = {x:x**2 for x in range(1, 6) if x%2==0}
print(evens)

numbers = [1,2,2,2,3,3,3,3,3,4,4,4,4,4,4]
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
print(frequency)             

##merge 2 dictionary

dict1 = {"a":1 , "b":2}
dict2 = {"c":3 , "d":4}
merges_dict = {**dict1 , **dict2}
print(merges_dict)

## Create a dictionary with the first 10 positive integers as keys and their squares as values. Print the dictionary.

my_dict_num = {x:x**2 for x in range(1, 11)}
print(my_dict_num)

##Print the value of the key 5 and the keys of the dictionary created in Assignment 1.
print(my_dict_num[5])
print(my_dict_num.keys())

##Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. Print the modified dictionary.
my_dict_num[11] = 121
print(my_dict_num)
del my_dict_num[1]
print(my_dict_num)

##Iterate over the dictionary created in Assignment 1 and print each key-value pair.
for key , value in my_dict_num.items():
    print(f"{key} : {value}")

## Create a new dictionary containing the cubes of the first 10 positive integers using a dictionary comprehension. Print the new dictionary.
cubes = {x:x**3 for x in range(1, 11)}
print(cubes)

## Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.
squares1 = {x:x**2 for x in range(1, 3)}
squares2 = {x:x**2 for x in range(4, 6)}

merge_squares = {**squares1 , **squares2}
print(merge_squares)


##Create a nested dictionary representing a student with keys 'name', 'age', 'grades', where 'grades' is another dictionary with keys 'math', 'science', and 'english'. Print the nested dictionary.
student_nested = {
    "name":"Rajan",
    "age":25,
    "grades":{
        "math":85,
        "science":90,
        "english":88
    }
}

print(student_nested)

##Create a dictionary where the keys are the first 5 positive integers and the values are lists containing the first 5 multiples of the key. Print the dictionary.
multiples = {1:[1,2,3,4,5], 2:[2,4,6,8,10], 3:[3,6,9,12,15]}
print(multiples)
multiples_dict = {i: [i * j for j in range(1, 6)] for i in range(1, 6)}
print(multiples_dict)


##Create a dictionary where the keys are the first 5 positive integers and the values are tuples containing the key and its square. Print the dictionary.
squares_tuple = {i:(i, i**2) for i in range(1, 6)}
print(squares_tuple)

##Create a dictionary with the first 5 positive integers as keys and their squares as values. Convert the dictionary to a list of tuples and print it.
list_squares = list(squares.items())
print(list_squares)
print(type(list_squares))


##Create a dictionary with the first 10 positive integers as keys and their squares as values. Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary.
even_squares = {x:x**2 for x in squares if x%2==0}
print(even_squares)

## Create a dictionary with the first 5 positive integers as keys and their squares as values. Create a new dictionary with keys and values swapped. Print the new dictionary.
swapped_dict = {value:key for key , value in squares.items()}
print(swapped_dict)


##Create a default dictionary where each key has a default value of an empty list. Add some elements to the lists and print the dictionary.
from collections import defaultdict
default_dict = defaultdict(list)
default_dict["a"].append(1)
default_dict["a"].append(2)
default_dict["c"].append(4)
print(default_dict)

## Write a function that takes a string and returns a dictionary with the count of each character in the string. Print the dictionary.
def char_count(s):
    count_dict = {}
    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

string = "hello world"
result = char_count(string)
print(result)


def char_count(s):
    count_char = {}
    for char in s:
        if char in count_char:
            count_char[char] +=1
        else:
            count_char[char] = 1
    return count_char

string1 = "Alok Mishra"
res = char_count(string1)
print(res)    









