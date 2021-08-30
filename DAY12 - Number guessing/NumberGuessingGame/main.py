import random


def random_number():
    return random.randint(1, 101)


game_finished = False
answer = random_number()


def set_num_lives(level):
    if level == "easy":
        return 10
    elif level == "hard":
        return 5


def check_guess(number):
    global answer
    global num_lives
    if number == answer:
        print("This is the correct answer, well done")
        return True
    elif number < answer:
        print("Too low")
        num_lives -= 1
        return False
    elif number > answer:
        print("Too high")
        num_lives -= 1
        return False


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

num_lives = set_num_lives(difficulty)

while not game_finished:
    print(f"You have {num_lives} attempts remaining to guess the answer")
    guess = int(input("Make a guess:"))
    game_finished = check_guess(guess)

    if num_lives == 0:
        print(f"Game over, the correct answer was {answer}")
        game_finished = True
