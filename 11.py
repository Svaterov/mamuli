import turtle
import math

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.width(2)

amplitude = 50
frequency = 2
length = 360
steps = 1000

for i in range(steps):
    x = i * (length / steps)
    y = amplitude * math.sin(frequency * math.radians(x))
    t.goto(x - length / 2, y)

t.hideturtle()
turtle.done()