from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

make_coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino/): ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        make_coffee.report()
        money.report()
    else:
        drink = menu.find_drink(user_input)
        if make_coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            make_coffee.make_coffee(drink)


