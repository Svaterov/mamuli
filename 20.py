import turtle
import math

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

sun_radius = 30
planets = [
    {'radius': 80, 'size': 8, 'angle': 0, 'speed': 2},
    {'radius': 120, 'size': 12, 'angle': 90, 'speed': -1.5},
    {'radius': 180, 'size': 10, 'angle': 180, 'speed': 1},
    {'radius': 220, 'size': 14, 'angle': 270, 'speed': -0.5}
]

while True:
    t.clear()
    t.penup()
    t.goto(0, -sun_radius)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(sun_radius)
    t.end_fill()

    for p in planets:
        x = p['radius'] * math.cos(math.radians(p['angle']))
        y = p['radius'] * math.sin(math.radians(p['angle']))
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor("white")
        t.begin_fill()
        t.circle(p['size'])
        t.end_fill()
        p['angle'] += p['speed']
        p['angle'] %= 360
    turtle.update()
    