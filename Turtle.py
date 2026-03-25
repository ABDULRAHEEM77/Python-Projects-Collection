from turtle import *;
speed(0);
bgcolor("black");
ht()
colors = ["cyan", "magenta",
          "yellow", "white"]
for i in range(80):
    color(colors[i%4]); up();
    goto(-i*2,-i*2); down();
    for _ in range(4):
        forward(i*4); left(90)
done()