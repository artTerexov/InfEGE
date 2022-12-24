from turtle import *


# отключение анимации
tracer(0, 0)
# коэффициент зумирования
z = 10
# Поворот на 90, чтобы черепаха смотрела на верх
left(90)
# Повтори 2 [Вперёд 10 Направо 90 Вперёд 20 Направо 90]
for i in range(2):
    forward(10 * z)
    right(90)
    forward(20 * z)
    right(90)
# Поднять хвост
pu()
# Назад 15 Направо 90 Вперёд 8 Налево 90
back(15 * z)
right(90)
forward(8 * z)
left(90)
# Опустить хвост
pd()
# Повтори 2 [Вперёд 30 Направо 90 Вперёд 40 Направо 90]
for i in range(2):
    forward(30 * z)
    right(90)
    forward(40 * z)
    right(90)

# Построение точек
pu()
for x in range(0, 21):
    for y in range(0, 20):
        goto(x * z, y * z)
        dot(5)

update()
done()