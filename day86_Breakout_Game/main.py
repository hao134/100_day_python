from turtle import Screen
from padding import Paddle
from ball import Ball
from block import Block
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Breakout Game")
screen.tracer(0)


paddle = Paddle((0, -280))
block1 = Block((0,30))
block2 = Block((120, 30))
block3 = Block((-120,30))
block4 = Block((0, 75))
block5 = Block((120, 75))
block6 = Block((-120,75))
block7 = Block((0, 120))
block8 = Block((120, 120))
block9 = Block((-120, 120))
blocks = [block1, block2, block3, block4, block5, block6, block7, block8, block9]
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_left,"Left")
screen.onkey(paddle.go_right, "Right")


while scoreboard.game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.ycor() < -270:
        ball.bounce_y()


    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    for block in blocks:
        if ball.distance(block) < 30:
            block.hideturtle()
            ball.bounce_y()
            blocks.remove(block)
            scoreboard.add_point()


    if ball.ycor() < -320:
        ball.reset_position()
        scoreboard.save_scores()
        scoreboard.reset()

    if len(blocks) == 0:
        scoreboard.save_scores()
        scoreboard.best_score()

screen.exitonclick()