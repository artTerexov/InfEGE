from turtle import *

tracer(0, 0)
z = 10
left(90)
for i in range(6):
    forward(5 * z)
    right(60)
pu()
forward(5 * z)
right(90)
pd()
for i in range(2):
    forward(15 * z)
    right(90)
    forward(5 * z)
    right(90)
pu()
for x in range(0, 20):
    for y in range(0, 20):
        goto(x * z, y * z)
        dot(5)
update()
done()
