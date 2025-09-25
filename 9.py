import turtle
import math

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

size = 20
cols = 20
rows = 20

def draw_hexagon(size):
    for _ in range(6):
        t.forward(size)
        t.right(60)

for row in range(rows):
    for col in range(cols):
        x = col * size * 3/2
        y = row * size * math.sqrt(3)
        if row % 2 == 1:
            x += size * 0.75
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pencolor("black")
        t.fillcolor("yellow")
        t.begin_fill()
        for _ in range(6):
            t.forward(size)
            t.right(60)
        t.end_fill()

turtle.done()