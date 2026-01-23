'''
A static method is a method inside a class that:
- does not use self (object)
- does not use cls (class)
- works like a normal function but kept inside class for better structure

use static methods when"
- method belongs to class logically
- but it des not need object or class data

example: a calculator methods, checking prime number, utility functions

'''

class MathUtils:

    @staticmethod
    def add(a, b):
        return a+b
    
print(MathUtils.add(5, 10))  # 15
# here we call static method using class name directly without creating object

class NumberUtils:

    @staticmethod
    def is_even(n):
        return n % 2 == 0   
    
print(NumberUtils.is_even(4))  # True
print(NumberUtils.is_even(7))  # False


'''
Difference between instance, class and static methods:
1. Instance methods:
    - use self
    - access object data
    - called by object

2. Class methods:
    - use cls
    - access class data
    - called by class or object

3. Static methods:
    - no self or cls
    - no access to object or class data
    - called by class or object
'''

class Demo:

    class_var = "class variable"

    def instance_methods(self):
        print("Instance method called", self.class_var)

    @classmethod
    def class_method(cls):
        print("Class method called", cls.class_var)

    @staticmethod
    def static_method():
        print("Static method called")

demo = Demo()
demo.instance_methods()  # Instance method called class variable
Demo.class_method()      # Class method called class variable   
Demo.static_method()     # Static method called
