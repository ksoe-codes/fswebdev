print("Welcome to Tip Calculator.")
bill = int(input("What was the total bill: "))
tip = input("What percentage of tip would you like to give? ")
tip_int = int(tip)/100
tip_amt = bill * tip_int

people = int(input("How many people to split the bill? "))

total_amount_perperson = (bill + tip_amt)/people

print("Each person should pay: " + str(total_amount_perperson))