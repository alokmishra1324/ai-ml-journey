class Car:
    pass

audi = Car()
bmw = Car()

print(type(audi))


print(audi)
print(bmw)

audi.windows = 4
print(audi.windows)

print(dir(audi))

##Instance variable and Methods

class Dog:
    ## constructor
    def __init__(self , name , age):
        self.name = name
        self.age = age

## create objects
dog1 = Dog("Buddy" ,3)
print(dog1)
print(dog1.name)
print(dog1.age)


##Define a class with instance methods

class Cat:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    def meow(self):
        print(f"{self.name} says meow")

cat1 = Cat("Lucy" , 3)
cat1.meow()


## Modelling a bank account

## Define a class for bank account 

class BankAccount:
    def __init__(self , owner , balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self , amount):
        self.balance += amount
        print(f"{amount} is deposited. New Balance is {self.balance}")
    
    def withdraw(self , amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"{amount} is withdrawn. New Balance is {self.balance}" )
    
    def get_balance(self):
        return self.balance
    

account = BankAccount("Alok" , 5000)
print(account.balance)

account.deposit(20000)

account.withdraw(300)

print(account.get_balance())