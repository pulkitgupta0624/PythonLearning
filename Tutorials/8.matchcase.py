a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

match op:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", a / b)
    case _:
        print("Invalid operator")
