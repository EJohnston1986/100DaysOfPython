from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True    # machine on/off
coffee_maker_obj = CoffeeMaker()
menu_obj = Menu()
money_machine_obj = MoneyMachine()

while is_on:
    options = menu_obj.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False;
    elif choice == "report":
        money_machine_obj.report()
        coffee_maker_obj.report()
    else:
        drink = menu_obj.find_drink(choice)
        if coffee_maker_obj.is_resource_sufficient(drink):
            if money_machine_obj.make_payment(drink.cost):
                coffee_maker_obj.make_coffee(drink)









