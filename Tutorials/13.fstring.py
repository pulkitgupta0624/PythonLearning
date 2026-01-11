name = "Pulkit"
age = 24

print(f"My name is {name} and my age is {age}")


# using expressions inside f-string
a = 10
b = 20
print(f"The sum of {a} and {b} is {a+b}")

# using functions inside f-string
def multiply(x, y):
    return x * y

print(f"The product of {a} and {b} is {multiply(a, b)}")

# formatting float values
pi = 3.141592653589793
print(f"Value of pi up to 2 decimal places: {pi:.2f}")