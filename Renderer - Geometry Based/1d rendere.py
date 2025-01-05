import math
import turtle
from turtle import *
from turtle import Screen

turtle.goto(0,0)
turtle.setheading(90)
screen = Screen()
screen.screensize(100, 100)
unit = 10

fo = 5
od = 5
fm = 8
rs = 4

fd = math.sqrt(fo**2 + od**2)
print("fd =",fd)
dfo = math.degrees(math.acos((fo**2 + fd**2 - od**2)/(2*fo*fd)))
print("dfo=",dfo)
fam = 180 - 90 - dfo
print("fam=",fam)
am = (math.sin(dfo)*fm)/math.sin(fam)
print("am =",am)
tu = rs+(rs/am)
print("tu =",tu)

for i in range (100):
    user_input = input("forwards = w \nbackwards = s \n")
    if user_input == "w":
        fo = fo + 1

        turtle.clear()

        turtle.goto(0,0)
        turtle.setheading(90)

        turtle.rt(90)
        turtle.fd(fo*unit)

        turtle.goto(0,0)
        turtle.setheading(90)

        turtle.lt(90)
        turtle.fd(fo*unit)

        turtle.goto(0,0)
        turtle.setheading(90)

    elif user_input == "s":
        fo = fo - 1

        turtle.clear()

        turtle.goto(0,0)
        turtle.setheading(90)

        turtle.rt(90)
        turtle.fd(fo*unit)

        turtle.goto(0,0)
        turtle.setheading(90)

        turtle.lt(90)
        turtle.fd(fo*unit)

        turtle.goto(0,0)
        turtle.setheading(90)
        
