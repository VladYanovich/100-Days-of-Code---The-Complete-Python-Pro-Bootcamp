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
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
unit_of_measure = {"water": "ml", "milk": "ml", "coffee": "g", "money": "$"}


def resources_check(beverage: str):
    for key in MENU[beverage]["ingredients"]:
        if resources[key] - MENU[beverage]["ingredients"][key] < 0:
            print(f"Not enough {key}")
            return False
        else:
            return True


def resources_change(beverage: str):
    for key in MENU[beverage]["ingredients"]:
        resources[key] = resources[key] - MENU[beverage]["ingredients"][key]


def brew_coffee(beverage: str):
    if beverage.lower() == "report":
        for key in resources:
            if key == "money":
                print(f"{key.capitalize()}: {unit_of_measure[key]}{resources[key]}")
            else:
                print(f"{key.capitalize()}: {resources[key]}{unit_of_measure[key]}")
        return True
    elif beverage == "off":
        return False
    elif not resources_check(beverage):
        return False
    else:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        input_money = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
        if input_money < MENU[beverage]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        elif input_money == MENU[beverage]["cost"]:
            resources_change(beverage)
            print(f"Here is your {beverage}, Enjoy!")
            resources["money"] += MENU[beverage]["cost"]
        else:
            resources_change(beverage)
            change = round(input_money - MENU[beverage]["cost"],2)
            print(f"Here is ${change} dollars in change.")
            print(f"Here is your {beverage}, Enjoy!")
            resources["money"] += MENU[beverage]["cost"]
        return True

while True:
    users_input: str = input("What would you like? (espresso/latte/cappuccino): ")
    if not brew_coffee(users_input):
        break
print("off")
