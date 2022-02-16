from turtle import Turtle, Screen
from random import randint, choice

color_list = [(245, 243, 239), (246, 243, 244), (202, 164, 109), (240, 245, 242), (236, 239, 243), (153, 75, 49),
              (222, 201, 136), (53, 94, 124), (171, 153, 41), (136, 32, 21), (133, 163, 184), (197, 93, 73),
              (48, 123, 87), (73, 44, 36), (14, 97, 72), (145, 178, 148), (91, 73, 75), (233, 176, 165),
              (160, 143, 159), (54, 47, 50), (184, 205, 172), (35, 61, 75), (22, 85, 89), (146, 19, 21), (86, 146, 130),
              (38, 67, 91), (13, 72, 66), (106, 128, 155), (175, 99, 101), (176, 192, 209), (114, 135, 138),
              (207, 182, 188), (69, 63, 57), (179, 197, 201)]
oscar = Turtle()
oscar.shape("classic")
oscar.color("red")
screen = Screen()
screen.colormode(255)
screen.screensize(500, 500)


def dashed_line(dashes, dash_size, distance_between_dash, random_colors):
    if random_colors:
        for x in range(dashes):
            oscar.color(color_list[randint(0, len(color_list) - 1)])
            oscar.forward(dash_size)
            oscar.penup()
            oscar.forward(distance_between_dash)
            oscar.pendown()
    else:
        for x in range(dashes):
            oscar.forward(dash_size)
            oscar.penup()
            oscar.forward(distance_between_dash)
            oscar.pendown()


def square():
    for x in range(4):
        oscar.forward(100)
        oscar.right(90)


def triangle():
    for x in range(3):
        oscar.forward(100)
        oscar.right(120)


def pentagon():
    for x in range(5):
        oscar.forward(100)
        oscar.right(72)


def hexagon():
    for x in range(6):
        oscar.forward(100)
        oscar.right(60)


def heptagon():
    for x in range(7):
        oscar.forward(100)
        oscar.right(51.429)


def octagon():
    for x in range(8):
        oscar.forward(100)
        oscar.right(45)


def nonagon():
    for x in range(9):
        oscar.forward(100)
        oscar.right(40)


def decagon():
    for x in range(10):
        oscar.forward(100)
        oscar.right(36)


def random_walk():
    arr = [0, 1]
    oscar.speed("fastest")
    oscar.pensize(5)
    for x in range(1000):
        if oscar.pos()[0] > 250:
            oscar.setheading(180)
            print("right bound hit")
        elif oscar.pos()[0] < -250:
            oscar.setheading(0)
            print("left bound hit")
        elif oscar.pos()[1] > 250:
            oscar.setheading(270)
            print("upper bound hit")
        elif oscar.pos()[1] < -250:
            oscar.setheading(90)
            print("lower bound hit")
        straight_or_turn = choice(arr)
        if straight_or_turn == 0:
            oscar.forward(10)
        else:
            oscar.color(random_color())
            left_or_right = choice(arr)
            if left_or_right == 0:
                oscar.left(90)
                oscar.forward(10)
            else:
                oscar.right(90)
                oscar.forward(10)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def spirograph():
    oscar.speed(1000)
    oscar.pensize(.5)
    angle = 0
    while angle < 273:
        if oscar.ycor() > 0:
            angle += 3
        oscar.circle(100)
        oscar.pencolor(random_color())
        oscar.right(3)


def dot_drawing():
    oscar.speed("fastest")
    oscar.penup()
    oscar.setx(-285)
    oscar.sety(-165)
    oscar.pendown()
    print(oscar.pos())
    oscar.pensize(30)
    dashed_line(12, 1, 50, True)
    for x in range(0, 7):
        oscar_y_pos = oscar.pos()[1]
        oscar.penup()
        oscar.setx(-285)
        oscar.sety(oscar_y_pos + 50)
        oscar.pendown()
        dashed_line(12, 1, 50, True)



# dashed_line(5)
# square()
# oscar.color(random_color())
# triangle()
# oscar.color(random_color())
# pentagon()
# oscar.color(random_color())
# hexagon()
# oscar.color(random_color())
# heptagon()
# oscar.color(random_color())
# octagon()
# oscar.color(random_color())
# nonagon()
# oscar.color(random_color())
# decagon()
# random_walk()
spirograph()
# dot_drawing()


screen.exitonclick()
