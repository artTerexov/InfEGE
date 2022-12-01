from turtle import *

left(90)
zoom = 50
for i in range(7):
    forward(10 * zoom)
    right(120)
pu()
for x in range(11):
    for y in range(11):
        goto(x * zoom, y * zoom)
        dot(5)
done()