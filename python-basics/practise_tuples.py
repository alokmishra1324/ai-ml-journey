numbers = (1,2,3,4,5, 6 ,7, 8, 9, 10)
print(numbers)

first , *middle , last = numbers
print(first)
print(middle)
print(last)

print(numbers[:3])
print(numbers[2:5])
print(numbers[7:])

matrices = ((1,2,3),(4,5,6),(7,8,9))
print(matrices[1][2])

num1 = (1,2,3)
num2 = (4,5,6)

res = num1 + num2
print(res)

num3 = (33, 55, 24, 89, 23, 67, 33, 89)
print(num3.count(89))
print(num3.index(67))
print(set(num3))
print(num3)

elements = (23, "Alok" , 3.14, True)

a, b, c, d = elements
print(a)
print(b)
print(c)
print(d)

num4 = [1,2,3,4,5]
converted_tuple = tuple(num4)
print(converted_tuple)

elements1 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(elements1)

num5 = (1,2,3,4,5)
converted_list = list(num5)
print(converted_list)
converted_list.append(6)
converted_tuple2 = tuple(converted_list)
print(converted_tuple2)

##Create a dictionary with tuple keys and integer values. Print the dictionary.
my_dict = {("a", "b"): 1, ("c", "d"): 2, ("e", "f"): 3}
print(my_dict)
print(my_dict[("a", "b")])

##Write functions that take a tuple and return the minimum, maximum, and sum of the elements. Print the results for a sample tuple.
def tuple_stats(tup):
    minimum = min(tup)
    maximum = max(tup)
    total_sum = sum(tup)
    return minimum, maximum, total_sum


sampleTuple = (23, 12, 90, 56) 

mini , maxi , sumof = tuple_stats(sampleTuple)
print("Minimum" , mini)
print("Maximum" , maxi)
print("Sum" , sumof) 