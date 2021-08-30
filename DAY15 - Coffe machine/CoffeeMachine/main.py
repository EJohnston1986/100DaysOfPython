from data import MENU
from data import resources

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def machine_off():
    print("\nThe coffee machine is being turned off, goodbye!")
    quit()


def check_resources(drink):
    water_res = MENU[drink]["water"]
    milk_res = MENU[drink]["milk"]
    coffee_res = MENU[drink]["coffee"]

    if drink["water"] < water_res:
        print("Sorry, there is not enough water.")
    elif drink["milk"] < milk_res:
        print("Sorry, there is not enough milk.")
    elif drink["coffee"] < coffee_res:
        print("Sorry, there is not enough coffee")


def process_coins():
    quarters = int(input("How many quarters ($0.25) do you want to enter? "))
    dimes = int(input("How many dimes ($0.10) do you want to enter? "))
    nickels = int(input("How many nickels ($0.05) do you want to enter? "))
    pennies = int(input("How many pennies ($0.01) do you want to enter? "))

    tot_quarters = quarters * 0.25
    tot_dimes = dimes * 0.10
    tot_nickels = nickels * 0.05
    tot_pennies = pennies * 0.01

    tot_money = tot_pennies + tot_nickels + tot_dimes + tot_quarters
    resources["money"] = tot_money


# def check_transaction():



# TODO Prompt user by asking what would you like?
order = input("What would you like? (espresso/latte/cappuccino):")

while order != "espresso" and order != "latte" and order != "cappuccino":
    if order == "off":
        machine_off()
    elif order == "report":
        print_report()
    else:
        print("not a valid option")
    order = input("What would you like? (espresso/latte/cappuccino):")

print(f"You have selected {order}")
check_resources(order)
check_transaction()


# TODO turn off the coffee machine by entering off at the prompt
# TODO print report
# TODO check resource sufficient
# TODO process coins
# TODO check transaction successful
# TODO make coffee
