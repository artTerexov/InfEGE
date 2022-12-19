# Повтори 2 [Вперёд 10 Направо 90 Вперёд 20 Направо 90]
# Поднять хвост
# Вперёд 15 Направо 90 Назад 10 Налево 90
# Опустить хвост
# Повтори 2 [Вперёд 20 Направо 90 Вперёд 40 Направо 90]
from turtle import *
tracer(0, 0)
z = 10
left(90)
for i in range(2):
    forward(10 * z)
    right(90)
    forward(20 * z)
    right(90)
pu()
forward(15 * z)
right(90)
back(10 * z)
left(90)
pd()
for i in range(2):
    forward(20 * z)
    right(90)
    forward(40 * z)
    right(90)

# Рисуем точки
# pu()
# for x in range(25):
#     for y in range(25):
#         goto(x * z, y * z)
#         dot(5)

update()
done()