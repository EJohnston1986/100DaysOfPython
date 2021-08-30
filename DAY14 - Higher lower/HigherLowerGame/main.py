from art import logo
from art import vs
from game_data import data
import random


# selects insta account from the list of dictionaries
def select_account():
    return random.choice(data)


# checks if two randomly selected accounts are the same
def compare_account(account1, account2):
    if account1 == account2:
        return True
    else:
        return False


def check_guess(attempt, account1, account2):
    global final_score
    if attempt == "A" and account1['follower_count'] > account2['follower_count']:
        final_score += 1
        print(f"You're right! Current score: {final_score}\n")
        return True
    elif attempt == "A" and account1['follower_count'] < account2['follower_count']:
        print(f"Sorry, that's wrong. Final score: {final_score}")
        return False
    elif attempt == "B" and account1['follower_count'] > account2['follower_count']:
        print(f"Sorry, that's wrong. Final score: {final_score}")
        return False
    elif attempt == "B" and account1[1] < account2[1]:
        final_score += 1
        print(f"You're right! Current score: {final_score}\n")
        return True


gameContinue = True  # for entering the game while loop
final_score = 0      # for tracking the users score

print(logo)          # printing the opening logo

# while loop that executes while the users guess is correct
while gameContinue:
    accountSame = True
    accountA = select_account()     # assign first account for guessing
    accountB = select_account()     # assign second account for guessing

    # Make sure accounts for comparing are not the same
    while accountSame:
        accountSame = compare_account(accountA, accountB)
        if accountSame:
            accountB = select_account()

    # printing output to screen for user to choose
    print(f"Compare A: {accountA['name']}, {accountA['description']}, from {accountA['country']}.")
    print(vs)
    print(f"Compare B: {accountB['name']}, {accountB['description']}, from {accountB['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ")

    gameContinue = check_guess(guess, accountA, accountB)
