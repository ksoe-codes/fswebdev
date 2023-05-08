print("Welcome to Tip Calculator.")
bill = float(input("What was the total bill: "))
tip = int(input("What percentage of tip would you like to give? "))
tip_perc = tip/100
tip_amt = bill * tip_perc

people = int(input("How many people to split the bill? "))

total_amount_perperson = (bill + tip_amt)/people
final_bill_amount = round(total_amount_perperson,2)
print("Each person should pay: " + str(final_bill_amount))