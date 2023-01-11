from turtle import Screen
from Ball import Ball
from Paddle import Paddle
from Scoreboard import Scoreboard


screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
ball = Ball()
l_paddle = Paddle(-280, 0)
r_paddle = Paddle(280, 0)
l_scoreboard = Scoreboard(-120, 260)
r_scoreboard = Scoreboard(120, 260)

screen.listen()
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()


screen.exitonclick()
