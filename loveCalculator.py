print("Welcome to Love Calculator.")
name1 = input("Enter your Name: ")
name2 = input("Enter your lovers Name: ")

name = name1 + name2

t = name1.lower().count("t")
r = name1.lower().count("r")
u = name1.lower().count("u")
e = name1.lower().count("e")
l = name1.lower().count("l")
o = name1.lower().count("o")
v = name1.lower().count("v")
e = name1.lower().count("e")

true = t+r+u+e
love = l+o+v+e

love_score = true + love

print(f"Your Love percentage is {love_score}%")

if love_score < 10 or love_score > 90:
    print("You are like coke and mentos.")
    
elif love_score > 40 and love_score < 50:
    print("You are alright together.")
    
else:
    print("You are made till heaven.")   