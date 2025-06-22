from turtle import Screen, Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for n in range(0, 3):
            turtle = Turtle("square")
            turtle.penup()
            turtle.color("white")
            turtle.goto(-20 * n, 0)
            turtle.penup()
            self.segments.append(turtle)


    def add_segment(self, position):
        turtle = Turtle("square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)
        turtle.penup()
        self.segments.append(turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].position())
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


