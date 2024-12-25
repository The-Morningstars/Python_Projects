print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
        bill =5
    elif age <= 18:
        print("Please pay $7.")
        bill = 7
    else:
        print("Please pay $10.")
        bill = 10

    response = input("do you want a pic? respond with Y or N")
    if response == "Y" :
            bill = bill + 3
            print (f"your total is {bill}")
    else:
        print(f"your total is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
