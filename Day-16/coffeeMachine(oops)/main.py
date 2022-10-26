from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True

moneyManage = MoneyMachine()
coffeeMaker = CoffeeMaker()
menu = Menu()


while machine_on:
  user_input = input(f"What would you like? ({menu.get_items()}): ")
  
  if user_input == 'report':
    coffeeMaker.report()
    print("")
    moneyManage.report()
    print("")

  elif user_input == 'off':
    machine_on = False

  else:
    item = menu.find_drink(user_input)
    if coffeeMaker.is_resource_sufficient(item):
      payment = moneyManage.make_payment(item.cost)
    if payment == True:
      coffeeMaker.make_coffee(item)