import turtle
import colorsys

turtle.setup(1000,1200)
turtle.speed(0)
turtle.tracer(5)
turtle.bgcolor("black")

times=24

for i in range (times):
    radius=240-i
    for j in range (times):
        turtle.color (colorsys.hsv_to_rgb (i/times 1,1))
        min(1,0.1+j/times), min(1,0.1/times)
        turtle.circle(radius)
        radius-=8
        turtle.right(30)


turtle.hideturtle
turtle.done()

