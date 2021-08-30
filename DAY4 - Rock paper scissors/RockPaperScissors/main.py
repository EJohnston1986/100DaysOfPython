import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to rock, paper, scissors\n\n\n")
userSelection = int(input("Please select 1 for rock, 2 for paper or 3 for scissors "))
compSelection = random.randint(1, 3)

if userSelection == 1:
    print("You chose\n")
    print(rock)
    if compSelection == 1:
        print("Computer chose\n")
        print(rock)
        print("\nYou draw")
    elif compSelection == 2:
        print("Computer chose\n")
        print(paper)
        print("\nYou lose")
    elif compSelection == 3:
        print("Computer chose\n")
        print(scissors)
        print("\nYou win")
if userSelection == 2:
    print("You chose\n")
    print(paper)
    if compSelection == 1:
        print("Computer chose\n")
        print(rock)
        print("\nYou win")
    elif compSelection == 2:
        print("Computer chose\n")
        print(paper)
        print("\nYou draw")
    elif compSelection == 3:
        print("Computer chose\n")
        print(scissors)
        print("\nYou lose")
if userSelection == 3:
    print("You chose\n")
    print(scissors)
    if compSelection == 1:
        print("Computer chose\n")
        print(rock)
        print("\nYou lose")
    elif compSelection == 2:
        print("Computer chose\n")
        print(paper)
        print("\nYou win")
    elif compSelection == 3:
        print("Computer chose\n")
        print(scissors)
        print("\nYou draw")
else:
    print("Invalid entry, you lose")