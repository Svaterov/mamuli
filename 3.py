import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_star(size, points):
    angle = 180 - 180 / points
    for _ in range(points):
        t.forward(size)
        t.right(angle)

for _ in range(20):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    star_size = random.randint(10, 30)
    points = random.choice([5, 8])
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    draw_star(star_size, points)

turtle.done()