print("Welcome to treasure island,\nYour mission is to find the treasure.")
print("\n\nWhere do you wanna go")
choice1 = input("\nLeft or Right: ").lower()

if choice1 == "right":
    print("\nGame Over!!!")
    exit()
else:
    print("\n\nYou chose to go LEFT")
    
print("\n\nWhat do you wanna do:")
choice2 = input("\nSwim or Wait: ").lower()

if choice2 == "wait":
    print("\nGame Over!!!")
    exit()
else:
    print("\n\nYou chose to SWIM")

print("\nChoose which door you think the treasure is: ")
choice3 = input("\n1.Red\n2.Blue\n3.Yellow\n\n").lower()

if choice3 == "yellow":
    print("\nYOU WON!!!")
    exit()
else:
    print("\nGame Over")
