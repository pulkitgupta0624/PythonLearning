'''
Python does not have strict public/private/protected keywords like java.

✅ public → normal name
✅ _protected → single underscore
✅ __private → double underscore (name mangling)
'''

## Public members
# can be accessed from anywhere (inside/outside class)

class Employee:
    def __init__(self, name):
        self.name = name # public

s = Employee("Pulkit")
print(f'Employee name : {s.name}')

## Protected members (_)
# can be accessed inside class + childe class
# still accessible outside but should not be used outside (just a convention)

class Parent:
    def __init__(self):
        self._age = 24 # protected

class Child(Parent):
    def show(self):
        print(self._age) # accessible in child

c = Child()
c.show()

print(c._age) # accessible but not recommend


## Private members (__)
# ✅ Only accessible inside the class
# ❌ Not directly accessible outside

class Student:
    def __init__(self):
        self.__salary = 50000 # private

    def show_salary(self):
        print(self.__salary)

s = Student()

# print(s.__salary) # this will give error
s.show_salary() # accessible through class method

## Name mangling:
# Python changes the name internally like:
# salary becomes _Student__salary

# So technically you can access it like this:
print(s._Student__salary)