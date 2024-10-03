import tkinter
import pandas
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}  # Dictionary to hold the current card's data
to_learn = {}  # Dictionary to hold words yet to be learned

# Try loading the 'words_to_learn.csv' file, otherwise load the 'french_words.csv'
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# Function to show the next flashcard
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Cancel any existing timer
    current_card = random.choice(
        to_learn
    )  # Choose a random card from the 'to_learn' list
    # Update canvas items with the new French word
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(
        3000, flip_card
    )  # Set a timer to flip the card after 3 seconds


# Function to flip the flashcard to show the English translation
def flip_card():
    # Update canvas items with the English word
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# Function to handle known words and remove them from the 'to_learn' list
def is_known():
    to_learn.remove(current_card)  # Remove the current card from the 'to_learn' list
    # Save the updated list to 'words_to_learn.csv'
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()  # Show the next card


# Create the main application window
window = tkinter.Tk()
window.title("Learn French Language")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Set the initial flip timer for flipping the card
flip_timer = window.after(3000, func=flip_card)

# Create the canvas for displaying the flashcards
canvas = tkinter.Canvas(width=800, height=526)
# Load front and back images of the flashcards
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_back_img = tkinter.PhotoImage(file="images/card_back.png")
# Display the front image initially
card_background = canvas.create_image(400, 263, image=card_front_img)

# Create text elements on the canvas for the title and word
card_title = canvas.create_text(400, 150, text=" ", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text=" ", font=("Arial", 60, "bold"))

# Configure canvas background and remove border highlighting
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)  # Place canvas on the grid

# Load images for the 'unknown' and 'known' buttons
cross_image = tkinter.PhotoImage(file="images/wrong.png")
unknown_button = tkinter.Button(
    image=cross_image, highlightthickness=0, command=next_card
)
unknown_button.grid(row=1, column=0)  # Place 'unknown' button on the grid

check_image = tkinter.PhotoImage(file="images/right.png")
known_button = tkinter.Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)  # Place 'known' button on the grid

# Show the first card when the program starts
next_card()

# Start the main event loop
window.mainloop()
