import random
from hangmanWords import word_list
from hangmanArt import logo, stages

# Displaying game intro logo
print(f"{logo}\n\n")

# choosing random word from list for game
index = random.randint(0, (len(word_list)))
chosenWord = word_list[index]
# or we can use chosenWord = random.choice(word_list)

# declaring variables for game
endOfGame = False
lives = 6
guesses = []

# creating list for chosen word, built with underscores initially
display = []
for letter in chosenWord:
    display.append("_")

print(*display)

# loop for users guesses of letters
while not endOfGame:
    guess = input("Guess a letter: ").lower()

    # check if letter has already been guessed
    while guess in guesses:
        print(f"You have already guessed {guess}")
        guess = input("Guess a letter: ").lower()

    guesses.append(guess)  # add guess to list

    # checking if guess is correct
    for index in range(0, len(chosenWord)):
        if guess == chosenWord[index]:
            display[index] = guess

    print(stages[lives])
    print(*display)

    # wrong guess, lose a life or game over
    if guess not in chosenWord:
        lives -= 1
        print(f"Your guess is incorrect, you have {lives} lives remaining")
        print(stages[lives])
        if lives == 0:
            print(f"Game over, the correct answer was {chosenWord}")
            endOfGame = True

    # game is complete, player wins. exit loop
    if "_" not in display:
        print("You win.")
        endOfGame = True
