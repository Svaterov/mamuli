import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

step = 20
size = 10

for row in range(size):
    for col in range(size):
        t.penup()
        t.goto(col * step, row * step)
        t.pendown()
        sides = [step, step, step, step]
        if row % 2 == 0:
            sides[0] = 0
        else:
            sides[3] = 0

        for length in sides:
            if length == 0:
                t.penup()
                t.forward(step)
                t.pendown()
            else:
                t.forward(length)
            t.right(90)

t.penup()
t.goto(size * step / 2, size * step / 2)
t.hideturtle()

turtle.done()