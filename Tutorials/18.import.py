'''
using import instead of writing everything from scratch we can use:
- built-in modules (math, time, os, sys, random, datetime, etc)
- external modules (installed via pip like numpy, pandas, requests, etc)
- custom modules (our own python files like utils.py, helpers.py, etc)

# Basic import syntax:
import module_name

# import specific intems using from keyword:
from module_name import item1, item2

# import with alias using as keyword:
import module_name as alias_name
'''

# import math
# print(math.sqrt(16))  # Output: 4.0

# from math import sqrt, pi
# print(sqrt(25))  # Output: 5.0

# import random as rndom
# print(rndom.randint(1, 10))  # Output: Random integer between 1 and 10

# print(dir(rndom))  # Output: List of attributes and methods in random module


'''
Use of __name__ == "__main__":
When a Python file is run directly, the special variable __name__ is set to "__main__".
When the file is imported as a module in another file, __name__ is set to the module's name.

When we run a file directly:
eg. python file.py
the python sets: __name__ = "__main__"

that means "this file is being run directly"


When we import a file as a module:
eg. import file

the python sets: __name__ = "file"
that means "this file is being imported as a module, not run directly"
'''

import file

print("This is import.py")

## Problem: When you import file, its code also runs automatically

# Solution: Use if __name__ == "__main__": in file.py to control execution
# In file.py, wrap the code that should only run when the file is executed directly:    


# if __name__ == "__main__":
#     print("file.py is being run directly")
#     greet()

# Now when we import file, only the function definitions are imported, not the code inside the if block.
file.greet()  # We can still call the greet function from file.py
# Output:
# This is import.py

'''
summary : if __name__ == "__main__" : means run this part only when file is executed directly, not when imported.
'''