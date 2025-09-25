import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)

size = 20
angle = 30

for _ in range(36):
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.right(angle)
    size += 5

turtle.done()