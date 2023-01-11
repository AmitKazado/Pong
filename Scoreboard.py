from turtle import Turtle

# SCORE_POSITIONS = [(-100, 260), (100, 260)]
ALIGNMENT = "center"
FONT = ("Arial", 16, "bold")


class Scoreboard(Turtle):

    def __init__(self, x, y):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        # Increases a player score
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        # Updates the score object according to new score
        self.write(f"{self.score}", False, ALIGNMENT, FONT)
