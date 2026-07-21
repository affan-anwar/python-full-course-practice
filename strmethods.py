##Inbuild String Methods - Single program
s = " Md Affan Anwar 25 "

print("Original String:", s) # Md Affan Anwar 25

#Case conversion methods
print("Upper Case:", s.upper()) # MD AFFAN ANWAR 25
print("Lower Case:", s.lower()) # md affan anwar 25
print("capitalize:", s.capitalize()) # Md affan anwar 25
print("title:", s.title()) # Md Affan Anwar 25
print("swapcase:", s.swapcase()) # mD aFFAN aNWAR 25

#Searching & counting
print("find('Tech'):", s.find("Tech")) # 10
print("count('a'):", s.count("a")) # 3

#Replace
print("replace('Anwar', 'Sheikh'):", s.replace("Anwar", "Sheikh")) # Md Affan Sheikh 25

#Start & End check
print("startswith('Md'):", s.startswith("Md")) # True
print("endswith('25'):", s.endswith("25")) # True

#Split & Join
words =s.split() # ['Md', 'Affan', 'Anwar', '25']
print("Split:", words) # ['Md', 'Affan', 'Anwar', '25']
print("Join:", "-".join(words)) # Md-Affan-Anwar-25

#Strip spaces
print("Strip():", s.strip()) # Md Affan Anwar 25
print("lstrip():", s.lstrip()) # Md Affan Anwar 25
print("rstrip():", s.rstrip()) # Md Affan Anwar 25

#Checking methods
print("isalpha():", s.isalpha()) # False
print("isdigit():", s.isdigit()) # False
print("isalnum():", s.isalnum()) # False

#Length
print("Length:", len(s)) # 20




# # Inbuilt String Methods – Single Program
# s = "  kodNest Technologies 123  "


# print("Original String:", s) #  kodNest Technologies 123  


# # Case conversion methods
# print("upper():", s.upper()) # KODNEST TECNOLOGIES 123
# print("lower():", s.lower()) #   kodnest technologies 123  
# print("capitalize():", s.capitalize()) #  kodnest technologies 123  
# print("title():", s.title()) #  kodnest Technologies 123  
# print("swapcase():", s.swapcase()) #kODNEST tECHNOLOGIES 123


# # Searching & counting
# print("find('Tech'):", s.find("Tech")) # 10
# print("count('o'):", s.count("o")) #3


# # Replace
# print("replace('123', '2025'):", s.replace("123", "2025"))
# #  kodNest Technologies 2025  


# # Start & End check
# print("startswith('  kod'):", s.startswith("  kod")) #True
# print("endswith('123  '):", s.endswith("123  ")) #True


# # Split & Join
# words = s.split() #["kodnest","Technologies,"123]
# print("split():", words)
# print("join():", "-".join(words)) #  kodNest - Technologies - 123  


# # Strip spaces
# print("strip():", s.strip()) #kodNest Technologies 123
# print("lstrip():", s.lstrip())#kodNest Technologies 123  
# print("rstrip():", s.rstrip())#  kodNest Technologies 123


# # Checking methods
# print("isalpha():", s.isalpha())#false
# print("isdigit():", s.isdigit())#false
# print("isalnum():", s.isalnum())#true


# # Length
# print("Length of string:", len(s)) #28