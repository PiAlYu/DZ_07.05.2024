from turtle import *

tracer(150)
n = 30
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * n, y * n)
        dot(3)
home()
left(90)
down()
for i in range(4):
    for j in range(6):
        forward(6 * n)
        right(150)
        forward(6 * n)
        right(30)
up()
done()