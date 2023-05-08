print("Welcome to python piza delveries: ")
size = input("What size of pizza do you want 'S' , 'M' , 'L' : ")

pepperoni = input("Do you want pepperoni? 'Y' or 'N': ")
extra_cheese = input("Do you want extra cheese? 'Y' or 'N': ")

if size == 'S':
    price = 15
    if pepperoni == 'Y':
        price += 2
    if extra_cheese == 'Y':
        price += 1
    print(f"Your total cost is: ${price}")

elif size == 'M':
    price = 20
    if pepperoni == 'Y':
        price += 3
    if extra_cheese == 'Y':
        price += 1
    print(f"Your total cost is: ${price}")
    
elif size == 'L':
    price = 25
    if pepperoni == 'Y':
        price += 3
    if extra_cheese == 'Y':
        price += 1
    print(f"Your total cost is: ${price}")