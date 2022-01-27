import coffee_maker
import menu
import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_true = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


while is_true:
    options = menu.get_items()
    choice = input(f'What would you like to drink?{options}').lower()
    if choice == 'off':
        is_true = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
