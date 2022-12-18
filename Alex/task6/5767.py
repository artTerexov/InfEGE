from turtle import *


# Повтори 2 [Вперёд 10 Направо 90 Вперёд 20 Направо 90]
# Поднять хвост
# Вперёд 3 Направо 90 Вперёд 5 Налево 90
# Опустить хвост
# Повтори 2 [Вперёд 70 Направо 90 Вперёд 80 Направо 90]


# Ускорение анимации
tracer(0, 0)
# Поворот по направлению оси Оу
left(90)
# Коэффициент увеличения
z = 15

for i in range(2):
    forward(10 * z)
    right(90)
    forward(20 * z)
    right(90)
pu()
forward(3 * z)
right(90)
forward(5 * z)
left(90)
pd()
for i in range(2):
    forward(70 * z)
    right(90)
    forward(80 * z)
    right(90)

# Рисование точек
pu()
for x in range(50):
    for y in range(50):
        goto(x * z, y * z)
        dot(5)
update()
done()