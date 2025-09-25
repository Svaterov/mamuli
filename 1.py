import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.width(2)

num_petals = 36
angle = 10
big_radius = 40
small_radius = 10
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

for i in range(num_petals):
    t.penup()
    t.goto(0, -big_radius)
    t.setheading(i * angle)
    t.pendown()
    t.pencolor(random.choice(colors))
    t.circle(big_radius)  

    t.penup()
    t.goto(0, -small_radius)
    t.setheading(i * angle)
    t.pendown()
    t.pencolor("white")
    t.circle(small_radius)

t.hideturtle()
turtle.done()