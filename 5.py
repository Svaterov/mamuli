import turtle

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_branch(length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
        return
    t.forward(length / 3)
    t.left(45)
    draw_branch(length / 3, level - 1)
    t.right(90)
    draw_branch(length / 3, level - 1)
    t.left(45)
    t.backward(length / 3)

def draw_snowflake():
    for _ in range(6):
        draw_branch(150, 3)
        t.right(60)

t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(2)
t.color("blue")

draw_snowflake()
turtle.done()