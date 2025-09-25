import turtle
import random

screen = turtle.Screen()
screen.setup(800, 400)
screen.bgcolor("skyblue")
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-400, -150)
t.pendown()

ground_level = -150
building_width = 40
num_buildings = 20
min_height = 60
max_height = 200
window_size = 8
window_gap_x = 5
window_gap_y = 10

def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_window(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

x_pos = -400
for _ in range(num_buildings):
    height = random.randint(min_height, max_height)
    draw_rectangle(x_pos, ground_level, building_width, height, "dimgray")

    rows = (height - window_gap_y) // (window_size + window_gap_y)
    cols = (building_width - window_gap_x) // (window_size + window_gap_x)

    for row in range(rows):
        for col in range(cols):
            wx = x_pos + window_gap_x + col * (window_size + window_gap_x)
            wy = ground_level + window_gap_y + row * (window_size + window_gap_y)
            if random.random() > 0.3:
                draw_window(wx, wy, window_size)

    x_pos += building_width + 5

t.hideturtle()
turtle.done()