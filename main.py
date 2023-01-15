import time
from turtle import Screen
from Ball import Ball
from Paddle import Paddle
from Scoreboard import Scoreboard

TOP_WALL = 280
BOTTOM_WALL = -280
LEFT_WALL = -290
RIGHT_WALL = 290
LEFT_PADDLE_X = -250
RIGHT_PADDLE_Y = 250

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
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > TOP_WALL or ball.ycor() < BOTTOM_WALL:
        # Ball hits a wall
        ball.change_direction_y()

    if ball.distance(l_paddle) < 50 and ball.xcor() < LEFT_PADDLE_X or ball.distance(r_paddle) < 50 and ball.xcor() > RIGHT_PADDLE_Y:
        # Ball hits a Paddle
        ball.change_direction_x()

    if ball.xcor() < LEFT_WALL:
        # Ball passes left Paddle, Right player earns a point.
        time.sleep(1)
        l_scoreboard.increase_score()
        ball.restart_ball()

    if ball.xcor() > RIGHT_WALL:
        # Ball passes left Paddle, Left player earns a point.
        time.sleep(1)
        r_scoreboard.increase_score()
        ball.restart_ball()

screen.exitonclick()
