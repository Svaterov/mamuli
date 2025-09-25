import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

def draw_shape():
    for _ in range(6):
        t.forward(50)
        t.backward(50)
        t.right(360 / 6)

for i in range(6):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * 60)
    t.pendown()
    draw_shape()

t.hideturtle()
turtle.done()