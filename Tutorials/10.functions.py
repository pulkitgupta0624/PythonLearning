## 1. Basic funtion
def greet():
    print("Hello Pulkit")

greet()


## 2. Functions with parameters
def salute(name):
    print("Hello", name)

salute("Puki")

## 3. Functions with return value
def add(a, b):
    return a+b

sum = add(15, 22)
print(sum)

## 4. Default Parameters
def average(a=10, b=4):
    avg = (a+b)/2
    print(avg)

average() # 7
average(2,4) # 3
average(4) # 4
average(b=6) # 8


## 5. Keyword Argument
def info(name, age):
    print(name, age)

info(age = 22, name= "Pulkit")
info("Shawty", 13)


## 6. *args (Multiple values)
def total(*nums):
    print(nums)

total(10,20,30,40)

## 7. **kwargs (Multiple keyword arguments)
def details(**data):
    print(data)

details(name="Pulkit", age=24, city="Dausa", state="Rajasthan")
details(naam="Puki", respectMe="Saab")

## 8. Lambda function (one-line function)
square = lambda x:x*x
print(square(8))

## 9. Recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))  # 120