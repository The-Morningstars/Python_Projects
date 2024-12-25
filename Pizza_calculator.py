print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    price = 15
    if pepperoni == "Y":
        price = price + 2
if size == "M":
    price = 20
    if pepperoni == "Y":
        price = price + 3
if size == "L":
    price = 25
    if pepperoni == "Y":
        price = price + 3
if extra_cheese == "Y":
    price = price + 1

print (f"Your final bill is: ${price}.")
