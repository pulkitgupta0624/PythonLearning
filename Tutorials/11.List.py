## A list is a collection that can store multiple values in one variable.
## It is ordered, mutable and allow duplicate values

fruits = ["apple", "banana", "mango"]
print(fruits)

## 1) Creating Lists
nums = [10, 20, 30, 40, 50]
name = ["Pulkit", "Puki", "Bro"]
mix = [1, "hello", 3.5, True]

## 2) Accessing List Elements (Indexing)
names = ["Pulkit", "Rahul", "Aman"]

print(names[0])   # Pulkit
print(names[2])   # Aman
print(names[-1])  # Aman (last element) 

## 3) Slicing in List
print(nums[0:3])  # [10, 20, 30]
print(nums[2:])   # [30, 40, 50]
print(nums[:4])   # [10, 20, 30, 40]
print(nums[0:5:2]) # [10, 30, 50]

## 4) Changing List Items (Mutable)
nums[1] = 99
print(nums)  # [10, 99, 30]


## 5) Adding Elements to List
# append() → adds at end
nums.append(60)
print(nums)

# insert() → adds at specific index
nums.insert(1, 10)
print(nums)

## 6) Removing Elements
# remove() → remove by value
nums.remove(30)
print(nums)

# pop() → remove by index
nums.pop(1)
print(nums) 

# clear() → removes all elements
nums.clear()
print(nums)


## 7) List Length
numbers = [1,2,3,4,5,6]
print(len(numbers))


## 8) Looping in List
# for loop
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

# while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

## 10) Sorting in List
eles = [4,1,8,2,7,9,3]
eles.sort()
print(eles)
eles.sort(reverse=True)
print(eles)

## 11) List Comprehension
square = [x*x for x in range(1, 6)]
print(square)


## 12) Concatinate two lists
m = [10,20,30]
n = [100,200,300]
k = m+n
print(k)