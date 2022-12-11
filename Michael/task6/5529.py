from turtle import *

tracer(0, 0)
zoom = 30
left(90)
for i in range(11):
    forward(4 * zoom)
    right(60)

pu()
for x in range(1, 10):
    for y in range(1, 10):
        goto(x * zoom, y * zoom)
        dot(3)
update()
done()