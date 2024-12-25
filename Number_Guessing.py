import random
from art import logo
print (logo)
answer = random.randint(1,100)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
mode = input("Choose a difficulty. Type 'easy' or 'hard':\n")

def guessing_game ():
    if mode == "easy":
        attempts = 10
        print("You have 10 attempts remaining to guess the number")
        guess = int(input("Make a guess:\n"))
        while guess != answer and attempts > 1:
            if guess > answer:
                attempts = attempts - 1
                print("too high")
                print(f"You have {attempts} left")
                guess = int(input("try again: \n"))
            if guess < answer:
                attempts = attempts - 1
                print("too low")
                print(f"You have {attempts} left")
                guess = int(input("try again: \n"))
            if guess == answer:
                attempts = attempts - 1
                print(f"You have {attempts} left")
                print(f"The answer was {answer}")
                print("YOU WIN!")
        if attempts == 1:
            print(f"The answer was {answer}")
            print("No more chances. \n YOU LOSE!")

    else:
        attempts = 5
        print("You have 5 attempts remaining to guess the number")
        guess = int(input("Make a guess:\n"))
        while guess != answer and attempts > 1:
            if guess > answer:
                attempts = attempts - 1
                print("too high")
                print(f" You have {attempts} left")
                guess = int(input("try again: \n"))
            if guess < answer:
                attempts = attempts - 1
                print("too low")
                print(f" You have {attempts} left")
                guess = int(input("try again: \n"))
            if guess == answer:
                attempts = attempts - 1
                print(f" You have {attempts} left")
                print(f"The answer was {answer}")
                print("YOU WIN!")
        if attempts == 1:
            print(f"The answer was {answer}")
            print("No more chances. \n YOU LOSE!")
guessing_game()
