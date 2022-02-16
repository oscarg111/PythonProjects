from turtle import Screen
from Paddle import Paddle
import time
from PongScoreboard import Scoreboard
from Ball import Ball

# screen settings
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

# initializes game objects
right_paddle = Paddle(x_cor=350, y_cor=0)
left_paddle = Paddle(x_cor=-350, y_cor=0)
ball = Ball()
scoreboard = Scoreboard()

# gets player names
name1 = screen.textinput(title="Enter Player 1 username: ", prompt="(Left Player)")
name2 = screen.textinput(title="Enter Player 2 username: ", prompt="(Right Player)")
scoreboard.write_names(name1, name2)

# listens for key press
screen.listen()
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.deflect()
        ball.move()

    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()
        scoreboard.write_names(name1, name2)

    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()
        scoreboard.write_names(name1, name2)

    if scoreboard.l_score == 5:
        print(f"{name1} has won! congratulations {name1}!")
        game_is_on = False

    if scoreboard.r_score == 5:
        print(f"{name2} has won! congratulations {name2}!")
        game_is_on = False

    ball.move()

screen.exitonclick()
