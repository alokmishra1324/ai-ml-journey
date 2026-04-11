numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)

print(numbers[2:4])
print(numbers[0])
print(numbers[-1])

print(numbers[0:6])
print(numbers[5:])


square = [num**2 for num in range(10)]
print(square)

even_Numbers = [num for num in square if num%2==0]
print(even_Numbers)

numbers2 = [5, 3, 12, 89, 45, 33,12, 77, 11]

# Ascending sort
numbers2.sort()
print(numbers2)

#Descending sort
numbers2.sort(reverse=True)
print(numbers2)

unique_numbers = set(numbers2)
print(unique_numbers)

##Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(matrix[1][2])

## Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'. Sort the list of dictionaries by the 'score' in descending order and print the sorted list.
marks = [{"name": "Raj", "score": 87}, {"name": "Rahul", "score": 77}, {"name": "Rohit", "score": 66}, {"name": "Rakesh", "score": 90}]
marks.sort(key=lambda x: x["score"], reverse=True)
print(marks)


## Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose. Print the original and transposed matrices.
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

transposed_matrix = transpose(matrix)
print(transposed_matrix)
