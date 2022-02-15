from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
answer = "yes"
bid_dict = {}
while answer != "no":
  print("Welcome to the secret auction program.")
  name = input("What's your name?")
  bid= input("What's your bid? $")
  answer = input("Are there any other bidders? Type 'yes' or 'no'")
  clear()
  bid_dict[name]=bid
highest_bid = 0
winner = ""
for key in bid_dict:
  if int(bid_dict[key]) > highest_bid:
    highest_bid = int(bid_dict[key])
    winner = key
print(f"The winner is {winner}, and the bid is {highest_bid}")

# It can also be written by def at the final "for" part.
# and add the def in the while loop.
