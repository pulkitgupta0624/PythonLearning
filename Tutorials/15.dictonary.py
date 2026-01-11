'''
Dictionary is:
Unordered (but from Python 3.7 it keeps insertion order)
Mutable (can change)
Keys are unique
Values can be duplicate
'''

## 1) Creating Dictionary
# Using curly braces {}
student = {"name": "Pulkit", "age": 24, "city": "Delhi"}
print(student)

# using dict() function
employee = dict(name="Puki", age=30, department="HR")

## 2) Accessing Dictionary Elements
print(student["name"])   # Pulkit
print(student.get("age"))  # 24
print(employee["department"])  # HR

## 3) Adding new items
student["course"] = "Python"
print(student)

## 4) Updating values
student["age"] = 25
print(student)

## 5) Removing items
# using del
del student["city"]
print(student)

# using pop()
employee.pop("age")
print(employee)

# clear() → removes all items
employee.clear()
print(employee)

### 6) Dictionary Length
print(len(student))  # 3

## 7) Looping through Dictionary
# Loop through keys
for key in student:
    print(key, ":", student[key])

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(key, "->", value)


## 8) Dictionary Methods
data = {"a": 1, "b": 2, "c": 3}
# keys()
print(data.keys())  # dict_keys(['a', 'b', 'c'])
# values()
print(data.values())  # dict_values([1, 2, 3])
# items()
print(data.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])
# copy()
data_copy = data.copy()
print(data_copy)
# fromkeys()
new_dict = dict.fromkeys(['x', 'y', 'z'], 0)
print(new_dict)  # {'x': 0, 'y': 0, 'z': 0}

## 9) Nested Dictionary
nested_dict = {
    "student1": {"name": "Pulkit", "age": 24},      
    "student2": {"name": "Puki", "age": 22}
}
print(nested_dict["student1"]["name"])  # Pulkit    
print(nested_dict["student2"]["age"])   # 22

## 10) Dictionary Comprehension
squares = {x: x*x for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}