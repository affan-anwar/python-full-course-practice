# STRING SLICING PRACTICE
text = "kodnest"
print(text[2:2]) #' '

print("Original String:", text)
print("----------------------------------------")

# POSITIVE INDEX SLICING
print("Q1:", text[0:4]) #kodn
print("Q2:", text[1:5]) #odne
print("Q3:", text[2:7]) #dnest
print("Q4:", text[3:6])  #nes
print("Q5:", text[4:7]) #est

# NEGATIVE INDEX SLICING
print("Q6:", text[-4:-1]) #nes
print("Q7:", text[-7:-3]) #kodn
print("Q8:", text[-5:-2]) #dne
print("Q9:", text[-6:-4]) #od
print("Q10:", text[-3:-1]) #es

# EDGE CASES
print("Q16:", text[2:2]) # Empty string
print("Q17:", text[5:3]) # Empty string
print("Q18:", text[10:15]) # Empty string

print("----------------------------------------")

# String Slicing Questions on "KODNEST"

s = "KODNEST"

print(s[0:4]) #KODN
print(s[2:7]) #DNEST
print(s[:5]) #KODNE
print(s[3:7]) #DNEST
print(s[-4]) #N

print(s[0:7:2]) #
print(s[1:6:2]) #ons
print(s[::3]) #Knt
print(s[2:7:3]) #ds
print(s[5:7:1]) #st

print(s[6:0:-1]) #TSEDN
print(s[::-1]) #TSEDNOK
print(s[5:1:-2]) #sn
print(s[4:0:-1]) #endo

print(s[3:6:-1]) #E
print(s[1:5:-1]) #E
print(s[0:7:-1]) #K
print(s[3::-1]) #DOK