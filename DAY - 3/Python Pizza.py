print("Welcome to Python Pizza\n")

size = input("select sixze ? S, M, L :\n")
pepperoni = input("Do you want Pepperoni ? Y or N :\n")
cheese = input("Do you want extra cheese ? Y or N :\n")

bill = 0

# Size
if size == "S":
    bill += 15

elif size == "M":
    bill += 20

elif size == "L":
    bill += 25

# Pepperoni
if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 3
    elif size == "L":
        bill += 3

# Cheese
if cheese == "Y":
    bill += 1

print(f"Total Bill = {bill}.")
