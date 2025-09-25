import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

def draw_half_loop(radius, direction):
    t.setheading(direction)
    t.circle(radius, 180)

t.penup()
t.goto(-50, 0)
t.pendown()
draw_half_loop(50, 0)

t.penup()
t.goto(50, 0)
t.pendown()
draw_half_loop(-50, 180)

t.hideturtle()
turtle.done()