#variable is a container that holds data

a=1
print(a, type(a), sep=':')
b="puki" 
print(b, type(b), sep=':')

# 1.Numeric data
c = 1
d = 1.5
e = complex(7, 8)

print(c, type(c))
print(d, type(d))
print(e, type(e))

# 2.Text type data
name = "Pulkit"
print(name, type(name))

# 3.Boolean type
x = True
y = False
print(x, type(x))
print(y, type(y))

# 4.Sequence type

# list - mutable or can be change
fruits = ["apple", "banana", "mango"]
print(fruits, type(fruits))

# tuple - immutable or cannot be change
numbers = (10, 20, 30)
print(numbers, type(numbers))

# range - sequence of numbers
m = range(1,9)
print(m, type(m))

# 5.Set types
# set - unique + unordered elements
s = {1,2,2,3,4,5,5}
print(s, type(s))

# fronzenset - immuatable set
fs = frozenset([1,2,3,1,2])
print(fs, type(fs))

# 6.Mapping type
# dict - key-value pairs
student = {"name" : "pulkit", "age" : 24}
print(student, type(student))

# 7.None type
abc = None
print(abc, type(abc))
