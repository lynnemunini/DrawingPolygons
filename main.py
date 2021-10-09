# Turtle Graphics Documentation
from turtle import Turtle, Screen
from random import randint
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.shapesize(1, 1)
# timmy_the_turtle.color("dark green")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.goto(5, 4)

# DRAW SQUARE
tim = Turtle()
# tim.shape("arrow")
# tim.shapesize(0.5, 0.5)
# for _ in range(4):
# tim.forward(100)
# tim.left(90)

# import heroes
# print(heroes.gen())

tim.shapesize(0.5, 0.5)
# Drawing a dashed line
# for _ in range(15):
# tim.fd(10)
# tim.penup()
# tim.fd(10)
# tim.pendown()

# Drawing triangle, square, pentagon, hexagon, heptagon
# Octagon, nonagon, decagon
screen = Screen()
screen.bgcolor("lemon chiffon")

# Setting the screen color-mode
screen.colormode(255)


def shape_down(lines):
    angle = 360 / lines
    for _ in range(lines):
        tim.fd(100)
        tim.right(angle)


def shape_up(lines):
    angle = 360 / lines
    for _ in range(lines):
        tim.fd(100)
        tim.left(angle)


for i in range(3, 11):
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    shape_down(i)
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    shape_up(i)

screen.exitonclick()


















