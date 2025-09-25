import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.width(3)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
segments = 36
angle = 360 / segments
segment_length = 10

for i in range(segments):
    t.pencolor(colors[i % len(colors)])
    t.forward(segment_length)
    t.right(angle)

t.hideturtle()
turtle.done()