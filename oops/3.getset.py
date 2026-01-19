'''
Why getters and detters??
suppose you want:
- age should not be negative
- user cannot directly chnage sensitive data

so instead of allowing direct access to attributes,
we use getter and setter methods to control access and modification.
'''

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age # _ means protected (do not access directly)

#     # Getter method for age
#     def get_age(self):
#         return self._age
    
#     # Setter method for age
#     def set_age(self, age):
#         if age < 0:
#             print("Age cannot be negative.")
#         else:
#             self._age = age

# # Creating a Student object
# s1 = Student("Pulkit", 22)
# print(f"{s1.name} is {s1.get_age()} years old.")  # Using getter
# s1.set_age(25)  # Using setter to update age
# print(f"After birthday, {s1.name} is now {s1.get_age()} years old.")
# s1.set_age(-5)  # Trying to set a negative age

## Best way to use getters and setters : property() function
class Student:
    def __init__(self, name, age):
        self.name = name
        self._age = age # _ means protected (do not access directly)

    # Getter method for age
    @property
    def get_age(self):
        return self._age
    
    # Setter method for age
    @get_age.setter
    def set_age(self, age):
        if age < 0:
            print("Age cannot be negative.")
        else:
            self._age = age

s1 = Student("Pulkit", 22)
print(f"{s1.name} is {s1.get_age} years old.")  # Using getter
s1.set_age = 25  # Using setter to update age
print(f"After birthday, {s1.name} is now {s1.get_age} years old.")
s1.set_age = -5  # Trying to set a negative age