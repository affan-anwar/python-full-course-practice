# Take Name Input
name = input("Enter the name: ")
print(name)

print("---------------")

# Take Name and Age Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"{name} is a Python student")
print(f"{name}'s age is {age}")

print("---------------")

# WAP to Add Two Numbers
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

result = num1 + num2

print("The sum is:", result)

print("---------------")

# Create a Complex Number
real = float(input("Enter the real part: "))
imag = float(input("Enter the imaginary part: "))

num = complex(real, imag)

print("Complex Number:", num)
print("Type:", type(num))

print("---------------")

# Find the Area of a Rectangle
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print("Area of Rectangle =", area)

print("---------------")

# Check Whether a Student Is Placed
status = input("Enter placement status (placed/not placed): ")

placed = status.strip().lower() == "placed"

print("Placed:", placed)
print("Type:", type(placed))