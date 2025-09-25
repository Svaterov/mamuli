import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

width, height = 800, 600
screen.setup(width, height)

num_lines = 15
segments_per_line = 20
step_length = 30

def random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

import random
turtle.colormode(255)

for _ in range(num_lines):
    x = random.randint(-width//2 + 50, width//2 - 50)
    y = random.randint(-height//2 + 50, height//2 - 50)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(random_color())

    angle = random.randint(0, 360)
    t.setheading(angle)

    for _ in range(segments_per_line):
        turn_angle = random.uniform(-90, 90)
        t.right(turn_angle)
        t.forward(step_length)

turtle.done()