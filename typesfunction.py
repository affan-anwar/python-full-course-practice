# # 1. No Input & No Output
# def add():
#     a = 10
#     b = 20
#     print(a + b)

# add()


# # 2. Input & No Output
# def add(a, b):
#     print(a + b)

# add(50, 200)


# # 3. No Input & Output
# def add():
#     a = 100
#     b = 1000
#     return a + b

# res = add()
# print(res)


# # 4. Input & Output
# def add(a, b):
#     c = a + b
#     return c

# print(add(30, 70))


# WAP to Find squares of a number
# 1. No input, no output
def square():
    num = 5
    print(num * num)

square()  # 25


# 2. No input, output (return)
def square():
    num = 10
    return num * num

res = square()
print(res)  # 100


# 3. Input, no output
def square(num):
    print(num * num)

square(100)  # 10000


# 4. Input, output
def square(num):
    return num * num

print(square(1000))  # 1000000



#return multiple expressions
def calculate(a, b):
    return a + b, a - b, a * b

x, y, z = calculate(20, 10)

print("Addition:", x)        # 30
print("Subtraction:", y)     # 10
print("Multiplication:", z)  # 200


print("------------------------------")

#return multiple values
def student():
    return "MD AFFAN ANWAR", 22, "Bangalore"

name, age, city = student()

print("Name:", name)   # MD AFFAN ANWAR
print("Age:", age)     # 22
print("City:", city)   # Bangalore