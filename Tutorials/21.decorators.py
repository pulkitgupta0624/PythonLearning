'''
Decorators in Python:
Decorators are a powerful and expressive feature in Python that allows you to modify the behavior of functions or methods. 
They are often used for logging, access control, instrumentation, and caching.
'''

## Basic example without decorator
# def greet():
#     print("Hello!")

# greet()  # Output: Hello!

## now suppose we want
# print "Good Morning!" before greeting
# and "Have a nice day!" after greeting
# we use decorator for this

def decorator(func):
    def wrapper():
        print("Good Morning!")
        func()
        print("Have a nice day!")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()

'''
@decorator is just a shorthand for:
greet = decorator(greet)
'''

## Decorators with parameters
def decorator_with_params(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function.")
        result = func(*args, **kwargs)
        print("After calling the function.")
        return result
    return wrapper

@decorator_with_params
def add(a, b):
    return a + b

result = add(5, 3)
print(f"Result: {result}")


### Timing decorator example
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function took {end - start} seconds to execute.")
        return result
    return wrapper

@timer
def loop_work():
    for i in range(100000000):
        pass

loop_work()