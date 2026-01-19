## Constructors is a special method in a class used to initialize objects.
'''
Syntax:
def __init__(self, parameters):
    # initialization code
'''

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
# Creating objects from the Car class
car1 = Car("Honda", "Civic", 2020)
car2 = Car("BMW", "X5", 2021)
print(car1.display_info())  # Output: 2020 Honda Civic
print(car2.display_info())  # Output: 2021 BMW X5

'''
Default Constructor:
If no constructor is defined, Python provides a default constructor that does nothing.
class Person:
    def info(self):
        return "This is a person."

p = Person()
print(p.info())  # Output: This is a person.

Parameterized Constructor:
A constructor that takes parameters to initialize object attributes.
Above is the example of parameterized constructor in Car class.
'''

'''
Python does not have multiple constructors like some other languages.
It means it does not support constructor overloading.
To achieve similar functionality, we can use default parameter values or variable-length arguments.
'''

class Person:
    def __init__ (self, name="Puki", occupation="Developer", salary=50000):
        self.name = name
        self.occupation = occupation
        self.salary = salary

    def info(self):
        return f"{self.name} is a {self.occupation} earning ${self.salary} per month."
    
p1 = Person()
print(p1.info())  # Output: Puki is a Developer earning $50000 per

p2 = Person("Alice", "Designer", 60000)
print(p2.info())  # Output: Alice is a Designer earning $60000 per month