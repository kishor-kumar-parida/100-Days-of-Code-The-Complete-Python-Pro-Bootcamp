import random  # Importing the random module to generate random numbers
from art import logo


# Function to select the difficulty level
def set_difficulty():
    level = input(
        "Choose difficulty 'easy' or 'hard': "
    )  # Asking user for difficulty level
    if level == "easy":
        return 10  # If easy, the user gets 10 attempts
    else:
        return 5  # If hard, the user gets 5 attempts


# Function to check the guess against the actual answer
def check_guess(guess, answer, turns_left):
    if guess == answer:
        print(f"Congratulations! You guessed it right. The answer was {answer}.")
        return 0  # Return 0 to indicate the game is won
    elif guess > answer:
        print("Your guess is too high.")
        return turns_left - 1  # Decrease attempts by 1 if the guess is too high
    else:
        print("Your guess is too low.")
        return turns_left - 1  # Decrease attempts by 1 if the guess is too low


# Main game function
print(logo)


def game():
    print("Welcome to the Guess the Number Game!")  # Game welcome message
    print("Guess a number between 1 and 100.\n")  # Instructions for the game

    answer = random.randint(1, 100)  # Randomly selecting the number to guess
    turns_left = set_difficulty()  # Get the number of attempts based on difficulty

    guess = 0  # Initializing the user's guess to 0
    # Repeat the game while the user hasn't guessed the correct number and still has attempts left
    while guess != answer and turns_left > 0:
        print(
            f"You have {turns_left} attempts remaining."
        )  # Display remaining attempts
        guess = int(input("Make a guess: "))  # Ask the user to guess a number

        # Check the user's guess and update the number of attempts
        turns_left = check_guess(guess, answer, turns_left)

        # If no attempts are left and the user didn't guess the answer, they lose
        if turns_left == 0 and guess != answer:
            print(
                f"Sorry, you've run out of attempts! The correct answer was {answer}."
            )


# Start the game
game()
