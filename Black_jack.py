import random
import art

from art import logo
print(logo)

def deal_card():
    """returns random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """this is to calculate card scores from list"""
    if sum == 21 and len(cards) == 2:
        return 0
    # this is to replace black jack with zero
    if sum(cards) > 21 and 11 in (cards) and len(cards) == 2:
        cards.remove(11)
        cards.append(1)
    # this is to replace ace with 1

    return sum(cards)


# the start
def playgame():
    user_cards = []
    computer_cards = []
    is_game_over = False
    computer_score = -1
    user_score = -1

    for _ in range (2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards {user_cards} and your score {user_score}")
        print(f"computer cards {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("do you want to draw again? y or n\n")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score < 17 and computer_score != 0 :
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    def compare(u_score, c_score):
        if u_score == c_score:
            print("draw")
        elif c_score == 0 or u_score > 21:
            print("you lose")
        elif u_score == 0 or c_score > 21:
            print("you win")
        else:
            print("you lose")

    print(f"your final hand is {user_cards} and final score was {user_score}")
    print(f"computer final card {computer_cards} and final score is {computer_score}")
    print(compare(user_score,computer_score))


while input("do you want to play again? y or n") == "y":
    print("\n" * 20)
    playgame()

# total_sum =sum(user_cards)
# computer_sum =sum(computer_cards)
#
# print (f" the cards are {user_cards}, your total score is {total_sum}")
# print (f" the computer cards are {computer_cards}, the computer score is {computer_sum}")
























# print(input("Do you want to play a game of blackjack? y or n \n"))
#
# drawn_card_1 = random.randint(1,11)
# drawn_card_2 = random.randint(1,11)
# drawn_card_3 = random.randint(1,11)
# drawn_card_4 = random.randint(1,11)
# drawn_card_5 = random.randint(1,11)
# drawn_card_6 = random.randint(1,11)
# computer_card_1= random.randint(1,11)
# computer_card_2= random.randint(1,11)
# computer_card_3= random.randint(1,11)
# computer_card_4= random.randint(1,11)
# computer_card_5= random.randint(1,11)
# computer_card_6= random.randint(1,11)
#
# sum = drawn_card_1+drawn_card_2
# print(f"Your cards: [{drawn_card_1},{drawn_card_2}], current score:{sum}")
# print(f"Computers first card: {computer_card_1}")
# draw_again=(input("Type y to get another card, or n to pass\n"))
# if draw_again == "y":
#     final_sum = drawn_card_1 + drawn_card_2 + drawn_card_3
#     print(f"Your cards: [{drawn_card_1},{drawn_card_2},{drawn_card_3}], current score:{final_sum}")
#     print(f"Computers first card: {computer_card_1}")
#     if final_sum == 21:
#         print("you win")
#     if final_sum > 21:
#         print ("you lose")
#     if final_sum < 21:
#         draw_again = (input("Type y to get another card, or n to pass\n"))
#         if draw_again == "y":
#             final_sum = drawn_card_1 + drawn_card_2 + drawn_card_3 + drawn_card_4
#             computer_score = computer_card_1 +computer_card_2 +computer_card_3 +computer_card_4
#             print(f"Your cards: [{drawn_card_1},{drawn_card_2},{drawn_card_3}, {drawn_card_4}],  current score:{final_sum}")
#             print(f"Computers first card: [ {computer_card_1},{computer_card_2},{computer_card_3}, {computer_card_4}], computer final score {computer_score}:")
#             if final_sum == 21 or computer_score > 21:
#                 print("you win")
#             if final_sum > 21:
#                 print("you lose")
#             if final_sum < 21:
#                 draw_again = (input("Type y to get another card, or n to pass\n"))
#                 if draw_again == "y":
#                     final_sum = drawn_card_1 + drawn_card_2 + drawn_card_3 + drawn_card_4 + drawn_card_5
#                     print(
#                         f"Your cards: [{drawn_card_1},{drawn_card_2},{drawn_card_3}, {drawn_card_4}, {drawn_card_5}],  current score:{final_sum}")
#                     print(f"Computers first card: {computer_card_1}")
#                     if final_sum == 21:
#                         print("you win")
#                     if final_sum > 21:
#                         print("you lose")
#                     if final_sum < 21:
#                         print("DRAW")
#                 else:
#                     computer_sum = computer_card_1 + computer_card_2 + computer_card_3
#                     final_sum = drawn_card_1 + drawn_card_2 + drawn_card_3
#                     print(f"Your cards: [{drawn_card_1},{drawn_card_2}],{drawn_card_3}] current score:{final_sum}")
#                     print(
#                         f"Computers first card: [{computer_card_1}, {computer_card_2}, {computer_card_3}] computer score:{computer_sum}")
#                     if final_sum > 21 :
#                         print("you lose")
#                     if computer_sum > 21:
#                         print("you win")
#         else:
#             computer_sum = computer_card_1 + computer_card_2 + computer_card_3
#             final_sum = drawn_card_1 + drawn_card_2 + drawn_card_3
#             print(f"Your cards: [{drawn_card_1},{drawn_card_2}],{drawn_card_3}] current score:{final_sum}")
#             print(f"Computers first card: [{computer_card_1}, {computer_card_2}, {computer_card_3}] computer score:{computer_sum}")
#             if final_sum > 21 or sum < computer_sum:
#                 print("you lose")
#             else:
#                 print("you win")
# else:
#     computer_sum = computer_card_1 + computer_card_2
#     print(f"Your cards: [{drawn_card_1},{drawn_card_2}], current score:{sum}")
#     print(f"Computers first card: [{computer_card_1}, {computer_card_2}], computer score:{computer_sum}")
#     if sum > 21 or sum < computer_sum:
#         print("you lose")
#     else:
#         print("you win")

    # if  computer_card_1 < final_sum <= 21:
    #       print("you win")
    #       print(f"Your cards: [{drawn_card_1},{drawn_card_2},{drawn_card_3}], current score:{final_sum}")
    #       print(f"Computers first card: {computer_card_1}")
    # if final_sum > 21:
    #       print("you lose")
    #       print(f"Your cards: [{drawn_card_1},{drawn_card_2},{drawn_card_3}], current score:{final_sum}")
    #       print(f"Computers first card: {computer_card_1}")
    # if final_sum
# else:
#     computer_sum = computer_card_1 + computer_card_2
#     print(f"Your final cards: [{drawn_card_1},{drawn_card_2}] current score:{sum}")
#     print(f"Computers final first cards: [{computer_card_1},{computer_card_2}] current score:{computer_sum}")
#     if computer_sum < sum <= 21:
#         print("you win")
#         input("Type y to get another card, or n to pass\n")
#         # draw_again
#     else:
#         print("you lose")
#         input("Type y to get another card, or n to pass\n")
        # draw_again
# draw_again = (input("Type y to get another card, or n to pass\n"))
#     if draw_again == "y":
#         computer_card_2= random.randint(1,11)
#         computersum = computer_card_1 + computer_card_2
#         print(f"Computers cards: [{computer_card_1},{computer_card_2}], current score:{computersum}")
#     if computersum < sum < 21:
#          print("you win")
#     else:
#          print("you lose")
#  else:
#      print("game is in development")

