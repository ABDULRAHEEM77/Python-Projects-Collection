from turtle import *
import colorsys
import math

# Screen setup
setup(900, 900)
bgcolor("black")
title("Hypnotic Mandala Fractal")

# Performance boost
tracer(0)
speed(0)
hideturtle()
colormode(1.0)

h = 0.0
penup()
goto(0, 0)
pendown()

# Main pattern
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.004

    for j in range(4):
        forward(i * 0.8)
        right(90)

    right(1)

update()
done()
