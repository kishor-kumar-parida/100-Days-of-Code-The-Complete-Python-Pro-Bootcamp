import random
import os

from art import logo
from art import vs
from game_data import data


def clear():
    os.system("cls" if os.name == "nt" else "clear")


# use if statement to check if user is correct
def check_answer(guess, a_count, b_count):
    if a_count > b_count:
        return guess == "a"
    else:
        return guess == "b"


# Format the account data into printable format
def format_data(account):
    account_name = account["name"]
    account_des = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_des}, from {account_country}"


# Display art
print(logo)

# Score
score = 0

# choose account b
account_b = random.choice(data)

# Make game repetable
game_continue = True
while game_continue:
    # Generate a random account from game data
    # Making account at postion B become the next account at postion A

    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    # Format the account data into printable format

    data_a = format_data(account_a)
    data_b = format_data(account_b)
    print(f"Compare A: {data_a}.")
    print(vs)
    print(f"Against B: {data_b}.")

    # ask user for guess

    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    ## check is user is correct
    # Get follower count of each account

    a_count = account_a["follower_count"]
    b_count = account_b["follower_count"]

    # use if statement to check if user is correct

    is_correct = check_answer(guess, a_count, b_count)

    clear()
    print(logo)

    # Provide feedback and track score

    if is_correct:
        score += 1
        print(f"You are right! current score: {score}\n")
    else:
        game_continue = False
        clear()
        print(f"Sorry, that's wrong. Your Final Score is : {score}")
