from select import select

from art import logo, vs
from game_data import data
import random

print (logo)


# selection_A = random.choice(data)
# # print(selection_A)
# # print(selection_A["name"], "a", selection_A["description"], "from", selection_A["country"])
# A = int(selection_A["follower_count"])
# # print (A,"M")
#
# selection_B = random.choice(data)
# # print(selection_B)
# # print(selection_B["name"], "a", selection_B["description"], "from", selection_B["country"])
# B = int(selection_B["follower_count"])
# # print (B,"M")
#
# print("Compare A:",selection_A["name"], "a", selection_A["description"], "from", selection_A["country"])
# print("Compare B:",selection_B["name"], "a", selection_B["description"], "from", selection_B["country"])
# guess = input("who has more followers: A or B? ").upper()

replay = True

score = 0
while replay:
    selection_A = random.choice(data)
    A = int(selection_A["follower_count"])
    selection_B = random.choice(data)
    B = int(selection_B["follower_count"])
    print("Compare A:", selection_A["name"], "a", selection_A["description"], "from", selection_A["country"])
    print("Compare B:", selection_B["name"], "a", selection_B["description"], "from", selection_B["country"])
    guess = input("Who has more followers: A or B? ").upper()
    if guess == "A":
        if A > B:
            print ("RIGHT!")
            score = score + 1
            print(f"your score is {score}")
        else:
            print ("WRONG!")
            print(f"your score is {score}")
            print("Compare A:", selection_A["name"], "has", selection_A["follower_count"], "M followers")
            print("Compare B:", selection_B["name"], "has", selection_B["follower_count"], "M followers")
            replay = False

    if guess == "B":
        if B > A:
            print ("RIGHT!")
            score = score + 1
            print(f"your score is {score}")
        else:
            print ("WRONG!")
            print(f"your score is {score}")
            print("Compare A:", selection_A["name"], "has", selection_A["follower_count"],"M followers")
            print("Compare B:", selection_B["name"], "has", selection_B["follower_count"],"M followers")
            replay = False
    print("\n"*2)