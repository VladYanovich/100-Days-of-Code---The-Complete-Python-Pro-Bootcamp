from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")

    def move(self):
        self.forward(MOVE_DISTANCE)

    def move_to_start(self):
        self.goto(STARTING_POSITION)
