from turtle import *
import colorsys

setup(900, 900)
bgcolor("black")
tracer(0)
speed(0)
hideturtle()
colormode(1.0)

h = 0

for i in range(500):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.002

    circle(i * 0.3, 60)
    right(20)

update()
done()
