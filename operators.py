# Program to Explain Python Operators

print("------ Arithmetic Operators ------")
a = 10
b = 3

print("Addition:", a + b)              # 13
print("Subtraction:", a - b)           # 7
print("Multiplication:", a * b)        # 30
print("Division:", a / b)              # 3.333
print("Floor Division:", a // b)       # 3
print("Modulus:", a % b)               # 1
print("Power:", a ** b)                # 1000

print("\n------ Comparison Operators ------")
x = 5
y = 10

print("x > y :", x > y)                # False
print("x < y :", x < y)                # True
print("x == y :", x == y)              # False
print("5 == 5")                        # True
print("x != y :", x != y)              # True
print("x >= y :", x >= y)              # False
print("x <= y :", x <= y)              # True

print("\n------ Logical Operators ------")
p = True
q = False

print("p and q :", p and q)            # False
print("p or q :", p or q)              # True
print("not p :", not p)                # False

print("\n------ Assignment Operators ------")
num = 10

print("Initial value:", num)           # 10

num += 5
print("After += :", num)               # num = num + 5 = 15

num -= 3
print("After -= :", num)               # num = 15 - 3 = 12

num *= 2
print("After *= :", num)               # num = 12 * 2 = 24

num //= 4
print("After //= :", num)              # num = 24 // 4 = 6

print("\n------ Identity Operators - Content address t/f ------")
a = 5
b = a
c = 10

print("a is b :", a is b)              # True
print("a is c :", a is c)              # False
print("a is not c :", a is not c)      # True

print("\n------ Membership Operators t/f ------")
numbers = [1, 2, 3, 4, 5, 4.5]

print("3 in list :", 3 in numbers)             # True
print("10 in list :", 10 in numbers)           # False
print("4.5 not in list :", 4.5 not in numbers) # False

print("\n------ Bitwise Operators ------")
a = 5
b = 3

print(a & b)     # 1
print(a | b)     # 7
print(a ^ b)     # 6
print(~a)        # -6
print(~b)        # -4

print("\n------ Shift Operators ------")
print(5 << 1)    # 10
print(5 >> 1)    # 2
print(5 >> 2)    # 1
print(7 << 3)    # 56
print(7 >> 3)    # 0