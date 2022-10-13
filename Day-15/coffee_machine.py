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

refill_resources = {
    "water": 0,
    "milk": 0,
    "coffee": 0,
}

#To check the resource are in enough quantity to process the customer's request
def check_resources(user_input):
    ingredients = MENU[user_input]['ingredients']
    availability = True
    for item in ingredients:
        if resources[item] >= ingredients[item]:
            availability = True
        else:
            availability = False
            return availability
    return availability

#To process the coins customer has inserted in regards to the requested drink
def process_coins(user_money,user_input):
    choice = user_input
    change = 0
    cost = MENU[choice]['cost']

    if choice == 'latte' or choice == 'cappuccino' or choice == 'espresso':
        if user_money > cost:
            change = round(user_money - cost,2)
            return f"Thanks for your time. Here's your ${change} change"
        elif user_money == cost:
            return "Thanks for your time."
        elif user_money < cost:
            return "Sorry, insufficient amount. We can't process your request."

#Processing the resources after fulfilling the user's request
def process_resources(user_input):
    ingredients = MENU[user_input]['ingredients']
    for item in ingredients:
        resources[item] = resources[item] - ingredients[item]

#In case the resources are not enough, we can use fill up the required amounts of resources
def refill(refill_resources):
    for item in refill_resources:
        resources[item] = resources[item] + refill_resources[item]

machine_on = True

while machine_on == True:
    
    user_money = 0
    
    # user input to run the machine. 'refill' and 'report' keywords are for machine admin.
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if user_input == 'off':
        machine_on = False
        print('Thank You!!')
    
    elif user_input == 'report':
        print(f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']}")
    
    elif user_input == 'refill':
        for item in refill_resources:
            refill_resources[item] += int(input(f"How much {item} would you like to refill?: ")) 
        refill(refill_resources)
        print("OK! The resources are filled in.")
    
    else:
        print("Please insert coins.")
        user_money += int(input("how many quarters?: "))*0.25
        user_money += int(input("how many dimes?: "))*0.10
        user_money += int(input("how many nickles?: "))*0.05
        user_money += int(input("how many pennies?: "))*0.01

        #using availability variable, we'll run the below if-else
        availability = check_resources(user_input)

        if availability == True:
            bill = process_coins(user_money,user_input)
            print(bill)
            process_resources(user_input)

        else:
            print(f'Sorry, At the monment we\'re not giving out {user_input}.')
            if user_money>0:
                print(f"Here's your refund of ${user_money}")
        