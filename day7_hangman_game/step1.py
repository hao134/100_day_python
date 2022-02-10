#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random
choice = random.randint(0, 2)
choose_word = word_list[choice]
# equal to -> chosen_word = random.choice(word_list)
guessed_letter = str(input("please guess a word: \n")).lower()
for word in choose_word:
    if word == guessed_letter:
        print("Right")
    else:
        print("Wrong")