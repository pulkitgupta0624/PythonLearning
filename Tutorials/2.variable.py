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


'''
Local vs Global Variable

1. Local Variable:
- A local variable is defined within a function and can only be accessed inside that function.

def my_function():
    local_var = 10
    print("Local Variable:", local_var)

my_function()
# print(local_var)  # This will raise an error because local_var is not accessible here


2. Global Variable:
- A global variable is defined outside of any function and can be accessed from any function within the same module.
global_var = 20
def another_function():
    print("Global Variable:", global_var)

another_function()
print("Global Variable from outside:", global_var)

3. Local and Global Variable with the Same Name:
- If both have same name, Python will use the local one inside function.

x = 50  # global

def test():
    x = 10  # local
    print(x)

test()
print(x)

output:
10
50

Note : is we modify global variable inside function, this will not change global variable unless we use 'global' keyword.
- To modify a global variable inside a function, use the 'global' keyword.

count = 0  # global variable
def increment():
    global count  # Declare that we are using the global variable 'count'
    count += 1
    print("Inside function, count:", count) 

increment()
print("Outside function, count:", count)

'''


'''
Difference between == and is operator
1. == Operator:
- The '==' operator checks for value equality. It returns True if the values of the two operands are equal, regardless of whether they are the same object in memory.
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True, because values are equal

2. is Operator:
- The 'is' operator checks for identity. It returns True if both operands refer to the same object in memory.
print(a is b)  # False, because they are different objects in memory

c = a
print(a is c)  # True, because both refer to the same object

best practice: use '==' for value comparison and 'is' when comparing with none.
'''