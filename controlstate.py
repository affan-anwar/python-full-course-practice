#Selection Statements
#if
age = 10
if age >= 18:
    print("Eligible to vote")

    print("Thank you")

#elif
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")
print("Thank you")

#elif ladder (if-elif-else)
marks = 40
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("fail")

#nested if
free_tonight = True
friends_available = False
if free_tonight:
    if friends_available:
        print("Go out for party")
    else:
        print("Order food online")
else:
    print("Continue with work")

#match
day = 4
match day:
    case 1: print("Mon")
    case 2: print("Tue")
    case 3: print("Wed")
    case 4: print("Thu")
    case 5: print("Fri")
    case _: print("Invalid day")

#case 3,4,5-summer, 6,7,8-rainy, 9,10,11-autumn, 12,1,2-winter
month = 12
match month:
    case 3 | 4 | 5:
        print("Summer")
    case 6 | 7 | 8:
        print("Rainy")
    case 9 | 10 | 11:
        print("Autumn")
    case 12 | 1 | 2:
        print("Winter")
    case _:
        print("Invalid month")
        