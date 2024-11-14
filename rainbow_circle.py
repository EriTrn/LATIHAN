import turtle
import colorsys
import math
import random

turtle.speed(0)
turtle.bgcolor("black")

def draw_circle(radius, color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
for i in range(36):
    turtle.color(colorsys.hsv_to_rgb(i / 36, 1, 1))
    turtle.circle(100)
    turtle.right(10)

# turtle.penup()
# turtle.goto(100, 0)
# turtle.pendown()
# for i in range(6):
#     turtle.color(colorsys.hsv_to_rgb(i / 6, 1, 1))
#     draw_circle((i+1)*20, colorsys.hsv_to_rgb(i / 6, 1, 1))

# turtle.penup()
# turtle.goto(-200, -200)
# turtle.pendown()
# for i in range(50):
#     turtle.color(colorsys.hsv_to_rgb(i / 50, 1, 1))
#     turtle.circle(5)
#     turtle.left(15)
#     turtle.forward(10)

# turtle.penup()
# turtle.goto(200, -200)
# turtle.pendown()
# for i in range(8, 0, -1):
#     turtle.color(colorsys.hsv_to_rgb(i / 8, 1, 1))
#     draw_circle(i * 15, colorsys.hsv_to_rgb(i / 8, 1, 1))

# turtle.penup()
# turtle.goto(0, -200)
# turtle.pendown()
# for i in range(8):
#     turtle.color(colorsys.hsv_to_rgb(i / 8, 1, 1))
#     draw_circle((i+1) * 15, colorsys.hsv_to_rgb(i / 8, 1, 1))
#     turtle.setheading(0)

# turtle.penup()
# turtle.goto(-200, 200)
# turtle.pendown()
# for i in range(36):
#     turtle.color(colorsys.hsv_to_rgb(i / 36, 1, 1))
#     turtle.circle(50)
#     turtle.right(10)

# turtle.penup()
# turtle.goto(200, 200)
# turtle.pendown()
# for i in range(6):
#     for j in range(6):
#         turtle.penup()
#         turtle.goto(-200 + i*50, 200 - j*50)
#         turtle.pendown()
#         turtle.color(colorsys.hsv_to_rgb((i + j) / 10, 1, 1))
#         draw_circle(20, colorsys.hsv_to_rgb((i + j) / 10, 1, 1))

# for i in range(4):
#     for j in range(4):
#         turtle.penup()
#         turtle.goto(-300 + i * 100, -300 + j * 100)
#         turtle.pendown()
#         turtle.color(colorsys.hsv_to_rgb((i + j) / 8, 1, 1))
#         draw_circle(30, colorsys.hsv_to_rgb((i + j) / 8, 1, 1))

# turtle.penup()
# turtle.goto(-200, 0)
# turtle.pendown()
# for i in range(24):
#     turtle.color(colorsys.hsv_to_rgb(i / 24, 1, 1))
#     turtle.goto(-200 + i * 10, 50 * math.sin(i))
#     turtle.circle(5)

# for _ in range(10):
#     x, y = random.randint(-250, 250), random.randint(-250, 250)
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     color = colorsys.hsv_to_rgb(random.random(), 1, 1)
#     draw_circle(random.randint(10, 30), color)

turtle.hideturtle()
turtle.done()