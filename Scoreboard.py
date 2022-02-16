from turtle import Turtle


class Scoreboard(Turtle):

    # initializes scoreboard
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=250)
        self.write(arg=f"Score: {self.score}", align="center", font=("Courier", 12, "normal"))

    # function to increase score
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align="center", font=("Courier", 12, "normal"))

    # function that displays the end of the game
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align="center", font=("Courier", 12, "normal"))
