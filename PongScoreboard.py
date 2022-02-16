from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 190)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def write_names(self, name1, name2):
        self.goto(-100, 250)
        self.write(f"{name1}:", align="center", font=("Courier", 20, "normal"))
        self.goto(100, 250)
        self.write(f"{name2}:", align="center", font=("Courier", 20, "normal"))
