from turtle import Turtle
import time

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.scores = []
        self.update_scoreboard()
        self.game_is_on = True

    def update_scoreboard(self):
        self.clear()
        self.goto(0,200)
        self.write(self.score, align="center", font=("Courier", 80, "normal"))

    def update_finalscoreboard(self):
        self.clear()
        self.goto(0,0)
        self.write("Best: " +str(self.score) +" pts", align="center", font=("Courier", 80, "normal"))


    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        self.score = 0
        self.update_scoreboard()

    def save_scores(self):
        self.scores.append(self.score)

    def best_score(self):
        self.score = max(self.scores)
        self.update_finalscoreboard()
        time.sleep(3)
        self.game_is_on = False

