# import colorgram
#
# colors  = colorgram.extract("image.jpg", 42)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Screen
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83), (245, 205, 7), (35, 88, 88), (103, 24, 56)]

def random_color():
    color_c = random.choice(color_list)
    return color_c
for i in range(10):
    tim.goto(-300, -300 + i * 65)
    for _ in range(10):
        tim.dot(20, random_color())
        tim.forward(65)

screen = Screen()
screen.exitonclick()
