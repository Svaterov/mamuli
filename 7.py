import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

length = 20
turn_angle = 90
steps = 50

for _ in range(steps):
    t.forward(length)
    t.left(turn_angle)
    length += 2
    t.forward(length)
    t.right(turn_angle)
    length += 2
    t.backward(length / 2)
    t.left(45)
    t.forward(length / 2)
    t.right(45)

t.hideturtle()
turtle.done()