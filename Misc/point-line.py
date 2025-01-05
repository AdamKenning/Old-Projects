def cos(num):
    num = math.cos(math.radians(num))
    return(num)

def draw_point(point):
    colour = point.c
    if colour == None:turtle.color("black")
    else: turtle.fillcolor(colour)
    
    turtle.goto(point.x,point.y-point.r)

    turtle.begin_fill()
    turtle.circle(point.r)
    turtle.end_fill()

def draw_line(line):
    draw_point(line.p1)
    draw_point(line.p2)
    
    turtle.goto(line.p1.x,line.p1.y)
    turtle.pd()
    turtle.goto(line.p2.x,line.p2.y)
    turtle.pu()

def distance(p1,p2):
    d = math.sqrt(abs(p1.x-p2.x)**2 + abs(p1.y-p2.y)**2)
    return(d)

def collision(point,line):
    line_length = distance(line.p1,line.p2)
    
    distance_1 = distance(point,line.p1)
    distance_2 = distance(point,line.p2)

    distance_t = distance_1 + distance_2
    
    if line_length >= distance_t:
        return(True)
    else:
        return(False)
    

class point: # point
    def __init__(s,x,y,r,c):
        s.x = x
        s.y = y
        s.r = r #radius
        s.c = c #colour

class line:
    def __init__(s,p1,p2):
        s.p1 = p1
        s.p2 = p2

p = point(50,50,5,"black")

p1 = point(30,5,0.5,"black")
p2 = point(80,80,0.5,"black")

l = line(p1,p2)

import turtle
import math

default_colour = "black"
size = 100
turtle.setworldcoordinates(0,0, size, size)
turtle.pensize(2)
turtle.hideturtle()
turtle.tracer(0)
turtle.pu()

counter = 0
running = True
while running == True:
    counter += 1
    
    draw_point(p)
    draw_line(l)
    turtle.Screen().update()
    turtle.clear()

    p.x = (p.x + 0.05)%size

    if collision(p,l) == True: p.c = "red";print("c")
    else: p.c = default_colour












