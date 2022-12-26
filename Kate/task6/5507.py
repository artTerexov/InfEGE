# Вперёд 200
# Повтори 200 [Направо 90 Вперёд 50]
from turtle import *
tracer(0, 0)
z = 5
left(90)
# forward(200)
for i in range(200):
    right(90)
    forward(50 * z)
pu()
for x in range(51):
    for y in range(-51, 0):
        goto(x * z, y * z)
        dot(3)
update()
done()
