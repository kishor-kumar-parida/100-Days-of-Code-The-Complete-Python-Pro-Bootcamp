# from turtle import *
# import turtle
# import turtle as t
# pip install turtle

# import random
from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("green")
t.speed(0)


# ==================================================== #

# Challenge 1

# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)


# ==================================================== #

# Challenge 2

# for _ in range(15):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()


# ==================================================== #

# Challenge 3

# def draw_shape(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         t.forward(100)
#         t.right(angle)

# for shape_side in range(3, 11):
#     draw_shape(shape_side)


# ==================================================== #

# Challenge 4

# direction = [0, 90, 180, 270]
# t.pensize(10)

# for _ in range(100):
#     t.forward(30)
#     t.setheading(random.choice(direction))


# ==================================================== #

# # Challenge 5
# def draw(size):
#     for _ in range(int(360 / size)):
#         t.circle(100)
#         t.setheading(t.heading() + size)

# draw(1)


# ==================================================== #

# Challenge 6


# ==================================================== #


screen = Screen()
screen.exitonclick()
