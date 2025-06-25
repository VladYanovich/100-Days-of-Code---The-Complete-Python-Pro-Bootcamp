from turtle import Turtle


class Palette(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.hideturtle()
        self.shapesize(1, 5)
        self.color("white")
        self.left(90)


    def left_palette(self):
        self.goto(-360, 0)
        self.showturtle()

    def right_palette(self):
        self.goto(360, 0)
        self.showturtle()

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)