## Declaring and initailzing the variables

age=25
name = "Alok"
height = 5.7
is_working = True

print("Age:" , age) #int
print("Name:" , name) #str
print("Height:", height) #float
print("Working:" , is_working) #bool

## Naming Conventions
## Variables names should be descriptive
## They must start with letter or '_' and contains number, letters and underscores
## variables are case senisitive

##valid variable names

first_name = "Alok"

## invalid variables names
## 2age = 30
## @name = "Alok"
## first-name = "ALok"

## Python is dynamically types language , type of a variable determine at a run time

## Type checking and type conversion

age = 25
print(type(age))

age_str = str(age)
print(type(age_str))

'''
name = "alok"
int(name)

'''

height = 5.7
print(int(height))
print(type(int(height)))
print(float(int(height)))

## python allows the variable to change as teh program executes

var = 10
print(var , type(var))

var = "Hello"
print(var , type(var))

var = 7.99
print(var , type(var))


age = int(input("What is the age:"))
print(age)
print(type(age))

## Simple Calculator

num1  = float(input("Enter the first number:"))
num2  = float(input("Enter the second number:"))

sum = num1 + num2
diff = num1 - num2
multi = num1*num2
div = num1/num2

print("Sum of num1 and num2 is:" , sum)
print("Diff of num1 and num2 is:" , diff)
print("Multi of num1 and num2 is:" , multi)
print("Div of num1 and num2 is:" , div)

##bool datatype

a=10
b=10
print(type(a==b))

result = "Hello" + str(5)
print(result)
