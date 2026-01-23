'''
A class methods is a method inside a class that:
- uses cls parameter that points to the class
- can access class variables and other class methods
- can be called using class name or object
- is defined using @classmethod decorator


'''
class Student:

    college = "IIIT"

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college

print("Before changing college:", Student.college)  # IIIT
Student.change_college("IIT")
print("After changing college:", Student.college)   # IIT