# code to make a spirograph with turtle

from turtle import *
sides = 3
i: int = 1
pendown()
pensize(5)
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(135)
    if abs(pos()) < 1:
        break

end_fill()

penup()
goto(-200, -100)
pendown()
color("black", 'brown')
i = 0
begin_fill()
while i < sides:
    forward(100)
    left(360 / sides)
    i = i + 1

end_fill()
done()