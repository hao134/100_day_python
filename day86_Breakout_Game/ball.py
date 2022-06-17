from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.start_angle = 360 - 53
        self.move_speed = 0.1

    def move(self):
        self.setheading(self.start_angle)
        self.forward(20)

    def bounce_y(self):
        self.start_angle = 360 - self.start_angle

    def bounce_x(self):
        self.start_angle = 180 - self.start_angle

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()