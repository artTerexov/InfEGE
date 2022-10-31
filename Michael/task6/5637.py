# Повтори 5 [ Повтори 3 [ Вперед 4 Налево 90 ] Вперед 2 ]

from turtle import *

zoom = 10

left(90)
for i in range(5):
    for j in range(3):
        forward(4 * zoom)
        left(90)
    forward(2 * zoom)
done()

