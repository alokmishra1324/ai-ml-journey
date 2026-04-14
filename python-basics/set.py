my_empty_set = set()
print(my_empty_set)
print(type(my_empty_set))

my_set = {1,2,3,4,5,3,2}
print(my_set)
print(type(my_set))

my_set.add(7)
print(my_set)

my_set.remove(2)
print(my_set)

my_set.discard(9)
print(my_set)

my_set.pop()
print(my_set)

my_set.clear()
print(my_set)

my_set2 = {1,2,3,4,5}
print( 3 in my_set2)
print(9 in my_set2)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

union_set = set1.union(set2)
print(union_set)

intersection_set = set1.intersection(set2)
print(intersection_set)

# print(set1)
# set1.intersection_update(set2)
# print(set1)

print(set1.difference(set2))
print(set2.difference(set1))

# set1.difference_update(set2)
# print(set1)

print(set1.symmetric_difference(set2))

print(set1.issubset(set2))
print(set1.issuperset(set2))

text = "Hello in this tutorial we will learn about sets in python"
words = text.split()
unique_words = set(words)
print(unique_words)
print(len(unique_words))


squares = {x **2 for x in range(1, 11)}
print(squares)
print(type(squares))

even_numbers = {x for x in my_set2 if x%2==0}
print(even_numbers)

vowels = frozenset(['a', 'e' , 'i' , 'o' , 'u'])

print(vowels)

print(type(vowels))

num1 = frozenset([1,2,3,4,5])
num2= frozenset([4,5,6,7,8])

print(num1.union(num2))
print(num1.intersection(num2))

# num1.add(6)  # This will give error as frozenset is immutable

print(num1.issubset(num2))
print(num1.issuperset(num2))


##Create a set with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a set. Print the resulting set.

num3 = set([1,2,3,4,5])
list_num = list(num3)
print(list_num)
list_num.append(6)
num3 = set(list_num)
print(num3)

my_dict = {"a" :1 , "b":2 , "c":3}
print(my_dict)

for i in num3:
    print(i)

##Create a set and remove elements from it until it is empty. Print the set after each removal.
while num3:
    if len(num3) == 0:
        break
    num3.pop()
    print(num3)

## Create a set containing tuples, where each tuple contains two elements. Print the set.
set_tuple = {(1,2) , (3,4)  , (5,6) }

print(set_tuple)
print(type(set_tuple))

##Create a set and test if certain elements are present in the set. Print the results.
my_set4 = {1,2,3,4,5}
print(3 in my_set4)
print(9 in my_set4)
