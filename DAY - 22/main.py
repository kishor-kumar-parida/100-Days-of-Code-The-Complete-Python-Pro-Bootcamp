from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Constants
WINNING_SCORE = 5

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# Create paddles, ball, and scoreboard
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Listen to user input
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    # Detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

    # Check if either player has won
    if scoreboard.l_score == WINNING_SCORE:
        scoreboard.clear()
        scoreboard.goto(0, 0)
        scoreboard.write(
            "Left Player Wins!", align="center", font=("Courier", 36, "normal")
        )
        game_is_on = False  # Stop the game
    elif scoreboard.r_score == WINNING_SCORE:
        scoreboard.clear()
        scoreboard.goto(0, 0)
        scoreboard.write(
            "Right Player Wins!", align="center", font=("Courier", 36, "normal")
        )
        game_is_on = False  # Stop the game

screen.exitonclick()
