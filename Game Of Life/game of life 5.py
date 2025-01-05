#standard rules:
# alive :
# <2 neighbours = death
# 2 - 3 neightboyrs = live
# >3 neighbours = death

# dead :
# 3 neighbours = live

class cell:
    def __init__(self,x,y,state,buffer):
        self.x = x
        self.y = y
        self.state = state
        self.buffer = buffer
    def print(self):
        print("xy = ",self.x,self.y," state = ",self.state," buffer = ",self.buffer)

def check_against(cell,cell_list,paramater):
    for i in range(len(cell_list)):
        if cell.x == cell_list[i].x:
            if cell.y == cell_list[i].y:
                if paramater == "s":
                    cell.state = cell_list[i].state
                elif paramater == "b":
                    cell.buffer = cell_list[i].buffer

def check_list(cell,cell_list):
    inside = False
    number = None
    for i in range(len(cell_list)):
        if cell.x == cell_list[i].x and cell.y == cell_list[i].y:
            inside = True
            number = i
    return(inside,number)

def print_list(cell_list):
    for i in range(len(cell_list)):
        cell_list[i].print()
        
def run_cycle():
    global alive
    alive_buffer = []
    
    for i in range(len(alive)):
        layer_1 = []
        
        for y in range(neighbour_search,-neighbour_search-1,-1):
            for x in range(-neighbour_search,neighbour_search+1,1):
                cell_temp = cell(alive[i].x+x,alive[i].y+y,None,None)
                check_against(cell_temp,alive,"s")
                #check_against(cell_temp,alive,"b")
                if cell_temp.buffer == None:
                    layer_1.append(cell_temp)
        print_list
        for j in range(len(layer_1)):
            layer_2 = []
            for y in range(neighbour_search,-neighbour_search-1,-1):
                for x in range(-neighbour_search,neighbour_search+1,1):
                    cell_temp = cell(layer_1[j].x+x,layer_1[j].y+y,0,0)
                    check_against(cell_temp,alive,"s")
                    layer_2.append(cell_temp)
                    
            alive_neighbours = 0
            for k in range(len(layer_2)):
                if (layer_1[j].x != layer_2[k].x or layer_1[j].y != layer_2[k].y) and layer_2[k].state >= alive_value: 
                    alive_neighbours += alive_neighbour_value


            
            if check_list(layer_1[j],alive_buffer)[0] == True:
                pass
            else:
                if layer_1[j].state >= alive_value:
                    if alive_neighbours <= under_population:
                        layer_1[j].buffer = 0
                    elif alive_neighbours >= over_population:
                        layer_1[j].buffer = 0
                    else:
                        layer_1[j].buffer = alive_value
                        alive_buffer.append(layer_1[j])
                else:
                    if alive_neighbours in range(lower_reproduction,upper_reproduction+1):
                        layer_1[j].buffer = alive_value 
                        alive_buffer.append(layer_1[j])
                    else:
                        layer_1[j].buffer = 0
    alive = []
    for k in range(len(alive_buffer)):
        alive.append(alive_buffer[k])

    for k in range(len(alive)):
        alive[k].state = alive_value
        alive[k].buffer = 0
    return(alive)

def pixel(x,y):
    global alive
    x = (round(x/zoom,0)) 
    y = (round(y/zoom,0)) 
    cell_temp = cell(x,y,1,None)
    if check_list(cell_temp,alive)[0] == True:
        del alive[check_list(cell_temp,alive)[1]]
    else:
        cell_temp = cell(x,y,1,None)
        alive.append(cell_temp)

def draw(cells,colour):
    turtle.color(colour)
    z = zoom/2
    for i in range(len(cells)):
        turtle.color(colour)

        x = (cells[i].x*zoom) 
        y = (cells[i].y*zoom) 
        
        turtle.pu()
        turtle.goto(x+z,y+z)
        turtle.pd()
        
        turtle.fillcolor([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
        
        turtle.begin_fill()
        turtle.goto(x+z,y-z)
        turtle.goto(x-z,y-z)
        turtle.goto(x-z,y+z)
        turtle.goto(x+z,y+z)

        turtle.end_fill()


def clear():
    global cells
    cells = []

def pause():
    global stopped
    if stopped == True:
        stopped = False
        turtle.bgcolor(back_colour)
    else:
        stopped = True
        turtle.bgcolor(pause_colour)
def clear():
    global alive
    alive = []
def zoom_in():
    global zoom
    zoom *= 2
def zoom_out():
    global zoom
    zoom /= 2

def up():
    global alive
    for i in range(len(alive)):
        alive[i].y -= zoom
def down():
    global alive
    for i in range(len(alive)):
        alive[i].y += zoom
def left():
    global alive
    for i in range(len(alive)):
        alive[i].x += zoom
def right():
    global alive
    for i in range(len(alive)):
        alive[i].x -= zoom
        
import turtle
import time
import random

screen = turtle.Screen()
size = 1000 # sets size of screen (in terms of corner coordinates)
turtle.setworldcoordinates(-size,-size,size,size)
screen.colormode(255)

turtle.pensize(0)
turtle.color(0,0,0)
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0)

back_colour = [50,50,50]
pause_colour = [100,100,100]

turtle.bgcolor(pause_colour)

#rules
neighbour_search = 1# distance around each cell, which a search is conducted
alive_neighbour_value = 1 # value of an alive neighbour
alive_value = 1 # value needed for a cell to be considered "alive"
# living cells dying
under_population = 1 # fewer than or equal to 1
over_population = 4 # greater than or equal to 4
# dead cells re-viving
lower_reproduction = 3 # fewer than  3
upper_reproduction = 3 # greater than 3

zoom = 20
speed = 20

alive = []

running = True
stopped = True

#time.sleep(1000)

while running == True:
    screen.onclick(pixel,1)

    turtle.onkeypress(up,'w')
    turtle.onkeypress(down,'s')
    turtle.onkeypress(left,'a')
    turtle.onkeypress(right,'d')
    
    turtle.onkeypress(pause,'t')
    turtle.onkeypress(clear,'c')
    turtle.onkeypress(zoom_in,'r')
    turtle.onkeypress(zoom_out,'e')
    
    draw(alive,[255,255,255])
    
    if stopped == False:
        time.sleep(1/speed)
        run_cycle()
        
    screen.listen()
    screen.update()
    turtle.clear()
    time.sleep(1/speed)








































        
        
        
