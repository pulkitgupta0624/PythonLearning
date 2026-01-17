'''
File I/O means:
- Reading data from files
- Writing data to files

Opening a file:
file = open("filename.txt", "mode")

Modes:
- "r" : read (default mode)
- "w" : write (creates a new file or overwrites existing file)
- "a" : append (adds data to the end of the file)
- "b" : binary mode (for non-text files like images)
- "t" : text mode (default mode for text files)
- "x" : create (creates a new file, fails if file exists)
- "rb", "wb", "ab" : binary read, write, append 

'''

## Reading Operations
# Reading from a file
file = open("data.txt", "r")  # Open file in read mode
content = file.read()             # Read the entire file content
print("File Content:")
print(content)
file.close()

# Read one line
file = open("data.txt", "r")
line = file.readline()           # Read one line from the file
print("First Line:")
print(line)
file.close()

# Read all lines into a list
file = open("data.txt", "r")
lines = file.readlines()         # Read all lines into a list
print("All Lines:")
for line in lines:
    print(line.strip())          # Print each line without newline
file.close()

## Writing Operations
# Writing to a file
# overwrite existing content
file = open("data.txt", "w")  # Open file in write mode
file.write("Hello, World!\n")    # Write a line to the file
file.write("This is a test file.\n")
file.close()

# Appending to a file
file = open("data.txt", "a")  # Open file in append mode
file.write("Appending a new line.\n")  # Append a line to the file
file.close()

## Example of copy content from one file to another
# Copy content from data.txt to copy.txt
source_file = open("data.txt", "r")
destination_file = open("copy.txt", "w")
for line in source_file:
    destination_file.write(line)   
source_file.close()
destination_file.close()


## Using 'with' statement for file operations
# 'with' automatically handles closing the file
with open("data.txt", "r") as file:
    content = file.read()
    print("File Content using 'with':")
    print(content)

with open("data.txt", "a") as file:
    file.write("Adding another line using 'with'.\n")   

## File pointer operations (seek and tell)

# tell() - returns current position of file pointer
# seek() - moves the file pointer to a specified position
with open("data.txt", "r") as file:
    print("Initial Pointer Position:", file.tell())
    file.read(10)  # Read first 10 characters
    print("Pointer Position after reading 10 chars:", file.tell())
    file.seek(0)   # Move pointer back to the beginning
    print("Pointer Position after seek(0):", file.tell())


