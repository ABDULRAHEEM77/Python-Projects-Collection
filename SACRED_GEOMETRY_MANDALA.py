from turtle import *
import colorsys
import math

# Screen setup
setup(900, 900)
bgcolor("black")
title("Sacred Geometry Mandala")

# Speed & performance
tracer(0)
speed(0)
hideturtle()
colormode(1.0)

h = 0.0
penup()
goto(0, 0)
pendown()

# Mandala layers
for layer in range(6):
    for i in range(180):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.002

        circle(200 - layer * 25, 60)
        right(360 / 12)

    right(360 / 6)

update()
done()
