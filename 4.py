import turtle

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.color("darkgreen")
t.hideturtle()

def wave(length, amplitude, waves_count):
    step = length / (waves_count * 2)
    for _ in range(waves_count):
        t.circle(amplitude, 90)
        t.circle(-amplitude, 90)

def draw_celtic_wave_square(size=300, amplitude=20, waves=6):
    start_x, start_y = -size / 2, size / 2
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(0)
    t.pendown()

    for _ in range(4):
        wave(size, amplitude, waves)
        t.right(90)

def draw_inner_pattern(size=300, amplitude=10, waves=4):
    step = size / 4
    for i in range(1, 4):
        # Horizontal wavy lines
        t.penup()
        t.goto(-size/2, size/2 - i * step)
        t.setheading(0)
        t.pendown()
        wave(size, amplitude, waves)
        # Vertical wavy lines
        t.penup()
        t.goto(-size/2 + i * step, size/2)
        t.setheading(-90)
        t.pendown()
        wave(size, amplitude, waves)

draw_celtic_wave_square(300, 20, 6)
t.pensize(2)
draw_inner_pattern(300, 10, 4)

turtle.done()