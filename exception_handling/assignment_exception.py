# Write a function that takes two integers as input and returns their division. 
# Use try, except, and finally blocks to handle division by zero and print an appropriate message.

# def divisionfunc(a, b):
#     try:
#         result = a/b
#         return result
#     except ZeroDivisionError:
#         print("Enter the denominator greater than 0")
#     except Exception as ex:
#         print(ex)
#     finally:
#         print("Exceution is complete")
              

# print(divisionfunc(12,0))


## Write a function that reads the contents of a file named `data.txt`. 
# Use try, except, and finally blocks to handle file not found errors and ensure the file is properly closed.

# try:
#     with open("data.txt"  , 'r') as file:
#         contents = file.read()
#         print(contents)
# except FileNotFoundError:
#     print("The specified file is not found")
# except Exception as ex:
#     print(ex)
# finally:
#     print("File operation is done")


## Write a function that takes a list of integers and returns their sum. Use try, except, and finally blocks 
# to handle TypeError if a non-integer value is encountered and print an appropriate message.

# def sum_lst(numbers):
#     sum = 0
#     try:
#         for num in numbers:
#             if not isinstance(num , int):
#                 raise TypeError("Only integers allowed")
#             sum += num
#         return sum
#     except TypeError as e:
#         print(e)
#     finally:
#         print("Sum operation done successfully")
# list1 =[1,2,3,4,5,-1]
# print(sum_lst(list1))


## Write a function that prompts the user to enter an integer. Use try, except, and finally blocks to handle 
# ValueError if the user enters a non-integer value and print an appropriate message.

# def enter_int():
#     try:
#         user_input = input("Enter the integer")
#         x = int(user_input)
#         return x
#     except ValueError:
#         print("Please enter a integer value")
#         return None
#     finally:
#         print("Execution of input operation is complete")



# result = enter_int()
# print("Result:", result)


## Write a function that takes a dictionary and a key as input and returns the value associated with the key. Use try, except, and finally blocks to handle 
#  KeyError if the key is not found in the dictionary and print an appropriate message.

def get_val_dict(data , key):
    try:
        value = data[key]
        return value
    except KeyError:
        print(f"Error: {key} not found in dictionary")
    finally:
        print("Execution of dictionary lookup is complete")

dict1 = {'a' : 10 , 'b' :12 , 'c':15}

print(get_val_dict(dict1 , 'b'))
print(get_val_dict(dict1 , 'x'))

## Write a function that performs nested exception handling. It should first attempt to convert a string to an integer, and then attempt to divide by that integer. 
# Use nested try, except, and finally blocks to handle ValueError and ZeroDivisionError and print appropriate messages.


def nested_func(user_input):
    try:
        num = int(user_input)
        print("Conversion to integer is successfull")
        try:
            res = 100/num
            return res
        except ZeroDivisionError:
            print("Enter the number greater than 0")
        finally:
            print("Execution is complete")
    except ValueError:
        print("Invalid input please enter a valid integer")
    finally:
        print("outer operation is complete")

print(nested_func(123))


## Write a function that takes a list and an index as input and returns the element at the given index. 
# Use try, except, and finally blocks to handle IndexError if the index is out of range and print an appropriate message.

def ind_func(list1 , index):
    try:
        value = list1[index]
        return value
    except IndexError:
        print("Index out of range")
    finally:
        print("Execution is complete")

            

lst = [1,8,6,3,6]
print(ind_func(lst , 4))
print(ind_func(lst , 9))