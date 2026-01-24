'''
Methods Overriding in Python
Method overriding is a feature in object-oriented programming that allows a subclass (derived class) to provide
a specific implementation of a method that is already defined in its superclass (base class). When the method is called on an instance of the subclass, the overridden method in the subclass is executed
instead of the one in the superclass.

- The method name must be same
- The parameters must be same or compatible
'''

## Example of method overriding

class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Car started with a roar!")

c = Car()
v = Vehicle()

c.start()  # Output: Car started with a roar!
v.start()  # Output: Vehicle started

'''
What is method overloading?
Method overloading is a feature in some programming languages that allows a class to have multiple methods with the same name but different parameters (different type or number of parameters). However, Python does not support method overloading in the traditional sense. In Python, if you define multiple methods with the same name in a class, the last defined method will override the previous ones.

'''

## Example showing lack of method overloading in Python
class MathOperations:
    def add(self, a, b):
        return a + b

    # This method will override the previous add method
    def add(self, a, b, c):
        return a + b + c
    
m = MathOperations()
# print(m.add(2, 3))        # This will raise a TypeError   
print(m.add(2, 3, 4))     # Output: 9

'''
To achieve similar functionality as method overloading, we can use default arguments or variable-length arguments.

'''

'''
Operator Overloading
Operator overloading is a feature in object-oriented programming that allows developers to define custom behavior for operators
(for example, +, -, *, etc.) when they are used with user-defined classes. This is done by defining special methods (also known as magic methods or dunder methods) in the class that correspond to the operators.

Example:
a+b

for integers, the + operator adds the two numbers.
for strings, the + operator concatenates the two strings.
In operator overloading, we can define how the + operator behaves when used with instances of our custom class.

'''

## Example of operator overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2  # This will call v1.__add__(v2)
print(v3)      # Output: Vector(6, 8)
