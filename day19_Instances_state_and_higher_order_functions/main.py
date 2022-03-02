from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_counter_clockwise():
    tim.setheading(tim.heading()+5)

def turn_clockwise():
    tim.setheading(tim.heading()-5)

def all_clear():
    tim.goto(0, 0)
    tim.setheading(0.0)
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=all_clear)
screen.exitonclick()
