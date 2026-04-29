'''
__add__(self , other): Adds two objects using the + operator
__sub__(self , other): Subtracts two objects using - operator
__mul__(self , other): Multiplies two objects using * operator
__truediv__(self , other):Divides two objects using / operator
__eq__(self , other):Checks if two objects are eual using == operator
__lt__(self , other): Checks if one object is less than another using the < operator
__gt__(slef , other): Checks if one object is greater tha another using > operator

'''
## Mathematical operation for Vectors
class Vector:
    def __init__(self , x, y):
        self.x = x
        self.y = y
    
    def __add__(self , other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self , other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self , other):
        return Vector(self.x * other.x, self.y * other.y)
    
    def __eq__(self , other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f"Vector({self.x} , {self.y})"
    
## Create objects of the Vector class
v1 = Vector(2,3)
v2 = Vector(5,4)

print(v1+v2)
print(v1-v2)
print(v1*v2)