'''
A generator is a special type of function that:
- returns values one at a time.
- uses the 'yield' keyword instead of 'return'.
- maintains its state between successive calls.
- is memory efficient for large datasets.

👉 Instead of returning all values at once (like a list), it produces them on demand.
'''

# Normal function
def square_numbers(nums):
    result = []
    for n in nums:
        result.append(n * n)
    return result

# Generator function
def square_numbers_gen(nums):
    for n in nums:
        yield n * n

# Using the normal function
numbers = [1, 2, 3, 4, 5]
squared = square_numbers(numbers)
print("Squared using normal function:", squared)

# Using the generator function
squared_gen = square_numbers_gen(numbers)       
print("Squared using generator function:", list(squared_gen))

