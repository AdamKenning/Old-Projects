# the class for every planet
class planet:
    def __init__(self,name,colour,mass,radius,xx,yy,vx,vy,fx,fy):
        self.name = name
        self.colour = colour
        self.mass = mass*sm
        self.radius = radius * au
        self.xx = xx * au
        self.yy = yy * au
        self.vx = vx 
        self.vy = vy 
        self.fx = fx
        self.fy = fy
    def print(self):
        print()
        print("name   = ",self.name)
        print("colour = ",self.colour)
        print("mass   = ",self.mass)
        print("radius = ",self.radius)
        print("xy     = ",self.xx,",",self.yy)
        print("vxy    = ",self.vx,",",self.vy)
        print("fxy    = ",self.fx,",",self.fy)
        print()
        
# useful trigonometry functions
def sine(num):
    num = math.sin(math.radians(num))
    return(num)

def cosine(num):
    num = math.cos(math.radians(num))
    return(num)

def tan_min1(num1,num2):
    num = math.degrees(math.atan2(num1,num2))
    return(num)

# function to get the force in newtons for each planet
def get_force(p_list):
  for j in range(len(p_list)):
    p = p_list[j]
    p.fx = 0
    p.fy = 0
    for i in range(len(p_list)):
      distance = math.sqrt(((p.xx-p_list[i].xx)**2)+((p.yy-p_list[i].yy)**2)) # returns distance in 2d space
      distance_x = abs(p.xx-p_list[i].xx) # returns distance on a line
      distance_y = abs(p.yy-p_list[i].yy) # returns distance on a line
      if distance != 0:
        if distance_x != 0 :
          cos_theta = cosine(tan_min1(distance_y,distance_x))
          force = gc*((p.mass*p_list[i].mass)/((distance_x**2)+(distance_y**2))) # total force (hypotenuse)
          direction_x = -((p.xx-p_list[i].xx)/abs(p.xx-p_list[i].xx)) # returns if the latter (p_list[i]) is greater or not
          
          force_x = cos_theta * force * direction_x # x axis component of force & direction (+/-)
        else:
          force_x = 0
          
        if distance_y != 0 :
          cos_theta = sine(tan_min1(distance_y,distance_x))
          force = gc*((p.mass*p_list[i].mass)/((distance_x**2)+(distance_y**2))) # total force (hypotenuse)
          direction_y = -((p.yy-p_list[i].yy)/abs(p.yy-p_list[i].yy)) # returns if the latter (p_list[i]) is greater or not
          
          force_y = cos_theta * force * direction_y # y axis component of force & direction (+/-)
        else:
          force_y = 0
      else:
        force_x = 0
        force_y = 0
      p.fx += force_x
      p.fy += force_y

# updates the positions of every planet		
def update(p_list):
    for i in range(len(p_list)):
        p = p_list[i]
        
        cull_f_v(p)
        
        p_displacement_x = ((p.vx*ti)+(0.5*(p.fx/p.mass)*(ti**2)))
        p_velocity_x = p_displacement_x/ti

        p_displacement_y = ((p.vy*ti)+(0.5*(p.fy/p.mass)*(ti**2)))
        p_velocity_y = p_displacement_y/ti

        p.xx = p.xx + p_displacement_x
        p.yy = p.yy + p_displacement_y
        
        p.vx = p_velocity_x
        p.vy = p_velocity_y

# draws every planet in turtle
def draw(p_list):
    for i in range(len(p_list)):
        p = p_list[i]
        
        turtle.pu()
        turtle.color(p.colour[0],p.colour[1],p.colour[2])
        turtle.goto(p.xx,p.yy-p.radius) # going to the correct coordinates
        turtle.pd()
        
        turtle.fillcolor(p.colour[0],p.colour[1],p.colour[2]) # setting the correct colour
        
        turtle.begin_fill()
        turtle.circle(p.radius) # creating an appropriately sized cirlce 
        turtle.end_fill()
        
        turtle.pu()
        turtle.goto(0,0)

def bounce(p_list): # litteraly just bounces the plants off the bounding box walls
    if Bounce == True:
        for i in range(len(p_list)):
            loss_in_v = 1.5
            p = p_list[i]
            if p.xx > size - p.radius:
                p.xx = size - p.radius
                p.vx = -p.vx/loss_in_v          
            if p.xx < -size + p.radius:
                p.xx = -size + p.radius
                p.vx = -p.vx/loss_in_v
            if p.yy > size - p.radius:
                p.yy = size - p.radius
                p.vy = -p.vy/loss_in_v
            if p.yy < -size + p.radius:
                p.yy = -size + p.radius
                p.vy = -p.vy/loss_in_v
    if Gravity == True: # me testing something 
        for i in range(len(p_list)):
            p = p_list[i]
            p.vy = p.vy - 10*size/au

# some things to try and limit amount of "flicks"         
def cull_f_v(p):
    if limit_f == True:
        if p.fx > maximum_f:
            p.fx = maximum_f
        if p.fx < -maximum_f:
            p.fx = -maximum_f
        if p.fy > maximum_f:
            p.fy = maximum_f
        if p.fy < -maximum_f:
            p.fy = -maximum_f

    if limit_v == True:
        if p.vx > maximum_v:
            p.vx = maximum_v
        if p.vx < -maximum_v:
            p.vx = -maximum_v
        if p.vy > maximum_v:
            p.vy = maximum_v
        if p.vy < -maximum_v:
            p.vy = -maximum_v
            
    else:
        pass
    
# funtions for interatcting with the game engine
def small_planet(x,y):
    new_p = planet("small",[200,200,200],20,0.5,x/au,y/au,00,00,00,00)
    planet_list.append(new_p)
    
def medium_planet(x,y):
    new_p = planet("medium",[100,100,100],50,1,x/au,y/au,00,00,00,00)
    planet_list.append(new_p)
    
def negative(x,y):
    new_p = planet("negative",[25,25,25],-30,1,x/au,y/au,00,00,00,00)
    planet_list.append(new_p)

def giga_planet():
    new_p = planet("giga",[200,000,000],500,2,0,0,00,00,00,00)
    planet_list.append(new_p)
    
def wipe_planets():
    planet_list.clear()

# start of the actual program
################################################################################################################################

import math
import turtle
import time

Bounce = True
Gravity = False

# some things to try and limit amount of "flicks"
limit_f = True
maximum_f = 1e30
limit_v = True
maximum_v = 1e6

gc = 6.67408e-11 # gravitational constant
ti = 3.145e7*0.05 # base time incriment (1 tenth of a year ( in seconds) )
sm = 1.989e30 # solar mass ; mass of our sun (kg)
au = 1.496e11 # astronomical unit ; distance from earth to sun (m)

# useful stuff for turtle5
screen = turtle.Screen()
size = 50*au # sets size of screen (in terms of corner coordinates)
turtle.setworldcoordinates(-size,-size,size,size)
screen.colormode(255)

turtle.pensize(0)
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0)
turtle.bgcolor(40,40,40)

#              name   hex value  mass r xx yy vx vy fx fy
#base = planet("medium",[100,100,100],50,1,x/au,y/au,00,00,00,00)
base = planet("base",[100,100,100],50,1,00,00,00,00,00,00)

planet_list = [base]

running = True
while running == True:
    
    
    # listening for inputs 
    screen.onclick(small_planet,1) # left mouse button = small planet
    screen.onclick(medium_planet,3) # right mouse button = medium planet
    screen.onclick(negative,2) # middle mouse button = negative planet
    turtle.onkey(giga_planet,"g") # button "G" = giga mass planet
    turtle.onkey(wipe_planets,"r") # butoon "r" = removes all planets (use when it gets laggy)
    screen.listen()

    # calculations for every planet
    get_force(planet_list)
    update(planet_list)
    draw(planet_list)
    bounce(planet_list)

    # updating the screen, then clearing it for next itteration
    screen.update()
    time.sleep(0.01)
    turtle.clear()
    

















    
