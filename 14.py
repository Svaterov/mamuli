import turtle
import random

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("white")
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

balls = []
num_balls = 5
colors = ["red", "blue", "green", "orange", "purple"]
velocity_range = [-5, 5]
radius = 10

for _ in range(num_balls):
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    ball.goto(x, y)
    vx = random.randint(*velocity_range)
    vy = random.randint(*velocity_range)
    # избежать нулевой скорости
    if vx == 0:
        vx = 1
    if vy == 0:
        vy = 1
    balls.append({'t': ball, 'vx': vx, 'vy': vy})

while True:
    for ball in balls:
        t = ball['t']
        x, y = t.position()
        x += ball['vx']
        y += ball['vy']

        if x > 290 or x < -290:
            ball['vx'] *= -1
        if y > 290 or y < -290:
            ball['vy'] *= -1

        t.goto(x, y)