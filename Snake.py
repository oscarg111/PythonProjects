from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
starting_x = 0


class Snakes:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()

    # creates snake
    def create_snake(self):
        global starting_x
        for x in range(3):
            self.add_segment((starting_x, 0))
            starting_x -= 20

    # moves all snake segments
    def move(self):
        for part in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part - 1].xcor()
            new_y = self.snake_parts[part - 1].ycor()
            self.snake_parts[part].goto(new_x, new_y)
        self.snake_parts[0].forward(20)

    # directional controls for snake
    def up(self):
        if self.snake_parts[0].heading() != DOWN:
            self.snake_parts[0].setheading(90)

    def down(self):
        if self.snake_parts[0].heading() != UP:
            self.snake_parts[0].setheading(270)

    def left(self):
        if self.snake_parts[0].heading() != RIGHT:
            self.snake_parts[0].setheading(180)

    def right(self):
        if self.snake_parts[0].heading() != LEFT:
            self.snake_parts[0].setheading(0)

    # adds a segment to the snake
    def extend(self):
        self.add_segment(self.snake_parts[-1].position())

    def add_segment(self, position):
        global starting_x
        oscar = Turtle(shape="square")
        oscar.penup()
        oscar.color("white")
        self.snake_parts.append(oscar)
        oscar.goto(position)
        starting_x -= 20

