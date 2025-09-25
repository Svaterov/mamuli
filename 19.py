import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

radius = 30
rows = 15
cols = 20
x_start = -screen.window_width() // 2
y_start = screen.window_height() // 2 - radius

for row in range(rows):
    for col in range(cols):
        x = x_start + col * radius * 1.5
        y = y_start - row * radius
        if row % 2 == 1:
            x += radius * 0.75
        t.goto(x, y)
        t.setheading(0)
        t.pendown()
        t.fillcolor("lightblue")
        t.begin_fill()
        t.circle(radius, 180)
        t.right(90)
        t.forward(radius * 2)
        t.right(90)
        t.circle(radius, 180)
        t.right(90)
        t.forward(radius * 2)
        t.end_fill()
        t.penup()

turtle.done()