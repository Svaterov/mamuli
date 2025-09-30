import turtle

# Настройка окна
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
turtle.colormode(255)

# Цвета для узора
colors = [(0, 0, 0), (70, 130, 180), (255, 99, 71)]  # Черный, голубой, томатный

def draw_line(start, end, color):
    t.penup()
    t.goto(start)
    t.pendown()
    t.color(color)
    t.goto(end)

def draw_celtic_pattern(size, spacing):
    # Создаст сетку линий для имитации переплетения
    for i in range(-size, size + 1, spacing):
        # Вертикальные линии
        draw_line((i, -size), (i, size), colors[i // spacing % len(colors)])
        # Горизонтальные линии
        draw_line((-size, i), (size, i), colors[(i // spacing + 1) % len(colors)])

def main():
    size = 300  # Размер области
    spacing = 30  # Расстояние между линиями
    draw_celtic_pattern(size, spacing)
    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()