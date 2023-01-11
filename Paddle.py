from turtle import Turtle

MOVING_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, x, y):
        super(Paddle, self).__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.color("white")
        self.goto(x, y)

    def move_up(self):
        self.sety(self.ycor() + MOVING_DISTANCE)

    def move_down(self):
        self.sety(self.ycor() - MOVING_DISTANCE)


