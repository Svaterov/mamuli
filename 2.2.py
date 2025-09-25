import turtle
import random

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("#020252")  
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_star(size, points=5):
    angle = 180 - 180 / points
    t.penup()
    x = random.randint(-350, 350)
    y = random.randint(-250, 250)
    t.goto(x, y)
    t.pendown()
    t.color("#A39300")  
    t.begin_fill()
    for _ in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

for _ in range(20):
    star_size = random.randint(10, 30)
    star_points = random.choice([5, 8])
    draw_star(star_size, star_points)

turtle.done()