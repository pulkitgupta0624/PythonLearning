'''
super() is used to call methods or constructors of the parent class from a child class
'''

## super() with methods

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()  # Call the parent class method
        print("Dog barks")

d = Dog()
d.speak()


## super() with constructors
class Person:
    def __init__(self, name):
        self.name = name
        print("parent constructor called")

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)  # Call the parent class constructor
        self.emp_id = emp_id
        print("child constructor called")

e = Employee("Alice", 101)
print(e.name)    # Alice
print(e.emp_id)  # 101
