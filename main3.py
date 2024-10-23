import turtle
t = turtle.Turtle()

s = turtle.Screen()
colors = ['orange', 'red', 'magenta', 'blue', 'yellow', 'cyan', 'yellow', 'green']
s.bgcolor('black')
t.pensize(3)
t.speed(0)

for x in  range(360):
    t.pencolor(colors[x%8])
    t.width(x//100+1)
    t.backward(x)
    t.right(44)

turtle.hideturtle()