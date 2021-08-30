from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(textInput, adjustment, enOrDe):
    endText = ""
    for char in textInput:
        if char not in alphabet:
            endText += char
        if char == " ":
            endText += " "
            continue
        if enOrDe == "encode":
            index = alphabet.index(char) + adjustment
            if index > 25:
                index = index - 26
            endText += alphabet[index]
        elif enOrDe == "decode":
            index = alphabet.index(char) - adjustment
            if index < 0:
                index = index + 26
            endText += alphabet[index]

    print(f"The {direction}d text is {endText}")


again = True

while again:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26

    caesar(text, shift, direction)
    answer = input("Would you like to go again, type 'yes' or 'no'")

    if answer == "yes":
        continue
    elif answer == "no":
        again = False
        print("Goodbye!")
