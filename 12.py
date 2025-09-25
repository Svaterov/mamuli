import turtle

screen = turtle.Screen()
screen.setup(400, 400)
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()

size = 300
steps = 100

def interpolate_color(color1, color2, factor):
    return tuple(int(color1[i] + (color2[i] - color1[i]) * factor) for i in range(3))

red = (255, 0, 0)
blue = (0, 0, 255)

turtle.colormode(255)
start_x = -size / 2
start_y = size / 2
step_size = size / steps

for i in range(steps):
    factor = i / (steps - 1)
    color = interpolate_color(red, blue, factor)
    t.fillcolor(color)
    t.goto(start_x + i * step_size, start_y)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(step_size)
        t.right(90)
        t.forward(size)
        t.right(90)
    t.end_fill()
    t.penup()

turtle.done()