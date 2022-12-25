# Повтори 2 [Налево 120 Опустить хвост
# Повтори 10 [Направо 30 Вперёд 4 Направо 60]
# Поднять хвост
# Налево 150 Назад 2 Налево 90 Назад 2]

from turtle import *
tracer(0, 0)
z = 30
left(90)
for i in range(2):
    left(120)
    pendown()
    for k in range(10):
        right(30)
        forward(4 * z)
        right(60)
    penup()
    left(150)
    back(2 * z)
    left(90)
    back(2 * z)

# рисование точек
penup()
for x in range(-10, 10):
    for y in range(0, 10):
        goto(x * z, y * z)
        dot(5)
update()
done()