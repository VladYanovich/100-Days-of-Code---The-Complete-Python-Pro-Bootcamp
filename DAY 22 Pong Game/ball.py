from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        #self.hideturtle()
        self.shape("circle")
        self.penup()
        self.shapesize(1, 1)
        self.direction = {"x": 15, "y": 15}
        self.move_speed = 0.1


    def starting(self):
        self.hideturtle()
        self.goto(0, random.randint(-200, 200))
        self.showturtle()
        random.choice([self.right(0), self.left(180)])
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.direction["x"]
        new_y = self.ycor() + self.direction["y"]
        self.goto(new_x, new_y)

    def rebound_palette(self):
        self.direction["y"] *= random.choice([-1, 1])
        self.direction["x"] *= -1
        self.move_speed *= 0.5

    def rebound_wall(self):
        self.direction["y"] *= -1
