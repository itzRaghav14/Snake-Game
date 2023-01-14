from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard, SCREEN_SIZE
import time

GAME_SPEED = 5


# Screen setup
screen = Screen()
screen.setup(width=2 * SCREEN_SIZE, height=2 * SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

# Creating objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Defining controls
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# MAIN GAME LOOP
game_on = True
while game_on:
	screen.update()
	time.sleep(0.5 / GAME_SPEED)
	snake.move()

	# Detect collision with Food
	if snake.head.distance(food) < 15:
		food.refresh()
		scoreboard.increase_score()
		snake.extend()
		GAME_SPEED *= 1.05

	# Detect collision with Wall
	if snake.head.xcor() > SCREEN_SIZE - 10 or snake.head.xcor() < -SCREEN_SIZE + 10 or snake.head.ycor() > SCREEN_SIZE - 10 or snake.head.ycor() < -SCREEN_SIZE + 10:
		game_on = False
		scoreboard.game_over()

	# Detect collision with Tail
	for segment in snake.segments[1:]:
		if snake.head.distance(segment) < 10:
			game_on = False
			scoreboard.game_over()

screen.exitonclick()
