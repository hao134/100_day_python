from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

# CoffeeMaker().report()
# MoneyMachine().report()
# print(Menu().get_items())
# drink = Menu().find_drink("latte")
# print(drink.cost)
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        CoffeeMaker().report()
        MoneyMachine().report()
    else:
        drink = Menu().find_drink(choice)
        if CoffeeMaker().is_resource_sufficient(drink):
            if MoneyMachine().make_payment(drink.cost):
                CoffeeMaker().make_coffee(drink)

# this code has some problems, see solution code to figulize where the faults.

