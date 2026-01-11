# ese likhte hai
'''
we can use double quotes (" ")
singke quotes (' ')
and triple quotes (""" """) for multiline strings
'''

# 1. Creating strings
a = "Hello"
b = 'World'
c = """This is
multi-line
string"""
print(a, b)
print(c)


#double quote ke andar doube quote syntax error deta hai

text = "Python"

# 2.Accessing Characters (Indexing)
print(text[0])
print(text[1])
print(text[-1])

# 3.String Slicing - (string[start:end])
print(text[0:3])   # Pyt
print(text[2:6])   # thon
print(text[:4])    # Pyth
print(text[3:])    # hon
print(text[0:-3]) # -3 ka matlab len(text) - 3

# 4.String is immutable
name = "Pulkit"
# name[0] = "B" # this will give error below is the correct way

name = "B" + name[1:]
print(name)


# 5.String length - use len()
print(len(text))

# 6.String concarenation
a = "Hello"
b = "Puki"
print(a + " " + b)

# 7.Repeating Strings
print("Hii "*3)

# 8.Strig Methods
# Convert Case
print(text.upper())
print(text.lower())

# Remove extra space
msg = "  hello   "
print(msg.strip())
print(msg.rstrip())
print(msg.lstrip())

# Replace words
str = "hello bro"
print(str.replace("bro", "puki"))

# Find words
print(str.find("bro"))

# Split string
fruits = "apple,mango, banana"
print(fruits.split(","))

# 9.Checking in String
abc = "hello bro puki"
print("pulkit" in abc)
print("puki" in abc)

# 10.String formatting
naam = "pulkit"
umar = 22
print(f"my name is {naam} and age is {umar}")

# 11.Escape characters
print("Hello\nWorld")   # new line
print("Hello\tWorld")   # tab space
print("He said: \"Hi\"")  # quotes
