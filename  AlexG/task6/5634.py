from turtle import *


# отключение анимации
tracer(0, 0)
# коэффициент зумирования
z = 40

# Повтори 3 раз
for i in range(3):
    #   Сместиться на (3, 2)
    goto(xcor() + 3 * z, ycor() + 2 * z)
    #   Сместиться на (-2, 3)
    goto(xcor() - 2 * z, ycor() + 3 * z)
    #   Сместиться на (-3, -2)
    goto(xcor() - 3 * z, ycor() - 2 * z)
    #   Сместиться на (2, -3)
    goto(xcor() + 2 * z, ycor() - 3 * z)


# Построение точек
pu()
for x in range(-5, 10):
    for y in range(0, 10):
        goto(x * z, y * z)
        dot(5)

update()
done()
# конец