a = [1, 2, 3]  # separate list
b = a
c = [1, 2, 3]

# is  => checks memory address
# ==  => checks content/value

print(a is b)
print(a is c)
print(a == c)

s1 = " "
res = bool(s1)

print(res)
print(type(res))