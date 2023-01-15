import random
from turtle import Turtle

STARTING_SPEED = 0.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.8)
        self.penup()
        self.move_speed = STARTING_SPEED
        self.x_move = 10
        self.y_move = 10
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def change_direction_x(self):
        # Horizontal Bounce
        self.x_move *= -1
        self.move_speed /= 1.1

    def change_direction_y(self):
        # Vertical Bounce
        self.y_move *= -1

    def restart_ball(self):
        self.clear()
        self.home()
        self.change_direction_x()
        self.move_speed = STARTING_SPEED



    
        