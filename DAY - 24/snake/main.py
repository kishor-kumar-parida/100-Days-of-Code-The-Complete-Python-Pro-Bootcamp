from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Create a turtle object for displaying text at the bottom
message_turtle = Turtle()
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.color("white")
message_turtle.goto(0, -280)  # Bottom of the screen
message_turtle.write(
    "Press 'Enter' to end the game", align="center", font=("Arial", 12, "normal")
)

# Event listener for snake movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Function to end the game when Enter is pressed
def end_game():
    global game_is_on
    game_is_on = False


# Event listener for pressing Enter to end the game
screen.onkey(end_game, "Return")  # 'Return' is the Enter key

# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# Exit when the game ends
screen.exitonclick()
