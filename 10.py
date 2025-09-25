import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -200)
t.pendown()

def draw_branch(length, depth):
    if depth == 0 or length < 5:
        return
    t.forward(length)
    t.left(30)
    draw_branch(length * 0.7, depth - 1)
    t.right(60)
    draw_branch(length * 0.7, depth - 1)
    t.left(30)
    t.backward(length)

draw_branch(100, 6)
t.hideturtle()
turtle.done()