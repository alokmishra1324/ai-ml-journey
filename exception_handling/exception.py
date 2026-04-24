# try:
#     a=b
# except:
#     print("The variable has not been assigned")


# try:
#     a=b
# except NameError as ex:
#     print(ex)


  
# try:
#     res = 1/2  
#     a=b
# except  ZeroDivisionError as ex:
#     print(ex)
#     print("Please enter the denominator greater than 0")
# except Exception as ex1:
#     print(ex1)
#     print("Main exception got caught here")


##try, except, else block

# try:
#     num = int(input("Enter a number "))
#     result =10/num
# except ValueError:
#     print("This is not a valid number")
# except ZeroDivisionError:
#     print("Enter the denominator greater than 0")
# except Exception as ex:
#     print(ex)
# else:
#     print(f"The result is {result}")
# finally:
#     print("Exception complete")



## File handling and Exception Handling

try:
    file = open('example1.txt' , 'r')
    content = file.read()
    # a=b
    print(content)
except FileNotFoundError:
    print("The file does not exist")
except Exception as ex:
    print(ex)
finally:
    if 'file' in locals() and not file.close():
        file.close()
        print('file close')