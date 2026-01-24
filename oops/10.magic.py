'''
What are magic(dunder) methods?
Magic methods are special methods in python that:
- start and end with double underscores (dunder)
- are called automatically by python
- helps us to customize the behaviour of objects

Some commonly used magic methods:
1. __init__ : constructor method, called when an object is created
2. __str__ : returns string representation of an object
3. __add__ : defines behaviour of + operator
4. __len__ : defines behaviour of len() function

why are they called magic methods?
Because you don’t call them directly most of the time.
Python calls them internally when something happens.


Example:
print(obj)

the above line internally calls obj.__str__() method to get string representation of obj.
'''

## Example of some magic methods

class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __str__ (self):
        return f"Point({self.x}, {self.y})"
    
    def __add__ (self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __len__ (self):
        return int((self.x**2 + self.y**2)**0.5)  # Euclidean distance from origin
    
p1 = Point(3, 4)
p2 = Point(1, 2)
print(p1)               # Point(3, 4)  -> calls p1.__str__()
p3 = p1 + p2          # calls p1.__add__(p2)
print(p3)              # Point(4, 6)
print(len(p1))        # 5 -> calls p1.__len__()
print(len(p2))        # 2 -> calls p2.__len__()
# Output:
# Point(3, 4)   
# Point(4, 6)
# 5
# 2
