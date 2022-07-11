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


def is_resources_suff(order_ingredients):
    """Return true when ingredients is sufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Total inserted coins"""
    print("Please insert coins.")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickles?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total


def is_transaction_success(money_received, drink_cost):
    """return true when payment is accepted"""
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """deduct ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕")


profit = 0
is_on = True
while is_on:
    choose = input('What would you like? (espresso/latte/cappuccino):').lower()
    if choose == "off":
        is_on = False
    elif choose == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choose]
        if is_resources_suff(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_success(payment, drink["cost"]):
                make_coffee(choose, drink["ingredients"])
