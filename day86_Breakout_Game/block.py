from turtle import Turtle

class Block(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(position)
