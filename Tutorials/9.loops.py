## For loop

# print 1 to 10
for i in range(1,11):
    print(i)

# loop through string
name = "pulkit"
for ch in name:
    print(ch)

# loop through a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    # print(fruit)
    print(fruit, end=',')


## While loop 
# Used when you don’t know exact number of repetitions, depends on a condition.

# Print 1 to 5
print('')
i = 1
while i <= 5:
    print(i)
    i += 1


## Range() in for loop
## range(start, stop, step)

for i in range(1, 11, 2):
    print(i)



## Loop Control Statements
## 1) break (stop loop immediately)
 
for i in range(1, 10):
    if i == 5:
        break
    print(i)


## 2) continue (skip current iteration)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


## 3) pass (do nothing)
for i in range(5):
    pass


## For loop with else
# else runs only if the loop finishes normally
# else will not run if loop is terminated by break
for i in range(1, 6):
    print(i)    
else:
    print("Loop completed successfully")    

# output:
# 1
# 2
# 3
# 4
# 5
# Loop completed successfully

for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed successfully")

# output:
# 1
# 2
# (else block not executed because of break)

## Enumerate() function
# adds a counter to an iterable and returns it as an enumerate object
fruits = ["apple", "banana", "mango"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# output:
# 0 apple   
# 1 banana
# 2 mango

