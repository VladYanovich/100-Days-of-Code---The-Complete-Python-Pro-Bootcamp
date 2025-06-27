from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-230,265)
        self.write(f"Level: {self.level}", align="center", font = FONT)

    def rewrite_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=FONT)
