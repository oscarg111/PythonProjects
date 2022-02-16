# from turtle import Turtle, Screen
import prettytable

# oscar = Turtle()
# oscar.shape("turtle")
# oscar.color("blue")
# oscar.forward(100)
#
# screen = Screen()
# print(screen.canvheight)
# screen.exitonclick()

table = prettytable.PrettyTable()
table.add_column("Pokemon", ["pikachu", "squirtle", "charmander"])
table.add_column("Type", ["electric", "water", "fire"])
table.align = "l"

print(table)