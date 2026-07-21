# function overloading - function with same but different parameters not possible
# Default arguments
def add(a, b, c=0, d=0):
    return a + b + c + d

print(add(10, 20))          # 30
print(add(10, 20, 30))      # 60
print(add(10, 20, 30, 40))  # 100

# varargs, variable number of arguments *args 0...n
def add(*numbers):
    return sum(numbers)

print(add(10, 20))          # 30
print(add(10, 20, 30))      # 60
print(add(10, 20, 30, 40))  # 100