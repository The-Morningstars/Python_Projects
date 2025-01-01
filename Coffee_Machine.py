from http.client import responses

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

vending = True

resources_water = 300
resources_milk = 200
resources_coffee = 100
profit = 0

while vending:
    print("WELCOME TO CHONK'S 'COMfee' MACHINE!")
    response = input("What drink do you want? (espresso, cappuccino, or latte)\n").lower()

    if response == "report":
        print(f"water:{resources_water} oz ")
        print(f"milk:{resources_milk} oz")
        print(f"coffee:{resources_coffee} oz")
        print(f"profit:{profit} USD")


    if response == "off":
        print("Machine is now turned off")
        vending = False
    if response in MENU:
        drinks_water = (MENU[response]["ingredients"]["water"])
        drinks_milk = (MENU[response]["ingredients"]["milk"])
        drinks_coffee = (MENU[response]["ingredients"]["coffee"])
        drinks_cost = (MENU[response]["cost"])

        if drinks_water < resources_water and drinks_milk < resources_milk and drinks_coffee < resources_coffee:
            print(f"the drinks cost is {drinks_cost} USD")
            print("please insert coins")
            quarter_amount = int(input("how many quarters?"))
            dime_amount = int(input("how many dimes?"))
            nickel_amount =int(input("how many nickles?"))
            penny_amount = int(input("how many pennies?"))

            money = float(quarter_amount) * .25 + float(dime_amount) * .10 + float(nickel_amount) * .05 + float(penny_amount) * .01
            change = round(money - drinks_cost,2)
            if money >= drinks_cost:
                print(f"here is your {change} USD")
                print(f"you paid with {money} USD")
                print(f"Here is your {response}. ENJOY!!!")
            else:
                    print("not enough $monies$")
                    vending = False
            resources_water = resources_water - drinks_water
            resources_milk -= drinks_milk
            resources_coffee -= drinks_coffee
            profit = profit + drinks_cost

        else:
            print("Sorry, machine is running low on water,milk, and/or coffee")
            vending = False

