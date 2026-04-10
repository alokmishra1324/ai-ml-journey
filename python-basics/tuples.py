## createing a tuple

empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

lst = list()
print(type(lst))
tpl = tuple()
print(type(tpl))

## list to tuple
numbers = tuple([1,2,3, 4, 5 , 6, 7, 8, 9 ,10])
print(numbers)
## tupel to list
print(list((1,2,3, 4,5)))

mixed_tuple = (1, 2, "Alok" , 3.255 , True)
print(mixed_tuple)

print(numbers[3])
print(numbers[-1])
print(numbers[3:])
print(numbers[:6])
print(numbers[:-1])
print(numbers[::2])
print(numbers[3:5])

## tuple operations
concat_tuple = numbers + mixed_tuple
print(concat_tuple)

print(mixed_tuple *3)
print(numbers *2 )

## Immutable nature of tuples

lst = [1,2,3,4, 5]
lst[1] = "Alok"
print(lst)

# tple = (1,2,3, 4,5)
# tple[1] = "Alok"
# print(tple)  # this will give error

print(numbers.count(1))
print(numbers.index(4))
 
 ## Packing and unpacking a tuple
packed_tuple = 1,"Hello",5.99
print(packed_tuple)

a , b, c = packed_tuple
print(a)
print(b)
print(c)

first , *middle , last =numbers
print(first)
print(middle)
print(last)

## Nested list

lst = [[1,2,3,4,5],[6,7,8, 9],[1 , "Hello" , 3.14]]
print(lst[0][0:2])
print(lst)

lst1 = [[1,2,3,4,5],[6,7,8, 9],(1 , "Hello" , 3.14)]
print(lst1[2][2])

## Nested tuple

nested_tuple = ((1,2,3,) , ("a" , "b" , "c") , (True , False))
print(nested_tuple[2])
print(nested_tuple[1][-1])

for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item , end = " ")
    print()    
