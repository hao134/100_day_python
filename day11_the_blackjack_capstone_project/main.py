from art import logo
import random
from replit import clear

should_continue = True
ask = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if ask == "n":
    should_continue = False
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while should_continue:
    clear()
    print(logo)
    user_card = []
    computer_card = []
    say_yes = "y"
    not_over_17 = "yes"
    for _ in range(2):
        user_card.append(random.choice(deck))
        computer_card.append(random.choice(deck))

    if sum(user_card) == 22:
        user_card = [11, 1]
        print(f"Your Cards: {user_card}, current score: {sum(user_card)}")
    else:
        print(f"Your Cards: {user_card}, current score: {sum(user_card)}")
    print(f"Computer's first card: {computer_card[0]}")
    if sum(user_card) == 21:
        say_yes = "n"
        not_over_17 = "no"
    if sum(computer_card) == 21 and sum(user_card) != 21:
        not_over_17 = "no"
        say_yes = "n"

    if say_yes != "n" and not_over_17 != "no":
        say_yes = input("Type 'y' to get another card, type 'n' to pass")

    while say_yes == "y":
        random_num = random.choice(deck)
        user_card.append(random_num)
        if sum(user_card) > 21 and random_num == 11:
            user_card[-1] = 1
        elif sum(user_card) > 21 and 11 in user_card:
            user_card[user_card.index(11)] = 1
        else:
            pass

        print(f"Your Cards: {user_card}, current score: {sum(user_card)}")
        if sum(user_card) > 21:
            say_yes = "n"
        else:
            say_yes = input("Type 'y' to get another card, type 'n' to pass")

    if sum(computer_card) > 17 and not_over_17 != "no":
        not_over_17 = "no"
    while not_over_17 == "yes":
        random_com = random.choice(deck)
        computer_card.append(random_com)
        if sum(computer_card) > 21 and random_com == 11:
            computer_card[-1] = 1
        elif sum(computer_card) > 21 and 11 in computer_card:
            computer_card[computer_card.index(11)] = 1
        else:
            pass
        if sum(computer_card) >= 17:
            not_over_17 = "no"
    print(f"Your final hand: {user_card}, final score: {sum(user_card)}")
    print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)}")
    # show the result
    if len(user_card) == 2 and sum(user_card) == 21:
        print("You got a blackjack, You win!")
    elif len(computer_card) == 2 and sum(user_card) == 21:
        print("Computer got a blackjack, Computer win")
    elif sum(user_card) > 21:
        print("You went over, you lose")
    elif sum(computer_card) > 21:
        print("Computer went over, you win")
    elif sum(user_card) > sum(computer_card):
        print("You win")
    elif sum(user_card) < sum(computer_card):
        print("You lose")
    else:
        print("Draw")
    ask = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if ask != "y":
        should_continue = False




