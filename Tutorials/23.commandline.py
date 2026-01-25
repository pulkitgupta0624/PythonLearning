'''
A coomand line utility is a program that:
- runs from the command line (terminal/console)
- takes input arguments from the command line
- performs a task (like ls, pip, git, etc)

example:
python myscript.py arg1 arg2
'''

## basic command line utility example
# import sys

# name = sys.argv[1]  # first argument from command line
# age = sys.argv[2]   # second argument from command line

# print(f"Hello, {name}! You are {age} years old.")

# To run this script, save it as myscript.py and execute from command line:
# python myscript.py Alice 30

## Advanced example: A simple calculator
import argparse

parser = argparse.ArgumentParser(description="Simple Command Line Calculator")

parser.add_argument("a", type=float, help="First Number")
parser.add_argument("b", type=float, help="Second Number")
parser.add_argument("operation", type=str, choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")  

args = parser.parse_args()

print(args)

if args.operation == "add":
    result = args.a + args.b
elif args.operation == "subtract":
    result = args.a - args.b
elif args.operation == "multiply":
    result = args.a * args.b
elif args.operation == "divide":
    if args.b != 0:
        result = args.a / args.b
    else:
        result = "Error: Division by zero"

print(f"The result of {args.operation}ing {args.a} and {args.b} is: {result}")  

# To run this script, save it as calculator.py and execute from command line:
# python calculator.py 10 5 add 
