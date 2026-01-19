'''
OOPS is a programming style where we create:
Class → Blueprint / design
Object → Real thing made from that blueprint

Example:
Class = Car design
Object = Your real car (Honda, BMW, etc.)
'''

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         return f"{self.year} {self.make} {self.model}"
    
# # Creating objects from the Car class
# car1 = Car("Honda", "Civic", 2020)
# car2 = Car("BMW", "X5", 2021)
# print(car1.display_info())  # Output: 2020 Honda Civic
# print(car2.display_info())  # Output: 2021 BMW X5

class Person:
    name = "Puki"
    occupation = "Developer"
    salary = 50000

    def info(self):
        return f"{self.name} is a {self.occupation} earning ${self.salary} per month."
    
p1 = Person()
print(p1.info())  # Output: Puki is a Developer earning $50000 per month.

p2 = Person()
p2.name = "Alice"
p2.occupation = "Designer"
p2.salary = 60000
print(p2.info())  # Output: Alice is a Designer earning $60000 per month
    

## self keyword : self represents the current object
# means : object ke andar jo bhi attribute or method hoga wo self k through access hoga