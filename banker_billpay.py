import random
name_string = input("Give the names of people enjoying this delicious meal: ")

split_names = name_string.split(",")
len = len(split_names)
i = random.randint(0,len - 1)

print(f"So today {split_names[i]} will pay the bill")