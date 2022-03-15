# Errors
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dicitonary = {"key":"value"}
# value = a_dicitonary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

########### example 1: try / except / else /finally

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sdfsdf"])
# except FileNotFoundError:
#     file = open("a_file.txt","w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else: # else will be executed only the above except didn't be triggled.
#     content = file.read()
#     print(content)
# finally: # finally will be executed anyway
#     file.close()
#     print("File was closed")

############ example 2: raise
# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")
# bmi = weight / height ** 2
# print(bmi)

########## exercise 1
# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("the index is out of range")
#     else:
#         print(fruit + "pie")
#
#
# make_pie(4)

########### excercise 2
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         total_likes += 0
#         # or
#         #pass
#
#
# print(total_likes)


########### exercise 3
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

######### my attempt
# no_error = False
# while no_error != True:
#     try:
#         word = input("Enter a word: ").upper()
#         output_list = [phonetic_dict[letter] for letter in word]
#         print(output_list)
#         no_error = True
#     except KeyError:
#         print("Sorry, only letters in the alphabet please")

####### solution to exercise 3


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list=[phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()


# 點評： 我只想到用while loop 解決， 這樣子製造迴圈的方式真的高明，這就是 recursive吧?

