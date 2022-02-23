from art import logo, vs
from game_data import data
import random
from replit import clear

# Compare follower count
def compare(a, b):
    if int(data[a]['follower_count']) > int(data[b]['follower_count']):
        return True
    else:
        return False

# statement
def statement(num_a, num_b):
    print(logo)
    print(f"Compare A: {data[num_a]['name']}, a {data[num_a]['description']}, from {data[num_a]['country']}")
    print(f"test {data[num_a]['follower_count']}")
    print(vs)
    print(f"Against B: {data[num_b]['name']}, a {data[num_b]['description']}, from {data[num_b]['country']}")
    print(f"test {data[num_b]['follower_count']}")

play_game = True
compare_a = 0
compare_b = 1
count = 0
while play_game:
    statement(compare_a, compare_b)
    chosen = input("Who has more followers? Type 'A' or 'B':")
    if chosen == "A" and compare(compare_a, compare_b):
        count += 1
    elif chosen == "B" and compare(compare_b, compare_a):
        count += 1
    else:
        play_game = False
    compare_a = compare_b
    compare_b = random.randint(0,49)

    # Avoid compare two same elements
    while compare_b == compare_a:
        compare_b = random.randint(0, 49)
    clear()
    if play_game == True:
        print(f"You're right! Current score: {count}")
print(logo)
print(f"Sorry, that's wrong. Final score: {count}")







