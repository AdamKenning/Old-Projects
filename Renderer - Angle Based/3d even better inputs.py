
    
# sets inputs on off
def input_on(key):
    key.press = True
def input_off(key):
    key.press = False

# takes stuff broing lame
def input_handler(camera,mouse):
    c = camera
    
    # movement horizontal
    if press_w.press == True:
        c.x -= (cos(c.angle.h) * move_speed)
        c.z -= (sin(c.angle.h) * move_speed)
    if press_s.press == True:
        c.x += (cos(c.angle.h) * move_speed)
        c.z += (sin(c.angle.h) * move_speed)
    if press_a.press == True:
        c.x -= (sin(c.angle.h) * move_speed)
        c.z += (cos(c.angle.h) * move_speed)
    if press_d.press == True:
        c.x += (sin(c.angle.h) * move_speed)
        c.z -= (cos(c.angle.h) * move_speed)
    # movement up/down
    if press_z.press == True:
        c.y += move_speed
    if press_x.press == True:
        c.y -= move_speed

    m = mouse
    mx = m.x * 0.01
    my = -(m.y * 0.01)

    if math.sqrt(mx**2+my**2) < 0.2:
        pass
    else:
        c.angle.h = format180((c.angle.h + mx))
        c.angle.v = format180((c.angle.v + my))
    
    # look around
    if press_e.press == True:
        c.fov.h = (c.fov.h + 1 if c.fov.h != -1 else c.fov.h + 2)
        c.fov.v = (c.fov.v + 1 if c.fov.v != -1 else c.fov.v + 2)
        #c.angle.h = format180((c.angle.h + look_speed))
    if press_q.press == True:
        c.fov.h = (c.fov.h - 1 if c.fov.h != +1 else c.fov.h - 2)
        c.fov.v = (c.fov.v - 1 if c.fov.v != +1 else c.fov.v - 2)
        #c.angle.h = format180((c.angle.h - look_speed))
    if press_r.press == True:
        c.angle.v = format180((c.angle.v + look_speed))
    if press_f.press == True:
        c.angle.v = format180((c.angle.v - look_speed))

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

# function for returning distance
def get_distance(a,b):
    d_x = abs(a.x - b.x)
    d_y = abs(a.y - b.y)
    d_z = abs(a.z - b.z)
    d = math.sqrt(d_x**2 + d_y**2 + d_z**2)
    return(d)

# functions for returning angle between two points
def get_angle(a,b): 
    d_x = a.x - b.x
    d_z = a.z - b.z

    y = abs(a.y-b.y)
    d_y = (y if b.y > a.y else -y)
   
    horizontal = tan(d_z,d_x)
    d_xz = math.sqrt(d_x**2 + d_z**2)

    """
    if horizontal < -90 or  horizontal > 90:
        d_xz = 0 - d_xz
    """
    verticle = tan(d_y,d_xz)

    return(horizontal,verticle)

# shifts an angle into the range of +180 -180
def format180(angle):
    if angle > 180:
        angle = angle - 2*180
    elif angle < -180:
        angle = angle + 2*180
    return angle

# gets the mean of an arbitrary amount of items
def mean(*args):
    return(sum(args)/len(args))

# class of mouse
class mouse:
    def __init__(s,x,y):
        s.x = x
        s.y = y
        
class hv: # horizontal & verticle
    def __init__(s,h,v):
        s.h = h
        s.v = v

class decimal:
    def __init__(s,point):
        s.d = hv((format180(get_angle(c,point)[0] - c.angle.h))/(c.fov.h/2),
                 (format180(get_angle(c,point)[1] - c.angle.v))/(c.fov.v/2))

# defines a point in space
class point:
    def __init__(s,x,y,z):
        s.shape = "point"
        s.x = x
        s.y = y
        s.z = z
        
# defines a triangle in space
class triangle():
    def __init__(s,p1,p2,p3,colour):
        s.shape = "triangle"
        s.p1 = point(p1[0],p1[1],p1[2])
        s.p2 = point(p2[0],p2[1],p2[2])
        s.p3 = point(p3[0],p3[1],p3[2])
        
        s.colour = colour

# defines a square in space
class square():
    def __init__(s,p1,p2,p3,p4,colour):
        s.shape = "square"
        s.p1 = point(p1[0],p1[1],p1[2])
        s.p2 = point(p2[0],p2[1],p2[2])
        s.p3 = point(p3[0],p3[1],p3[2])
        s.p4 = point(p4[0],p4[1],p4[2])
        
        s.colour = colour

# updates everything 
def update_point(point,camera):
    c = camera
    p = point
    p.d = hv((format180(get_angle(c,p)[0] - c.angle.h))/(c.fov.h/2),
             (format180(get_angle(c,p)[1] - c.angle.v))/(c.fov.v/2))
    
    p.pc_distance = math.sqrt(abs(p.x-c.x)**2 + abs(p.y-c.y)**2 + abs(p.z-c.z)**2)
    
def update_triangle(triangle,camera):
    c = camera
    s = triangle
    s.pc = point(mean(s.p1.x,s.p2.x,s.p3.x),
                 mean(s.p1.y,s.p2.y,s.p3.y),
                 mean(s.p1.z,s.p2.z,s.p3.z))

    s.pc_distance = get_distance(s.pc,c)
    
    s.d1 = hv((format180(get_angle(c,s.p1)[0] - c.angle.h))/(c.fov.h/2),
              (format180(get_angle(c,s.p1)[1] - c.angle.v))/(c.fov.v/2))
    s.d2 = hv((format180(get_angle(c,s.p2)[0] - c.angle.h))/(c.fov.h/2),
              (format180(get_angle(c,s.p2)[1] - c.angle.v))/(c.fov.v/2))
    s.d3 = hv((format180(get_angle(c,s.p3)[0] - c.angle.h))/(c.fov.h/2),
              (format180(get_angle(c,s.p3)[1] - c.angle.v))/(c.fov.v/2))
    
def update_square(square,camera):
    c = camera
    s = square
    s.pc = point(mean(s.p1.x,s.p2.x,s.p3.x,s.p4.x),
                 mean(s.p1.y,s.p2.y,s.p3.y,s.p4.y),
                 mean(s.p1.z,s.p2.z,s.p3.z,s.p4.z),)

    s.pc_distance = get_distance(s.pc,c)
    
    s.d1 = hv((format180(get_angle(c,s.p1)[0] - c.angle.h))/(c.fov.h/2),
              (format180(get_angle(c,s.p1)[1] - c.angle.v))/(c.fov.v/2))
    s.d2 = hv((format180(get_angle(c,s.p2)[0] - c.angle.h))/(c.fov.h/2),
              (format180(get_angle(c,s.p2)[1] - c.angle.v))/(c.fov.v/2))
    s.d3 = hv((format180(get_angle(c,s.p3)[0] - c.angle.h))/(c.fov.h/2),
              (format180(get_angle(c,s.p3)[1] - c.angle.v))/(c.fov.v/2))
    s.d4 = hv((format180(get_angle(c,s.p4)[0] - c.angle.h))/(c.fov.h/2),
              (format180(get_angle(c,s.p4)[1] - c.angle.v))/(c.fov.v/2))

# defines a cube  
class cube():
    def __init__(s,x,y,z,radius,colour):
        s.shape = "cube"
        r = radius/2
        # top/bottom
        s.s1 = square([x-r,y+r,z-r],[x-r,y+r,z+r],[x+r,y+r,z+r],[x+r,y+r,z-r],colour)
        s.s2 = square([x-r,y-r,z-r],[x-r,y-r,z+r],[x+r,y-r,z+r],[x+r,y-r,z-r],colour)
        # left/right
        s.s3 = square([x-r,y-r,z+r],[x-r,y+r,z+r],[x+r,y+r,z+r],[x+r,y-r,z+r],colour)
        s.s4 = square([x-r,y-r,z-r],[x-r,y+r,z-r],[x+r,y+r,z-r],[x+r,y-r,z-r],colour)
        # front/back
        s.s5 = square([x-r,y-r,z-r],[x-r,y+r,z-r],[x-r,y+r,z+r],[x-r,y-r,z+r],colour)
        s.s6 = square([x+r,y-r,z-r],[x+r,y+r,z-r],[x+r,y+r,z+r],[x+r,y-r,z+r],colour)
        
        s.s = [s.s1,s.s2,s.s3,s.s4,s.s5,s.s6]

# defines the camera    
class camera:
    def __init__(s,x,y,z,angle_horizontal,angle_vertical,fov_horizontal,fov_vertical):
        s.x = x
        s.y = y
        s.z = z

        s.angle = hv(angle_horizontal,angle_vertical)
        s.fov = hv(fov_horizontal,fov_vertical)

def draw_point(point):
    point_size = 0.0
    circle = False
    p = point
    if p.d.h >= 1 or p.d.h <= -1 or p.d.v >= 1 or p.d.v <= -1:
        pass
    else:
        if circle == True:
            turtle.pu()
            turtle.goto(p.d.h*size,p.d.v*size-(point_size/2))
            turtle.color(colour)
            turtle.pd()
            turtle.circle(point_size)
            turtle.pu()
        else:
            turtle.pu()
            turtle.goto(p.d.h*size,p.d.v*size-(point_size/2))
            turtle.pd()
            turtle.color(colour)
            turtle.goto(p.d.h*size,p.d.v*size+(point_size/2))
            turtle.pu()

def draw_triangle(triangle):
    s = triangle
    turtle.fillcolor(s.colour)
    
    turtle.pu()
    turtle.goto(s.d3.h*size,s.d3.v*size)
    turtle.pd()
    
    turtle.begin_fill()
    turtle.goto(s.d1.h*size,s.d1.v*size)
    turtle.goto(s.d2.h*size,s.d2.v*size)
    turtle.goto(s.d3.h*size,s.d3.v*size)
    turtle.end_fill()
    turtle.pu()
    
def draw_square(square):
    s = square
    turtle.fillcolor(s.colour)
    
    turtle.pu()
    turtle.goto(s.d4.h*size,s.d4.v*size)
    turtle.pd()
    
    turtle.begin_fill()
    turtle.goto(s.d1.h*size,s.d1.v*size)
    turtle.goto(s.d2.h*size,s.d2.v*size)
    turtle.goto(s.d3.h*size,s.d3.v*size)
    turtle.goto(s.d4.h*size,s.d4.v*size)
    turtle.end_fill()
    turtle.pu()
        
# some imports
from operator import attrgetter # used for sorting lists
import turtle
import math
import time # used for controlling fps
from functools import partial

# seting the canvas size for the turtle
screen = turtle.Screen()
size = 10
turtle.setworldcoordinates(-size,-size,size,size)
screen.colormode(255)

move_speed = 0.1
look_speed = 0.6

colour = [0,0,0] 
turtle.color(colour)

# useful stuff for turtle
turtle.pensize(3)
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0)
turtle.bgcolor("white")

#render_distance = 20
class button():
    def __init__(s,press,key):
        s.press = press
        s.key = key
        
press_w = button(False,"w")
press_s = button(False,"s")
press_a = button(False,"a")
press_d = button(False,"d")
press_z = button(False,"z")
press_x = button(False,"x")

press_r = button(False,"r")
press_f = button(False,"f")
press_e = button(False,"e")
press_q = button(False,"q")

press = [press_w,press_s,press_a,press_d,
         press_z,press_x,
         press_r,press_f,press_e,press_q]

#          x y z a a f f 
c = camera(10,5,0,0,0,90,90)
m = mouse(0,0)

#              x y z   x y z
t1 = triangle([0,0,3],[0,3,0],[3,0,0],[255,0,0])
t2 = triangle([0,0,-3],[0,3,0],[3,0,0],[0,255,0])
t3 = triangle([0,0,-3],[0,3,0],[-3,0,0],[0,0,255])
t4 = triangle([0,0,3],[0,3,0],[-3,0,0],[255,255,255])

t5 = triangle([0,0,3],[0,-3,0],[3,0,0],[0,255,255])
t6 = triangle([0,0,-3],[0,-3,0],[3,0,0],[255,0,255])
t7 = triangle([0,0,-3],[0,-3,0],[-3,0,0],[255,255,0])
t8 = triangle([0,0,3],[0,-3,0],[-3,0,0],[0,0,0])

shapes = [t1,t2,t3,t4,t5,t6,t7,t8]
  
cube1 = cube(5,0,5,1,"red")
cube2 = cube(5,0,6,1,"blue")
cube3 = cube(6,0,7,1,"green")

cubeBIG = cube (30,10,30,20,"orange")
objects = [cube1,cube2,cube3]#,cubeBIG]
        
for i in range(len(objects)):
    if objects[i].shape == "cube":
        for j in range(len(objects[i].s)):
            shapes.append(objects[i].s[j])


grid = 30
grid_spacing = 4
point_render_distance = 20
for x in range(-grid,grid,grid_spacing):
    for z in range(-grid,grid,grid_spacing):
        p = point(x,0,z)
        shapes.append(p)



def mouse_position(event):
    m.x = event.x - 480
    m.y = event.y - 400


canvas = turtle.getcanvas()   
running= True
while running == True: 
    canvas.bind('<Motion>',mouse_position)
    
                
    screen.listen()

    turtle.pensize(2)
    turtle.goto(0,-0.2)
    turtle.pd()
    turtle.circle(0.4)
    turtle.pu()
    turtle.pensize(3)
    
    screen.update()
    turtle.clear()
    
    for i in range(len(shapes)):
        if shapes[i].shape == "triangle":
            update_triangle(shapes[i],c)
        elif shapes[i].shape == "square":
            update_square(shapes[i],c)
        elif shapes[i].shape == "point":
            update_point(shapes[i],c)
            pass

    shapes = sorted(shapes, key= attrgetter('pc_distance'))
    shapes.reverse()

    for i in range(len(shapes)):
        if shapes[i].shape == "triangle":
            draw_triangle(shapes[i])
        elif shapes[i].shape == "square":
            draw_square(shapes[i])
        elif shapes[i].shape == "point":
            if shapes[i].pc_distance <= point_render_distance :
                draw_point(shapes[i])

    input_handler(c,m)
    for i in range(len(press)):
        turtle.onkeypress(partial(input_on,press[i]),press[i].key)
        turtle.onkeyrelease(partial(input_off,press[i]),press[i].key)

    

    




    




