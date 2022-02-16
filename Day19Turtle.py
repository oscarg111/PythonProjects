from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False

oscar = Turtle()


def forwards():
    oscar.forward(10)


def backwards():
    oscar.back(10)


def right():
    oscar.right(10)


def left():
    oscar.left(10)


def clear():
    oscar.reset()


def etch_a_sketch():
    screen.listen()
    screen.onkey(key='w', fun=forwards)
    screen.onkey(key='s', fun=backwards)
    screen.onkey(key='a', fun=right)
    screen.onkey(key='d', fun=left)
    screen.onkey(key='c', fun=clear)


def turtle_bet():
    user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win?").lower()
    print(user_bet)

    turtles = []
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    original_y = -70
    for index in range(6):
        sandy = Turtle(shape='turtle')
        turtles.append(sandy)
        sandy.color(colors[index])
        sandy.penup()
        sandy.goto(x=-230, y=original_y)
        original_y += 30
    if user_bet:
        global is_race_on
        is_race_on = True

    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You lost! The {winning_color} turtle won!")
            rand_dist = random.randint(0, 10)
            turtle.forward(rand_dist)


etch_a_sketch()
# turtle_bet()
screen.exitonclick()
