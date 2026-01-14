marks = int(input("Enter your marks : "))
print("your marks is:", marks)

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# a = 18
# print(a>18)
# print(a==18)
# print(a<18)
# print(a!=18)

# short hand if-else (ternary operator)
age = int(input("Enter your age: "))
status = "Adult" if age >= 18 else "Minor"
print("You are an", status)
