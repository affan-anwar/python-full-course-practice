str = "I am a \"good\" girl"

print(str)

s1 = "Hello"
print(s1)

str1 = 'I am a "good" girl'
print(str1)

s1 = "Hello"
s1 = s1 + "World"

print(s1)


s1 = "Hello"
print(id(s1))

s1 = s1 + " World"
print(id(s1))


s1 = "Hello"
s2 = s1 + " World"

print(s1, id(s1))
print(s2, id(s2))

s1 = "Python"
s2 = "Python"

print(s1, id(s1))
print(s2, id(s2))
print(s1 == s2)
print(s1 is s2)

s1 = "Python"
s2 = "python"
print(s1, id(s1))
print(s2, id(s2))
print(s1 == s2) 
print(s1 is s2)