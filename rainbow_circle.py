import turtle
import colorsys
import math
import time

# Setup screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Animasi Lingkaran Pelangi")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Helper functions
def reset_turtle():
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.pendown()

def draw_circle(radius, color):
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# 1. Lingkaran Pelangi Tunggal
def rainbow_circle_single():
    reset_turtle()
    for i in range(36):
        t.color(colorsys.hsv_to_rgb(i / 36, 1, 1))
        t.circle(100)
        t.right(10)

# 2. Lingkaran Pelangi Berulang
def rainbow_circle_repeated():
    reset_turtle()
    for i in range(6):
        t.color(colorsys.hsv_to_rgb(i / 6, 1, 1))
        draw_circle((i + 1) * 20, colorsys.hsv_to_rgb(i / 6, 1, 1))

# 3. Spiral Pelangi
def rainbow_spiral():
    reset_turtle()
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    for i in range(50):
        t.color(colorsys.hsv_to_rgb(i / 50, 1, 1))
        t.circle(5)
        t.left(15)
        t.forward(10)

# 4. Lingkaran Pelangi Bertingkat
def rainbow_circle_layers():
    reset_turtle()
    for i in range(8, 0, -1):
        t.color(colorsys.hsv_to_rgb(i / 8, 1, 1))
        draw_circle(i * 15, colorsys.hsv_to_rgb(i / 8, 1, 1))

# 5. Lingkaran Pelangi Berlapis Transparansi
def rainbow_circle_transparent():
    reset_turtle()
    for i in range(8):
        t.color(colorsys.hsv_to_rgb(i / 8, 1, 1))
        draw_circle((i + 1) * 15, colorsys.hsv_to_rgb(i / 8, 1, 1))

# 6. Lingkaran Pelangi Berputar
def rainbow_circle_rotating():
    reset_turtle()
    for i in range(36):
        t.color(colorsys.hsv_to_rgb(i / 36, 1, 1))
        t.circle(50)
        t.right(10)

# 7. Jaring Lingkaran Pelangi
def rainbow_grid():
    reset_turtle()
    for i in range(6):
        for j in range(6):
            t.penup()
            t.goto(-200 + i * 50, 200 - j * 50)
            t.pendown()
            t.color(colorsys.hsv_to_rgb((i + j) / 10, 1, 1))
            draw_circle(20, colorsys.hsv_to_rgb((i + j) / 10, 1, 1))

# 8. Pola Grid Lingkaran Pelangi
def rainbow_grid_pattern():
    reset_turtle()
    for i in range(4):
        for j in range(4):
            t.penup()
            t.goto(-300 + i * 100, -300 + j * 100)
            t.pendown()
            t.color(colorsys.hsv_to_rgb((i + j) / 8, 1, 1))
            draw_circle(30, colorsys.hsv_to_rgb((i + j) / 8, 1, 1))

# 9. Lingkaran Pelangi Bergelombang
def rainbow_wave():
    reset_turtle()
    for i in range(24):
        t.color(colorsys.hsv_to_rgb(i / 24, 1, 1))
        t.goto(-200 + i * 10, 50 * math.sin(i))
        t.circle(5)

# 10. Lingkaran Pelangi Terpencar
def rainbow_random():
    reset_turtle()
    import random
    for _ in range(10):
        x, y = random.randint(-250, 250), random.randint(-250, 250)
        t.penup()
        t.goto(x, y)
        t.pendown()
        color = colorsys.hsv_to_rgb(random.random(), 1, 1)
        draw_circle(random.randint(10, 30), color)

# Main loop for animation
animations = [
    rainbow_circle_single,
    rainbow_circle_repeated,
    rainbow_spiral,
    rainbow_circle_layers,
    rainbow_circle_transparent,
    rainbow_circle_rotating,
    rainbow_grid,
    rainbow_grid_pattern,
    rainbow_wave,
    rainbow_random
]

while True:
    for animation in animations:
        animation()
        time.sleep(0.25)
        t.clear()
