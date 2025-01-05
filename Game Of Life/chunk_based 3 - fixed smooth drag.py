def random_rgb(): return(random.randint(0,255),random.randint(0,255),random.randint(0,255))

def draw_dot(x,y,colour = "red",size = 3):
    turtle.color(colour)
    turtle.goto(x,y)
    turtle.dot(size)

def draw_pixel(x,y,colour = "black"):
    if (x+pan_x*zoom) >= -max_size and (x+pan_x*zoom) <= max_size:
        if (y+pan_y*zoom) >= -max_size and (y+pan_y*zoom) <= max_size:
            X = x/zoom + pan_x
            Y = y/zoom + pan_y
            turtle.setpos(X+0/zoom,Y+0/zoom)
            turtle.fillcolor(colour)
            turtle.begin_fill()
            turtle.setpos(X+1/zoom,Y+0/zoom)
            turtle.setpos(X+1/zoom,Y+1/zoom)
            turtle.setpos(X+0/zoom,Y+1/zoom)
            turtle.setpos(X+0/zoom,Y+0/zoom)
            turtle.end_fill()

def test(n,b,p = 5):
    weight = 0
    for i in range(p):
        if n%(b**i) == 0:
            weight += 1
    return(weight)

def draw_grid():
    turtle.pensize(0)

    percent = 1-max_size/30
    rgb_value = 255 - int(255 * percent)
    if rgb_value <= 255:
        turtle.color(rgb_value,rgb_value,rgb_value)
        
        for y in range(-max_size,max_size,1):
            if pan_y > 0: y -= round(zoom * pan_y)
            if pan_y < 0: y -= round(zoom * pan_y) - 1
            
            turtle.setpos(-max_size/zoom,y/zoom + pan_y)
            turtle.pd()
            turtle.setpos(+max_size/zoom,y/zoom + pan_y)
            turtle.pu()
            
        for x in range(-max_size,max_size,1):
            if pan_x > 0: x -= round(zoom * pan_x) 
            if pan_x < 0: x -= round(zoom * pan_x) - 1
            
            turtle.setpos(x/zoom + pan_x,-max_size/zoom)
            turtle.pd()
            turtle.setpos(x/zoom + pan_x,+max_size/zoom)
            turtle.pu()
    

def draw_visable(colour = "red", size = None):
    if size == None:
        try: size = c_size
        except: pass
    ms =  int(math.ceil(size * 1))
    turtle.color("red")
    turtle.setpos(-ms,-ms)
    turtle.pd()
    turtle.setpos(-ms,+ms)
    turtle.setpos(+ms,+ms)
    turtle.setpos(+ms,-ms)
    turtle.setpos(-ms,-ms)
    turtle.pu()

def add_pixel(x,y):
    x = round(zoom*(x - pan_x) - 0.5)
    y = round(zoom*(y - pan_y) - 0.5)
    import random
    rgb = random_rgb()
    demo.append([x,y,rgb])

import turtle
import math
import time as Time
import random

w_size = 800 # pixel size of window
c_size = 5 # coordinate size in window

turtle.setup(w_size ,w_size)
turtle.setworldcoordinates(-c_size,-c_size,c_size,c_size)

turtle.hideturtle()

turtle.tracer(False)
turtle.speed(0)
turtle.pu()

turtle.Screen().colormode(255)

#demo = []
demo = [ [0,0,"red"],[1,0,"blue"],[0,1,"blue"],[-1,0,"blue"],[0,-1,"blue"]]
#demo = [[0,0,"red"]]

# populating
for i in range(100):
    s = 20
    x = random.randint(-s,s)
    y = random.randint(-s,s)
    p = [x,y,random_rgb()]
    demo.append(p)

mouse_scroll_value = [0]
def mouse_scroll(event):
    s = 0
    if event.delta > 0: s = +0.05
    if event.delta < 0: s = -0.05
    mouse_scroll_value[0] = -s


right_mouse_position = [0,0]
def right_button_down(event):
    x = +(event.x - 0.5*w_size) * (c_size/w_size) * 2 * zoom
    y = -(event.y - 0.5*w_size) * (c_size/w_size) * 2 * zoom 
    right_mouse_position[0] = x
    right_mouse_position[1] = y

drag = [0,0]
def right_button_drag(event):
    x = +(event.x - 0.5*w_size) * (c_size/w_size) * 2 * zoom 
    y = -(event.y - 0.5*w_size) * (c_size/w_size) * 2 * zoom 
  
    drag[0] = x - right_mouse_position[0]
    drag[1] = y - right_mouse_position[1]

drag_carry = [0,0]
release = [False]
def right_button_up(event):
    x = +(event.x - 0.5*w_size) * (c_size/w_size) * 2 * zoom
    y = -(event.y - 0.5*w_size) * (c_size/w_size) * 2 * zoom

    drag_carry[0] += x - right_mouse_position[0]
    drag_carry[1] += y - right_mouse_position[1]
    release = [True]

    
    

        

    
    
zoom =  1
pan_x = 0
pan_y = 0
while True:

    
    turtle.getcanvas().bind('<Button-3>',right_button_down)
    turtle.getcanvas().bind('<B3-Motion>',right_button_drag)
    pan_x = drag[0]
    #pan_x += drag_carry[0]
    
    turtle.getcanvas().bind('<ButtonRelease-3>',right_button_up)




    #pan_y = drag[1] 
    
    #drag = [0,0]
    
    time = Time.time()
    
    turtle.Screen().update()
    turtle.clear()
    
    #turtle.Screen().listen()
    turtle.Screen().onclick(add_pixel,1)

    # mouse wheel zoom scroll stuff
    turtle.getcanvas().bind('<MouseWheel>',mouse_scroll)
    zoom += mouse_scroll_value[0] * zoom
    if zoom < 1: zoom = 1
    mouse_scroll_value[0] = 0

    

    demo_size = 4
    #max_size = int(math.ceil(c_size * zoom) + 1)
    max_size = int(math.ceil(demo_size * zoom))

    draw_grid()
    
    for p in demo: draw_pixel(*p)

    # square view
    draw_visable("red",demo_size)

    frame_time = Time.time() - time
    #print(frame_time)
    

















