import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.width(2)

num_circles = 8
radius_step = 30
num_radial = 16

for i in range(1, num_circles + 1):
    t.penup()
    t.goto(0, -i * radius_step)
    t.pendown()
    t.circle(i * radius_step)

for i in range(num_radial):
    angle = 360 / num_radial * i
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.pendown()
    t.forward(num_circles * radius_step)

t.hideturtle()
turtle.done()