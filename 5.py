import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

def draw_branch(length, depth):
    if depth == 0:
        t.forward(length)
        t.backward(length)
    else:
        for _ in range(3):
            t.forward(length / 3)
            draw_branch(length / 3, depth - 1)
            t.backward(length / 3)
            t.right(45)

for _ in range(6):
    draw_branch(100, 2)
    t.right(60)

t.hideturtle()
turtle.done()