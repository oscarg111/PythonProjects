from turtle import Screen
from Food import Food
from Scoreboard import Scoreboard
import Snake
import time

# setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)

# game objects
snake = Snake.Snakes()
food = Food()
scoreboard = Scoreboard()

# key listeners
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# game play variable
game_on = True

while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # detect food collision
    if snake.snake_parts[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect edge collision
    if snake.snake_parts[0].xcor() > 300 or snake.snake_parts[0].xcor() < -300 or snake.snake_parts[0].ycor() > 300 or snake.snake_parts[0].ycor() < -300:
        game_on = False
        scoreboard.game_over()

    # detect tail collision
    for segment in snake.snake_parts[1:]:
        if snake.snake_parts[0].distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
