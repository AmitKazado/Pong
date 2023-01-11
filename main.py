import time
from turtle import Screen
from Ball import Ball
from Paddle import Paddle
from Scoreboard import Scoreboard

TOP_WALL = 280
BOTTOM_WALL = -280
LEFT_WALL = -310
RIGHT_WALL = 310

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
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > TOP_WALL or ball.ycor() < BOTTOM_WALL:
        ball.change_direction()
    
    # requires fixing
    # if ball.distance(l_paddle) < 50 and ball.xcor() < -260 or ball.distance(r_paddle) < 50 and ball.xcor() > 260:
    #     ball.change_direction()

    if ball.xcor() < LEFT_WALL:
        time.sleep(1)
        l_scoreboard.increase_score()
        ball.restart_ball()

    if ball.xcor() > RIGHT_WALL:
        time.sleep(1)
        r_scoreboard.increase_score()
        ball.restart_ball()

screen.exitonclick()
