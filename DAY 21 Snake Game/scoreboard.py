from turtle import Turtle
FONT = ('Courier', 14, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score = 0
        self.write_score()

    def write_score(self):
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Your score: {self.score}", True, "center", font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()