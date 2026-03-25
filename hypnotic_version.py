from turtle import *
import colorsys

setup(900, 900)
bgcolor("black")
tracer(0)
speed(0)
hideturtle()
colormode(1.0)

h = 0

for i in range(200):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.005

    forward(i * 2)
    right(59)

update()
done()
