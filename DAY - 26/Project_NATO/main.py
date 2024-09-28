# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# 1. Create a dictionary in this format:

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# print(phonetic_dict)

# 2. Create a list of the phonetic code words from a word that the user inputs.


def generatePhonetic():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("Please enter a word of Letters")
        generatePhonetic()

    else:
        print(output_list)


generatePhonetic()
