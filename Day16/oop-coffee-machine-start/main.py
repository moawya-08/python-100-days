from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
drink = Menu()
money = MoneyMachine()  
# order = MenuItem(name=,)

is_on =True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/):")
    order = drink.find_drink(choice)
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        order = drink.find_drink(choice)
        if coffee.is_resource_sufficient(order):
            if money.make_payment(order.cost):
                coffee.make_coffee(order)
            

        