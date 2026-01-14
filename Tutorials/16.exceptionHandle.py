## An exception is an error that occurs during program execution.

'''
Syntax:
try:
    # Code that may raise an exception
except ExceptionType:
    # Code to handle the exception
'''

## 1) Basic Example
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print("Result:", a / b)
# except:
#     print("An error occurred. Please check your inputs.")


## 2) Handling Specific Exceptions
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")

## 3) try-except-else : else block runs if no exception occurs
try:
    a = int(input("Enter a number: "))
    print(10/a)
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division successful.")


## 4) try-except-finally : finally block always runs
try:
    a = int(input("Enter a number: "))
    print(10/a) 
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Execution completed.")


## 5) Raising Exceptions (manually raising exceptions)
age = int(input("Enter your age: "))
if age < 18:
    raise ValueError("Age must be at least 18.")

print("You are eligible.")

# we can throw built-in exceptions like ValueError, TypeError, etc.
# or create custom exceptions by defining new exception classes.


