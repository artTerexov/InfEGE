# Направо 30 Повтори 6 [Вперёд 7 Направо 120 Вперёд 7 Направо 60]


from turtle import *

tracer(0, 0)

zoom = 25

left(90)
right(30)
for i in range(6):
    forward(7 * zoom)
    right(120)
    forward(7 * zoom)
    right(60)

# рисуем точки на плоскости
penup()
for x in range(10):
    for y in range(-10, 10):
        goto(x * zoom, y * zoom)
        dot(5)

update()
done()

