import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
game_on = True


state_data = pd.read_csv("50_states.csv")
states = state_data["state"].to_list()

while game_on:
    answer_state = screen.textinput(title=f"Guess the state {score}/50", prompt="Whats another state's name?").title()

    if answer_state in states:
        turt = turtle.Turtle()
        turt.hideturtle()
        turt.penup()
        turt.goto(int(state_data[state_data["state"] == answer_state]["x"]), int(state_data[state_data["state"] == answer_state]["y"]))
        turt.write(answer_state)
        score += 1
    if score == 50:
        game_on = False

screen.exitonclick()
