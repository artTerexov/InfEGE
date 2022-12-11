# Повтори 2 [Вперёд 10 Направо 90 Вперёд 20 Направо 90]
# Поднять хвост
# Вперёд 3 Направо 90 Вперёд 5 Налево 90
# Опустить хвост
# Повтори 2 [Вперёд 70 Направо 90 Вперёд 80 Направо 90]

from turtle import *


tracer(0, 0)
zoom = 15
left(90)

for i in range(2):
    forward(10 * zoom)
    right(90)
    forward(20 * zoom)
    right(90)
pu()
forward(3 * zoom)
right(90)
forward(5 * zoom)
left(90)
pd()
for i in range(2):
    forward(70 * zoom)
    right(90)
    forward(80 * zoom)
    right(90)

pu()
for x in range(25):
    for y in range(12):
        goto(x * zoom, y * zoom)
        dot(5)

done()