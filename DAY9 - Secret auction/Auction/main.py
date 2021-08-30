from art import logo

# dictionary to store data
bidders = {}

proceed = True
highestBid = 0

print(logo)
while proceed:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    # add to dictionary
    bidders[name] = bid
    moreBidders = (input("Are there other users who want to bid, 'yes' or 'no'? "))

    if moreBidders == "yes":
        continue
    elif moreBidders == "no":
        proceed = False
        for key, value in bidders.items():
            if value > highestBid:
                highestBid = value
        for name, bid in bidders.items():
            if bid == highestBid:
                print(f"{name} wins the auction with a bid of ${bid}")

