from turtle import Turtle
import random


class Food(Turtle):

    # on initialization
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    # sets a new position for food
    def refresh(self):
        rand_x = random.randint(-200, 200)
        rand_y = random.randint(-200, 200)
        self.goto(rand_x, rand_y)
