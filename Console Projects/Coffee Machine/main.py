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
def sufficiency(flavour):
    if flavour == "espresso":
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            return True
    elif flavour == "latte":
        if resources["water"] >= 200 and resources["coffee"] >= 24 and resources["milk"] >= 150:
            return True
    elif flavour == "capuccino":
        if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100:
            return True
    else:
        print("insufficient resources")
        return False
def transaction_success (coins):
    if coffee_type == "espresso":
        if coins >= 1.50:
            return True
        else:
            print("transaction unsuccessful")
            return False
    if coffee_type == "latte":
        if coins >= 2.00:
            return True
        else:
            print("transaction unsuccessful")
            return False
    if coffee_type == "capuccino":
        if coins >= 3.00:
            return True
        else:
            print("transaction unsuccessful")
            return False
def deduct(flavour):
    if flavour == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
    if flavour == "latte":
        resources["water"] -= 200
        resources["coffee"] -= 24
        resources["milk"] -= 150
    if flavour == "capuccino":
        resources["water"] -= 250
        resources["coffee"] -= 24
        resources["milk"] -= 100

# coffee_emoji = ☕
#TODO: Three hot flavours
#todo: coin operated, penny = 1 cent, nickel = 5, dime = 10, quarter = 25
#todo: print report
money = 0

coffee_type = input("what would you like? (espresso/latte/capuccino): ")
if coffee_type == "report":
    print(f"Resources are water: {resources['water']}, \nmilk: {resources['milk']}, and coffee: {resources['coffee']} ")
if sufficiency(coffee_type) is True:
    print("Please insert coins.")
    quarters = int(input ("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    quarters_in_dollars = quarters * 0.25
    dimes_in_dollars = dimes * 0.10
    nickels_in_dollars = nickels * 0.05
    pennies_in_dollars = pennies * 0.01
    total_in_dollars = quarters_in_dollars + dimes_in_dollars + nickels_in_dollars + pennies_in_dollars

# todo: check resources sufficiency
if transaction_success(total_in_dollars):
    print("here's your coffee:☕ ")
    deduct(coffee_type)
    print(f"Resources are water: {resources['water']}, \nmilk: {resources['milk']}, and coffee: {resources['coffee']} ")


# todo: process coins
# todo: check transaction successful
# todo: Make coffee, deducting
