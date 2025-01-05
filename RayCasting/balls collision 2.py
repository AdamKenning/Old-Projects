

# useful functions cause python handles trigonometry weirdly
def sin(num):
    num = math.sin(math.radians(num))
    return(num)

def cos(num):
    num = math.cos(math.radians(num))
    return(num)

def tan(num1,num2):
    num = math.degrees(math.atan2(num1,num2))
    return(num)

# defines a point in space
class point:
    def __init__(s,x,y):
        s.x = x
        s.y = y

def draw_grid(size):
    t_grid.pu()
    for i in range(2*size+1):
        t_grid.goto(-size,-size+i)
        t_grid.pd()
        t_grid.goto(+size,-size+i)
        t_grid.pu()

    for i in range(2*size+1):
        t_grid.goto(-size+i,-size)
        t_grid.pd()
        t_grid.goto(-size+i,+size)
        t_grid.pu()

def draw_point(point,colour,radius):
    if colour == None: colour = [0,0,0]
    if radius == None: radius = 0.1

    t_point.color(colour)
    
    t_point.pu()
    t_point.goto(point.x,point.y-radius)
    t_point.pd()
    t_point.circle(radius)
    t_point.pu()
    
#####################################################################
import math
import time
import turtle

screen = turtle.Screen()
size = 10
turtle.setworldcoordinates(-size-1,-size-1,size+1,size+1)
screen.colormode(255)

# useful stuff for turtle
turtle.pensize(3)
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0)
turtle.bgcolor("white")

t_grid = turtle.Turtle()
t_point = turtle.Turtle()

a = point(0,0)
b = point(9,7)

draw_grid(size)
draw_point(a,"red",0.1)
draw_point(b,"blue",0.1)
screen.update()

dx = b.x - a.x
dy = b.y - a.y

h = math.sqrt(dx**2 + dy **2)
theta = tan(dy,dx)
ctheta = 1/cos(theta)
stheta = 1/sin(theta)

cx,cy = 1,1
 
running = True
while running == True:
    time.sleep(0.2)

    hx = cx * ctheta
    hy = cy * stheta

    print()
    print("c = ",cx,cy)
    print("h = ",round(hx,3),round(hy,3))
    if round(abs(hx),5) == round(abs(hy),5) == round(abs(h),5):
        running = False
        print("aa")

    print("intersection = ")
    if abs(hx) < abs(hy):
        print(cos(theta)*hx,sin(theta)*hx)
        p = point(cos(theta)*hx,sin(theta)*hx)
        cx += 1
    else:
        print(cos(theta)*-hy,sin(theta)*-hy)
        p = point(cos(theta)*hy,sin(theta)*hy)
        cy += 1

    if round(abs(hx),5) != round(abs(h),5) or round(abs(hy),5) != round(abs(h),5):
        draw_point(p,"black",0.05)
    screen.update()

turtle.exitonclick()





































