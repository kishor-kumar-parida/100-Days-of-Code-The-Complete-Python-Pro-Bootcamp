print("Welcome to the TIP Calculator\n")

# Convert input to appropriate numeric types
bill = float(input("What is your bill? \n"))
tip = float(input("What percentage of tip do you want to give? \n"))
no_of_person = int(input("How many people to split the bill? \n"))

# Calculate the total bill per person
total_bill = round((bill + ((tip / 100) * bill)) / no_of_person, 2)

# Print the result
print("Each person should pay: $ " + str(total_bill))
