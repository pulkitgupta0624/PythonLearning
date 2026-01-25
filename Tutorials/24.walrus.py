'''
The walrus operator (:=) is a new assignment expression operator introduced in Python 3.8. 
It allows you to assign a value to a variable and use it at the same time.
This can help to reduce redundancy and improve code readability in certain situations.
'''

# Example without walrus operator
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_evens = []
for n in numbers:
    if n% 2 == 0:
        squared = n**2
        squared_evens.append(squared)

print(squared_evens)  # Output: [4, 16, 36, 64, 100]

# Example with walrus operator
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_evens = []
for n in numbers:
    if(squared := n**2) % 2 == 0:
        squared_evens.append(squared)
print(squared_evens)  # Output: [4, 16, 36, 64, 100]