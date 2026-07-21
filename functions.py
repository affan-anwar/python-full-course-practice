# Add 2 numbers
def add():
    a = 10
    b = 20
    c = a + b
    print(f"The sum of {a} + {b} is: {c}")

add()


# WAF to find square of a number
# def square(num):
#     return num ** 2

# print(square(5))

def sqauare():
    num = 10
    print(f"The square of the number is {num * num}")

sqauare()

# WAF to find largest of 3 numbers
# def largest_of_three(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

# print(largest_of_three(10, 20, 15))

def largest():
    a = 10; b = 30; c = 20
    if a >= b and a >=c:
        return a
    elif b >= a and b >=c:
        return b
    else:
        return c
print(largest()) 

# WAF to find cube of a number
# def cube(num):
#     return num ** 3

# print(cube(3))

def cube():
    num = 10
    print(f"The cube of the number is {num * num * num}")


cube()