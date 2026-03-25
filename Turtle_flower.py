from turtle import *
import colorsys

# Screen setup
setup(width=800, height=800)
bgcolor("black")
title("Advanced Turtle Spiral Art")

# Performance boost
tracer(0)
speed(0)
hideturtle()
colormode(1.0)

h = 0.0

penup()
goto(0, 0)
pendown()

for i in range(36):
    for j in range(20):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.003

        circle(180 - j * 6, 90)
        left(90)
        circle(180 - j * 6, 90)
        right(180)

    left(10)

update()
done()
