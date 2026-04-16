##syntax

##lambda arguments:expression

##Normal addition
def add(a, b):
    return a+b
print(add(9,8))

##Using Lambda function
addition = lambda a,b:a+b

print(addition(6, 7))

even_num = lambda num:num%2==0

print(even_num(9))


#map() with lambda

numbers = [1,2,3,4,5]
print(list(map(lambda x:x**2, numbers)))


def square(x):
    return x*x

print(list(map(square, numbers)))

## map multiple iterables

num1 = [1,2,3]
num2 = [4,5,6]

added_num = list(map(lambda x,y:x+y , num1, num2))
print(added_num)

##map to convert a list of strings to integers

str_num = ['1' ,'2' ,'3' ,'4' ,'5']
int_num = list(map(int , str_num))

print(int_num)

words = ['apple' , 'banana' , 'cherry']
upper_word = list(map(str.upper , words))

print(upper_word)

def get_name(person):
    return person['age']

people = [
    {'name' :'Rama' , 'age':32},
    {'name' : 'Shyama' , 'age' :23}
]

print(list(map(get_name, people)))

##Filters

lst = [1,2,3,4,5,6,7,8,9,11,12,13]
print(list(filter(even_num , lst)))
print(list(filter(lambda x:x>5 , lst)))


#filter with lambda functions with multiple conditions

##even and greater than 5
print(list(filter(lambda x:x> 5 and x%2==0 , lst)))

def age_greater(person):
    return person['age']>25

print(list(filter(age_greater , people)))