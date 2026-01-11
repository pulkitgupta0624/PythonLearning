'''
Set is:
Unordered (no fixed index)
Unchangeable elements (but you can add/remove items)
No duplicate values
Faster for searching
'''

## 1) Creating Set
# Using curly braces {} 
fruits = {"apple", "banana", "mango"}
nums = {10, 20, 30}
mix = {1, "Pulkit", True, 5.5}
s = {1, 2, 3, 4, 5, 5, 2}
print(s)  # {1, 2, 3, 4, 5} (duplicates removed)

## 2) Accessing Set Elements
# sets are unordered, so you cannot access items by index
for item in s:
    print(item)

## 3) Adding Elements to Set
# add() → adds single element
s.add(6)
print(s)

# update() → adds multiple elements
s.update([7, 8, 9])
print(s)

## 4) Removing Elements from Set
# remove() → removes specific element (error if not found)
s.remove(3)
print(s)

# discard() → removes specific element (no error if not found)
s.discard(10)  # no error
print(s)

# pop() → removes a random element
removed_item = s.pop()
print("Removed:", removed_item) 
print(s)

# clear() → removes all elements
s.clear()
print(s)

## 5) Set Length
s = {1, 2, 3, 4, 5}
print(len(s))  # 5

## 6) Set Operations
A = {1, 2, 3, 4}    
B = {3, 4, 5, 6}

# Union
print(A | B)  # {1, 2, 3, 4, 5, 6}
print(A.union(B))  # {1, 2, 3, 4, 5, 6}

# Intersection
print(A & B)  # {3, 4}
print(A.intersection(B))  # {3, 4}

# Difference
print(A - B)  # {1, 2}
print(A.difference(B))  # {1, 2}

# Symmetric Difference
print(A ^ B)  # {1, 2, 5, 6}
print(A.symmetric_difference(B))  # {1, 2, 5, 6}    

## 7) Checking Membership
s = {1, 2, 3, 4, 5}
print(3 in s)    # True
print(10 not in s)  # True

## Note : empty set is created using set() not {}
empty_set = set()
print(type(empty_set))  # <class 'set'>



## Difference between intersection_update() and intersection()
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A.intersection_update(B)  # A is updated to intersection
print(A)  # A is now {3, 4}

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = A.intersection(B)  # C is new set with intersection
print(C)  # C is {3, 4}

