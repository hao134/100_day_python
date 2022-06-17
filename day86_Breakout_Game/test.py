from turtle import Screen, Turtle
from random import randint

def draw_square():
    turtle.goto(randint(-200, 200), randint(-200, 200))

    turtle.pendown()

    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

    turtle.penup()

def erase_square():
    turtle.clear()
    screen.ontimer(square_update)  # no time, ASAP

def square_update():
    draw_square()
    screen.ontimer(erase_square, 3000)  # 3 seconds in milliseconds

screen = Screen()

turtle = Turtle()
turtle.hideturtle()
turtle.speed('fastest')
turtle.penup()

square_update()

screen.exitonclick()