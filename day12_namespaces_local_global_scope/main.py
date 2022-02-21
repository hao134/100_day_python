from art import logo
import random

answer = random.randint(1, 100)
guess = -1
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# print(f"Pssst, the correct answer is {answer}")
mode = "not_chosen"
flag = True

while mode == "not_chosen":
    mode = input("Choose a difficulty. Type 'easy' or 'hard':")
    if mode != "easy" and mode != "hard":
        print("please choose one mode")
        mode = "not_chosen"

if mode =="easy":
    chance = 10
    while flag:
        print(f"You have {chance} attempts remaining to guess the number")
        guess = int(input("Make a guess:"))
        if guess < answer:
            print("Too low\nGuess again")
        elif guess > answer:
            print("Too high\nGuess again")
        else:
            print(f"You got it! The answer was {answer}")
            flag = False
        chance -= 1
        if chance == 0:
            print(f"You've run out of guesses, you lose. The answer is {answer}")
            flag = False
else:
    chance = 5
    while flag:
        print(f"You have {chance} attempts remaining to guess the number")
        guess = int(input("Make a guess:"))
        if guess < answer:
            print("Too low\nGuess again")
        elif guess > answer:
            print("Too high\nGuess again")
        else:
            print(f"You got it! The answer was {answer}")
            flag = False
        chance -= 1
        if chance == 0:
            print(f"You've run out of guesses, you lose. The answer is {answer}")
            flag = False



