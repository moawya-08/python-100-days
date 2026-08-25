import sys
import art

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
    "water": 200,
    "milk": 500,
    "coffee": 100,
    "Money": 0,
}

def report(resources):
    for key in resources:
        if key == "water" or key == "milk":
            print(key, ":", resources[key],"ml")
        if key == "coffee":
            print(key, ":", resources[key],"g")
        if key == "Money":
            print(key, ":", "$",resources[key],) 


def check_resources(coffee):
    
    water_required = MENU[coffee]["ingredients"]["water"]
    if coffee != "espresso":
        milk_required = MENU[coffee]["ingredients"]["milk"]
    coffee_required = MENU[coffee]["ingredients"]["coffee"]

    water_left = resources["water"]
    milk_left = resources["milk"]
    coffee_left = resources["coffee"]

    if water_required > water_left:
        print("Sorry there is not enough water.")   
    elif coffee_required > coffee_left:
        print("Sorry there is not enough coffee.")
    elif coffee != "espresso":
        if milk_required > milk_left:
            print("Sorry there is not enough milk.")
        else:
            process_coins()
    else:
        process_coins()

def process_coins():
    print("Please Insert Coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int (input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_money = (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
    transaction(total_money,choice)
    
def transaction(money,coffee):
    if money < MENU[coffee]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    if money > MENU[coffee]["cost"]:
        change = money - MENU[coffee]["cost"]
        print(f"Here is ${change:.2f} dollars in change.")
        profit=MENU[coffee]["cost"]
        resources["Money"]+=profit
        make_coffee(coffee)
        print(f"Here is your {coffee},Enjoy!")
        print(art.coffee)
    elif money == MENU[coffee]["cost"]:
        profit=MENU[coffee]["cost"]
        resources["Money"]+=profit
        make_coffee(coffee)
        print(f"Here is your {coffee},Enjoy!")
        print(art.coffee)
        
def make_coffee(coffee):
    water_required = MENU[coffee]["ingredients"]["water"]
    if coffee != "espresso":
        milk_required = MENU[coffee]["ingredients"]["milk"]
    coffee_required = MENU[coffee]["ingredients"]["coffee"]

    water_left = resources["water"]
    milk_left = resources["milk"]
    coffee_left = resources["coffee"]

    resources["water"] = water_left-water_required
    if coffee != "espresso":
        resources["milk"] =  milk_left-milk_required
    resources["coffee"] = coffee_left-coffee_required
    
machine_running = True
while True:
    
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    
    if choice == "off":
        sys.exit()
    elif choice == "report":
        report(resources)
    elif choice == "espresso":
        check_resources("espresso")
    elif choice == "latte":
        check_resources("latte")
    elif choice == "cappuccino":
        check_resources("cappuccino")
        
      

        