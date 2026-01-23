## 1. dir() method
# returns list of attributes and methods of an object
x = [1, 2, 3]
print(dir(x))  # list of methods and attributes of list object

## 2. __dict__
# returns dictionary of object's writable attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p.__dict__)  # {'name': 'Alice', 'age': 30}

## 3. help() method
# provides help documentation for an object
print(help(str))  # help documentation for str class