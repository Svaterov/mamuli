import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()

pixel_size = 20

heart_pattern = [
    "  XX  XX  ",
    " XXXXXX ",
    "XXXXXXXX",
    "XXXXXXXX",
    " XXXXX ",
    "  XXX  ",
    "   X   "
]

def draw_pixel(x, y, color):
    t.goto(x, y)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(pixel_size)
        t.right(90)
    t.end_fill()
    t.penup()

start_x = -pixel_size * len(heart_pattern[0]) // 2
start_y = pixel_size * len(heart_pattern) // 2

for row_idx, row in enumerate(heart_pattern):
    for col_idx, ch in enumerate(row):
        if ch == "X":
            x = start_x + col_idx * pixel_size
            y = start_y - row_idx * pixel_size
            draw_pixel(x, y, "red")

turtle.done()