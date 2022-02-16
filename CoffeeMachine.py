from CoffeeMachineData import MENU, resources

menu = MENU

"""
I have a dictionary with the given information for the different types of Coffee, and the resources
that are currently in the coffee machine.

The goal is to prompt the user for what type of coffee they would like, then ask them for how many of
each coin they would like to insert.  

if there is not enough resources, or they have not given enough money, the user would be prompted again.

Functions:
    check_resources(drink_chosen, resources)
        this function will return true if there are sufficient resources available
        for the chosen drink
    order(boolean value)
        continues prompting the user for a drink until they don't want one, or
        there are not enough resources to continue.
    subtract_resources(drink_chosen, resources)
        this function will subtract the resources based on the coffee made
    keep_ordering()
        prompts the user if they wish to order again, and returns a boolean based on their answer
"""

def keep_ordering():
    keep_ordering = input("Do you wish to continue ordering? (Y/N)\n").lower()

    if keep_ordering == 'y':
        return True
    elif keep_ordering == 'n':
        return False
    else:
        print("You have entered an invalid value.")
        return False


def subtract_resources(drink_chosen, resources_input):
    resources_input['water'] -= drink_chosen['ingredients']['water']
    resources_input['milk'] -= drink_chosen['ingredients']['milk']
    resources_input['coffee'] -= drink_chosen['ingredients']['coffee']


def check_resources(drink_chosen, resources_input):
    if drink_chosen['ingredients']['water'] > resources_input['water']:
        return False
    if drink_chosen['ingredients']['milk'] > resources_input['milk']:
        return False
    if drink_chosen['ingredients']['coffee'] > resources_input['coffee']:
        return False
    return True


def order(continue_order):
    if continue_order:
        print("Welcome to the Coffee Machine.")

        # Collects user choice of drink
        drink_choice = input("Choose your drink (latte/cappuccino/espresso)\n").lower()

        # makes a variable for the amount needed to pay
        payment = menu[drink_choice]['cost']

        if check_resources(menu[drink_choice], resources):

            # changes the resources dependent on the user input
            subtract_resources(menu[drink_choice], resources)

            # prompts the user for their money
            quarters_entered = int(input("How many quarters? (number value please)\n"))
            dimes_entered = int(input("How many dimes? (number value please)\n"))
            nickels_entered = int(input("How many nickels? (number value please)\n"))
            pennies_entered = int(input("How many pennies? (number value please)\n"))

            # converts the money entered into UDS value
            quarters_entered *= .25
            dimes_entered *= .1
            nickels_entered *= .05
            pennies_entered *= .01

            # sum of money payed
            total_money_inserted = quarters_entered + dimes_entered + nickels_entered + pennies_entered

            # checks if money entered enough
            if total_money_inserted >= payment:

                # gets user change
                change = float(total_money_inserted - payment)
                formatted_change = '{0:.2f}'.format(change)

                print(f"Here is ${formatted_change} in change\n"
                      f"enjoy your {drink_choice}!")

                order(keep_ordering())
            else:
                print("You have not payed enough.")
                order(keep_ordering())
        else:
            print(f"There are not enough resources to make a {drink_choice}.")
            order(keep_ordering())
    else:
        pass


order(True)
