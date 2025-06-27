from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]



class CarManager(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(0.8, 2)
        self.y = random.randint(-250, 250)
        self.goto(330, self.y)
        self.s_cars = []
        self.speed = speed

    def car_move(self):
        new_x = self.xcor() - self.speed
        self.goto(new_x, self.y)

    def create_s_cars(self):
        for n in range(15):
            car = CarManager(self.speed)
            car.goto(random.randint(-300, 300), random.randint(-250, 250))
            self.s_cars.append(car)

    def move_s_cars(self):
        for car in self.s_cars:
            car.car_move()