from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
comp_cards = []


# function to add players first two cards to their list
def first_two_cards(blackjack):
    for card in range(2):
        player_cards.append(cards[random.randint(0, len(cards) - 1)])
    user_score = player_cards[0] + player_cards[1]
    if user_score == 21 and 11 in player_cards:
        print("You have blackjack!")
        return True
    print(f"Your cards: {*player_cards,}, current score {user_score}")
    return False


# function for player to add new cards to their list
def deal_player_card():
    player_cards.append(cards[random.randint(0, len(cards) - 1)])
    score = sum(player_cards)
    if score > 21:
        for num in range(len(player_cards)):
            if player_cards[num] == 11:  # checking if ace in hand, change to lower value if bust
                player_cards[num] = 1
                score = score - 10
    print(f"\nYour cards: {*player_cards,}, current score: {score}")
    return score


# function to add computers first two cards
def comp_card():
    for card in range(2):
        comp_cards.append(cards[random.randint(0, len(cards) - 1)])
    return f"Computers first card {comp_cards[0]}"


def deal_comp_card():
    comp_cards.append(cards[random.randint(0, len(cards) - 1)])
    score = sum(comp_cards)
    if score > 21:
        for num in range(len(comp_cards)):
            if comp_cards[num] == 11:  # checking if ace in hand, change to lower value if bust
                comp_cards[num] = 1
                score = score - 10
    print(f"Computers cards: {*comp_cards,}, score is {score}\n")
    return score


# main function from where game operates
def game():
    print(logo)
    global player_cards, comp_cards
    player_blackjack = False
    hit_player = True
    player_score = 0
    comp_score = 0

    player_blackjack = (first_two_cards(player_blackjack))  # users first cards
    print(comp_card())                                      # computers first card

    # update player score after two cards
    player_score = sum(player_cards)

    # loop will call function to add more player cards until false
    while hit_player:
        hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit_me == 'y':
            player_score = deal_player_card()
            if player_score > 21:
                print("You're Bust!")
                break

        # Computer player now selects its cards
        elif hit_me == 'n':
            comp_score = sum(comp_cards)
            print(f"Computers second card is {comp_cards[1]}, it's score is {comp_score}")
            if comp_score == 21 and 11 in comp_cards:
                print("Computer has blackjack, you lose!")
                break
            while comp_score < 17:
                comp_score = deal_comp_card()
                if comp_score < 17:
                    print(f"The computers score is {comp_score}, it will take another card")

            print(f"\nYour final hand: {*player_cards,}, final score {player_score} ")
            print(f"Computer's final hand {*comp_cards,}, final score {comp_score} ")
            if comp_score < player_score < 22:
                print("You win!\n")
            elif player_score < comp_score < 22:
                print("You lose!\n")
            elif player_score == comp_score:
                print("It's a draw!\n")
            elif comp_score > 21:
                print("Computer is bust, you win!\n")
            hit_player = False

    # asking user if they want to play another game
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n'")
    if play_again == 'y':
        player_cards.clear()
        comp_cards.clear()
        game()
    elif play_again == 'n':
        print("Goodbye")


game()
