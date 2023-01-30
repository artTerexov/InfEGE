from turtle import *
tracer(0, 0)
goto(0, 0)
left(90)
for I in range(10):
    goto(xcor() + 200, ycor() + 100)
    goto(xcor() - 50, ycor() - 150)
    goto(xcor() - 150, ycor() + 50)
penup()
# for x in range(-10, 40):
#     for y in range(-30, 10):
#         goto(x, y)
#         dot(10)
update()
done()