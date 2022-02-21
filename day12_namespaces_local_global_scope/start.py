#

# Global scope
# player_health = 10
#
# def drink_potion():
#     potion_strength = 2
#     print(player_health)
# drink_potion()

# There is no Block Scope
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]
# print(new_enemy)

# Modifying Global scope
#
# enemies = "Skeleton"
# def increase_enemies():
#     global enemies
#     enemies = "Zombie"
#     print(f"enemies inside function: {enemies}")
# increase_enemies()
# print(f"enemies inside function: {enemies}")
#
# # or
# enemies = 1
# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1
# enemies = increase_enemies()
# print(f"enemies ouside function: {enemies}")

# Global Constants -> used for store constant
PI = 3.14159
URL = "https://www.google.com"
TWITER_HANDLER = "@yu_angela"