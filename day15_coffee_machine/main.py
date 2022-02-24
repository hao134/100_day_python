MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#print(MENU["cappuccino"]["ingredients"]["water"])

def convert_money(quarter, dime, nickel, penny):
    return 0.25 * quarter + 0.1 * dime + 0.05 * nickel + 0.01 * penny

# constants
espresso_water = MENU["espresso"]["ingredients"]["water"]
espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
espresso_cost = MENU["espresso"]["cost"]
latte_water = MENU["latte"]["ingredients"]["water"]
latte_milk = MENU["latte"]["ingredients"]["milk"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]
latte_cost = MENU["latte"]["cost"]
cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
cappuccino_cost = MENU["cappuccino"]["cost"]
resources_water = resources["water"]
resources_milk = resources["milk"]
resources_coffee = resources["coffee"]

def check(coffee):
    if coffee == "espresso":
        if MENU["espresso"]["ingredients"]["water"] > resources["water"]:
            return "water"
        elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
            return "coffee"
        else:
            return "yes"
    elif coffee == "latte":
        if MENU["latte"]["ingredients"]["water"] > resources["water"]:
            return "water"
        elif MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
            return "coffee"
        elif MENU["latte"]["ingredients"]["milk"] > resources["milk"]:
            return "milk"
        else:
            return "yes"
    else:
        if MENU["cappuccino"]["ingredients"]["water"] > resources["water"]:
            return "water"
        elif MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]:
            return "coffee"
        elif MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]:
            return "milk"
        else:
            return "yes"


power = "on"
money = 0
resources["Money"] = money
while power == "on":
    choose = input("What would you like? (espresso/latte/cappuccino):")
    if choose == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${resources['Money']}")
    elif choose == "espresso":
        if check(choose) == "yes":
            resources["water"] -= espresso_water
            resources["coffee"] -= espresso_coffee
            resources["Money"] += espresso_cost
            Quarters = int(input("how many quarters?: "))
            Dimes = int(input("how many dimes?: "))
            Nickles = int(input("how many nickles?: "))
            Pennies = int(input("how many pennies?: "))
            print(f"Here is ${round(convert_money(Quarters, Dimes, Nickles, Pennies) - espresso_cost,2)} in change")
            print(f"Here is your {choose}. Enjoy")
        elif check(choose) == "water":
            print("Sorry there is not enough water")
        else:
            print("Sorry there is not enough Coffee")
    elif choose == "latte":
        if check(choose) == "yes":
            resources["water"] -= latte_water
            resources["coffee"] -= latte_coffee
            resources["milk"] -= latte_milk
            resources["Money"] += latte_cost
            Quarters = int(input("how many quarters?: "))
            Dimes = int(input("how many dimes?: "))
            Nickles = int(input("how many nickles?: "))
            Pennies = int(input("how many pennies?: "))
            print(f"Here is ${round(convert_money(Quarters, Dimes, Nickles, Pennies) - espresso_cost, 2)} in change")
            print(f"Here is your {choose}. Enjoy")
        elif check(choose) == "water":
            print("Sorry there is not enough water")
        elif check(choose) == "coffee":
            print("Sorry there is not enough Coffee")
        else:
            print("Sorry there is not enough Milk")
    elif choose == "cappuccino":
        if check(choose) == "yes":
            resources["water"] -= cappuccino_water
            resources["coffee"] -= cappuccino_coffee
            resources["milk"] -= cappuccino_milk
            resources["Money"] += cappuccino_cost
            Quarters = int(input("how many quarters?: "))
            Dimes = int(input("how many dimes?: "))
            Nickles = int(input("how many nickles?: "))
            Pennies = int(input("how many pennies?: "))
            print(f"Here is ${round(convert_money(Quarters, Dimes, Nickles, Pennies) - espresso_cost, 2)} in change")
            print(f"Here is your {choose}. Enjoy")
        elif check(choose) == "water":
            print("Sorry there is not enough water")
        elif check(choose) == "coffee":
            print("Sorry there is not enough Coffee")
        else:
            print("Sorry there is not enough Milk")


    elif choose == "off":
        power = "off"

    else:
        print("please choose provided services")

