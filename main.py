from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    choice = input(f"what would you like? ({menu.get_items()})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        order = menu.find_drink(choice)
        if order is not None:
            if coffee_maker.is_resource_sufficient(order):
                if money_machine.make_payment(order.cost):
                    coffee_maker.make_coffee(order)










