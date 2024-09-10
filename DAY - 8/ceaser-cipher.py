from art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

print(logo)


def encrypt(text, shift):
    cipher_text = ""
    for char in text:
        if char in alphabet:
            pos = (alphabet.index(char) + shift) % 26
            cipher_text += alphabet[pos]
        else:
            cipher_text += char
    print(cipher_text)


def decrypt(text, shift):
    plain_text = ""
    for char in text:
        if char in alphabet:
            pos = (alphabet.index(char) - shift) % 26
            plain_text += alphabet[pos]
        else:
            plain_text += char
    print(plain_text)


should_countinue = True
while should_countinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Please write valid operation")

    flag = input("Type 'yes' to countinue, 'no' to end\n").lower()

    if flag == "yes":
        should_countinue = True
    elif flag == "no":
        should_countinue = False
        print("Thank You...")
    else:
        print("Please enter valid operation")
