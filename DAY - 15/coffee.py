MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    },
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total = 0


def process_coins():
    print("\nPlease insert coins...\n")
    total = int(input("how many 5 rupee coins: ")) * 5
    total += int(input("how many 10 rupee coins: ")) * 10
    total += int(input("how many 20 rupee coins: ")) * 20
    return total


def is_resource(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"\nSorry there is not enough {item}\n")
            return False
    return True


def is_transaction(money_recived, drink_cost):
    if money_recived >= drink_cost:
        change = money_recived - drink_cost
        global profit
        profit += drink_cost
        if change == 0:
            return True
        print(f"\nMoney refunded: {change}")
        return True
    else:
        print("\nSorry that's not enough. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"\nHere is your {drink_name} ☕\n")


is_on = True
while is_on:
    choice = input("what would you like? (espresso / latte / cappuccino): ")
    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"\nWater: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs.{profit}\n")

    else:
        drink = MENU[choice]
        if is_resource(drink["ingredients"]):
            payment = process_coins()
            if is_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
