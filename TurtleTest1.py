# turtle stuff
i = 0
from turtle import *
sides = 12345
color('red', 'teal')
begin_fill()
pensize(5)
while i < 100000000000000000000:
    forward(1)
    left(360 / sides)
    i = i + 1
end_fill()
done()
