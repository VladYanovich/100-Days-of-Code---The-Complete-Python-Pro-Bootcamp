import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
STARTING_MOVE_DISTANCE = 5

scoreboard = Scoreboard()
player = Player()


screen.listen()
screen.onkeypress(player.move, "Up")
next_level = True

starting_cars = CarManager(STARTING_MOVE_DISTANCE)
starting_cars.create_s_cars()

spawn = 5
moving_cars = []
car_speed = [0, 0, 0, 0]
game_is_on = True

def create_moving_cars():
    moving_cars.append(CarManager(STARTING_MOVE_DISTANCE))

while game_is_on:
    time.sleep(0.1)
    screen.update()
    starting_cars.move_s_cars()

    for car in moving_cars:
        car.car_move()

    for n in range(0,4):
        car_speed[n] += 1

    if car_speed[0] % spawn == 0:
        create_moving_cars()
        if car_speed[1] % spawn + 5 == 0 and scoreboard.level > 1:
            create_moving_cars()
            if car_speed[2] % spawn*2 + 1 == 0:
                create_moving_cars()
                create_moving_cars()

    all_cars = moving_cars + starting_cars.s_cars
    for car in all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.move_to_start()
        scoreboard.rewrite_level()
        STARTING_MOVE_DISTANCE += 10
        spawn -= 1

screen.exitonclick()