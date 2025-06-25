import random
from turtle import Screen
from palette import Palette
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")


r_palette = Palette()
r_palette.right_palette()
l_palette = Palette()
l_palette.left_palette()
ball = Ball()
ball.starting()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_palette.up, "Up")
screen.onkeypress(r_palette.down, "Down")
screen.onkeypress(l_palette.up, "w")
screen.onkeypress(l_palette.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.distance(r_palette) < 20 or ball.distance(l_palette) < 20:
        ball.rebound_palette()
    elif ball.xcor() > 335 or ball.xcor() < -335:
        if ball.distance(r_palette) < 50 or ball.distance(l_palette) < 50:
            ball.rebound_palette()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.rebound_wall()

    if ball.xcor() > 500:
        ball.starting()
        scoreboard.l_point()
    elif ball.xcor() < -500:
        ball.starting()
        scoreboard.r_point()

















screen.exitonclick()