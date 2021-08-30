# This program will create a password for you of a set length initialised with random characters

import random

# lists of character types to be used
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")

numLetters = int(input("How many letters would you like in your password?\n"))
numSymbols = int(input("How many symbols would you like?\n"))
numNumbers = int(input("How many numbers would you like?\n"))

password = []

for letter in range(0, numLetters):
    randLetter = random.randrange(0, 25)
    password.append(letters[randLetter])

for number in range(0, numNumbers):
    randNum = random.randrange(0, 10)
    password.append(numbers[randNum])

for symbol in range(0, numSymbols):
    randSymbol = random.randrange(0, 9)
    password.append(symbols[randSymbol])

random.shuffle(password)
finalPass = ""
print("Your password is: ")
for char in password:
    finalPass += char

print(finalPass)