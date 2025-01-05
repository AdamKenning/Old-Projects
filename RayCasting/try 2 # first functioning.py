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

def get_angle(a,b):
    d_x = a.x - b.x
    d_y = a.y - b.y
    angle = tan(d_y,d_x)
    return(angle)

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
        
def get_p(p,a,b):
    dx = b.x - a.x
    dy = b.y - a.y

    px = round(p.x,5)
    py = round(p.y,5)
    
    if dx >= 0:
        if px%1 == 0:
            px += -1      
    else:
        if px%1 == 0:
            px += +0      

    if dy >= 0:
        if py%1 == 0:
            py += -1      
    else:
        if py%1 == 0:
            py += +0
        
    px = math.floor(px)
    py = math.floor(py)
  
    p = point(px,py)
    return(p)

def draw_fill(point,colour):
    t_fill.pu()
    t_fill.fillcolor(colour)
    
    t_fill.goto(point.x+0,point.y+0)
        
    t_fill.begin_fill()
    t_fill.goto(point.x+1,point.y+0)
    t_fill.goto(point.x+1,point.y+1)
    t_fill.goto(point.x+0,point.y+1)
    t_fill.goto(point.x+0,point.y+0)
    t_fill.end_fill()

    
def draw_point(point,colour,radius):
    t_point.fillcolor(colour)
    
    t_point.pu()
    t_point.goto(point.x,point.y-radius)
    t_point.begin_fill()
    t_point.circle(radius)
    t_point.end_fill()

def draw_line(a,b,colour):
    t_line.pensize(2)
    
    t_line.pu()
    t_line.goto(a.x,a.y)
    t_line.color(colour)
    t_line.pd()
    t_line.goto(b.x,b.y)

# returns intersections of a ray
def get_intersects(a,b):
    intersects = []
    
    dx = b.x - a.x
    dy = b.y - a.y

    if dx != 0 or dy != 0:
        theta = tan(dy,dx)
        cx = 1 
        cy = 1
        running = True
        while running == True:
            hx = abs(cx/cos(theta))
            try:
                hy = abs(cy/sin(theta))
            except:
                hy = hx + 1

            if hx > hy:
                cy += 1

                px = a.x + cos(theta)*hy
                py = a.y + sin(theta)*hy
            if hx < hy:
                cx += 1

                px = a.x + cos(theta)*hx
                py = a.y + sin(theta)*hx
            if hx == hy:
                cx += 1
                cy += 1

                px = a.x + cos(theta)*hx
                py = a.y + sin(theta)*hx

            if cx-1 == abs(dx) and cy-1 == abs(dy):
                running = False

        
            p = point(px,py)
            intersects.append(p)

    if dx == 0 and dy == 0:
        p = point(a.x,a.y)
        intersects.append(p)
        
    return(intersects)
        
import math
import time
import turtle

screen = turtle.Screen()
size = 20
turtle.setworldcoordinates(-size-1,-size-1,size+1,size+1)
screen.colormode(255)

# useful stuff for turtle
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0)
turtle.bgcolor("white")

t_grid = turtle.Turtle()
t_point = turtle.Turtle()
t_fill = turtle.Turtle()
t_line = turtle.Turtle()

t_grid.hideturtle()
t_point.hideturtle()
t_fill.hideturtle()
t_line.hideturtle()

start = point(0,0)
end = point(5,0)

angle = 0
def rotate_end():
    global angle
    angle += 0.5

    l = 7
    
    length = (cos(angle)*l)*(sin(angle)*l)
    x = cos(angle)*length
    y = sin(angle)*length
    
    end.x = int(round(x,0))
    end.y = int(round(y,0))
    #return(angle)


draw_grid(size)   
game_running = True
while game_running == True:
    rotate_end()
    
    for i in range(len(get_intersects(start,end))):
        p = get_intersects(start,end)[i]
        p_square = get_p(p,start,end)
        
        draw_fill(p_square,"grey")

    draw_point(start,"red",0.2)
    draw_point(end,"blue",0.2)

    draw_line(start,end,"pink")

    for i in range(len(get_intersects(start,end))):
        p = get_intersects(start,end)[i]
        draw_point(end,"orange",0.1)

    screen.update()
    t_point.clear()
    t_fill.clear()
    t_line.clear()



















































    
