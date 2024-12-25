import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



person=input("what do you pick? R,P,S")
if person == "R":
    print(rock)
if person == "P":
    print(paper)
if person == "S":
    print(scissors)

computer_answer = random.randint(0,2)
if computer_answer ==0:
    print(rock)
if computer_answer ==1:
    print(paper)
if computer_answer == 2:
    print(scissors)

