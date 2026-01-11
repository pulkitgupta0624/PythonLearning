## A tuple is a collection used to store multiple items in a single variable.
## Tuple is:
# Ordered
# Immutable (cannot be changed)
# Allows duplicate values
# Faster than list

## 1) Creating Tuples
t1 = (1, 2, 3)
t2 = ("Pulkit", "Puki", "Bro")
t3 = (1, "hello", 3.5, True)

# If tuple has only 1 element, you must put comma ,
t = (5,) # if not comma then its type is int not tuple
print(type(t))


## 2) Accessing Tuple Elements (Indexing)
names = ("Pulkit", "Aman", "Rahul")

print(names[0])   # Pulkit
print(names[-1])  # Rahul


## 3) Slicing Tuple
nums = (10, 20, 30, 40, 50)

print(nums[1:4])   # (20, 30, 40)
print(nums[:3])    # (10, 20, 30)
print(nums[2:])    # (30, 40, 50)


## 4) Tuple is Immutable (Cannot Change)
# nums[1] = 99  # error

# But you can convert tuple → list → change → tuple:
temp = list(nums)
temp[1] = 99
nums = tuple(temp)

print(nums)   # (10, 99, 30)


## 5) Looping through Tuple
t = (1, 2, 3)

for i in t:
    print(i)


## 6) tuple methods
t = (1, 2, 2, 3, 2)
print(t.count(2))
print(t.index(2))


## 7) Tuple Packing & Unpacking
# Packing
data = 10, 20, 30
print(data)  # (10, 20, 30)

# Unpacking
t = (10, 20, 30)
a, b, c = t
print(a, b, c)


## 8) Tuple with * (unpacking multiple values)
t = (1, 2, 3, 4, 5)
a, b, *c = t

print(a)  # 1
print(b)  # 2
print(c)  # [3, 4, 5]


