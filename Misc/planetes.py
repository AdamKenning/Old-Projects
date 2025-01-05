# defining these cause they a bitch with conversion the way python handles trigonometry
def sine(num):
    num = math.sin(math.radians(num))
    return(num)

def cosine(num):
    num = math.cos(math.radians(num))
    return(num)

# the defining thing of each planet
class planet:
    def __init__(self,radius,orbit,year,colour,R_angle):
        self.radius = radius
        self.orbit = orbit # distance from center
        self.year = year # basically how many years pass in the "total time"
        self.colour = colour # rgb value
        self.R_angle = R_angle # starts simulation with random rotations
    def properties(self):
        print()
        print("radius = ",self.radius)
        print("orbit radius = ",self.orbit)
        print("year  = ",self.year)
        print("colour  = ",self.colour)
        print("R_angle = ",self.R_angle)
        print()
        
# draws the planet with turtle
def draw_planet(planet,coords):
    turtle.penup()
    turtle.goto(coords[0],coords[1]-planet.radius)
    turtle.pendown()
    turtle.fillcolor(planet.colour[0],planet.colour[1],planet.colour[2])
    turtle.begin_fill()
    turtle.circle(planet.radius)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(coords[0],coords[1])

# just returns the current time in microsecons ie: 10:45 == 45mins * 60secs * 1000000microsecons + 10hours * 60   etc
# and the total time 
def get_time(seconds,minutes,hours):
    now = datetime.now()
    hour = int(now.strftime("%H"))
    mins = int(now.strftime("%M"))
    secs = int(now.strftime("%S"))
    micr = int(now.strftime("%f"))

    #print(hour,mins,secs,micr)
    total_time = (1000000)
    current_time = (micr)

    if seconds == True:
        total_time=1000000*60
        current_time= micr + 1000000*secs
        if minutes == True:
            total_time = 1000000*60*60
            current_time = micr + 1000000*secs + 1000000*60*mins
            if hours == True:
                total_time = 1000000*60*60*24
                current_time = micr + 1000000*secs + 1000000*60*mins + 1000000*60*60*hour
                
    return(total_time,current_time)

# uses trigonometry to get the coords for each planets center
def get_coords(time,planet):
    angle=(360/time[0])*(progression*planet.year)
    if random_angle == True:
        angle=(360/time[0])*(progression*planet.year)+planet.R_angle
    x=cosine(angle)*planet.orbit
    y=sine(angle)*planet.orbit
    return(x,y)
    
########################################################################################################
# some imports
import turtle
import math
from datetime import datetime
import time
import random

# define how long you want one "year" to be : 1 second, 1 minutes, 1 hour etc. when all are false, its 1 microsecond
seconds = True
minutes = False
hours = False
# all linked up to real world clock so 1 orbit of base planet == 60 seconds if only seconds is True :) 

# seting the canvas size for the turtle, -1000,1000 mark the coordinates of the corners of the screen
screen = turtle.Screen()
size = 900
turtle.setworldcoordinates(-size,-size,size,size)
screen.colormode(255)

# useful stuff for turtle
turtle.pensize(0)
turtle.color(10,10,10)
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0)
turtle.bgcolor(50,50,50)

# defining the planets 
base_planet=planet(10,100,0,[0,0,0],random.randint(0,360))#1) # ignore this one

sun = planet(50,0,0,[249,215,28],random.randint(0,360))
mercury = planet(2.44,100,4.147727,[26,26,26],random.randint(0,360))
venus   = planet(6.052,175,1.622222,[230,230,230],random.randint(0,360))
earth   = planet(6.371,225,1,[47,106,105],random.randint(0,360))
mars    = planet(3.390,275,0.531295,[153,61,0],random.randint(0,360))
jupiter = planet(69.911,400,0.083333,[176,127,53],random.randint(0,360))
saturn  = planet(58.232,550,0.034482,[176,143,54],random.randint(0,360))
uranus  = planet(25.362,700,0.0119047,[85,128,170],random.randint(0,360)) # ur anus*
neptune = planet(24.622,800,0.006060,[54,104,150],random.randint(0,360))
pluto   = planet(5,850,0.004032,[156,166,183],random.randint(0,360))


planetes=[sun,mercury,venus,earth,mars,jupiter,saturn,uranus,neptune,pluto]
random_angle = True # if true, planetes start at random rotations

# ignore this, its useful, but its an annoying af work around to another problem
prior_time = get_time(seconds,minutes,hours)[1]
progression = 0

# enter the simulation neo style
running = True
while running == True:
    # gets change in time since last cycle
    if prior_time != get_time(seconds,minutes,hours)[1]:
        if abs(get_time(seconds,minutes,hours)[1]-prior_time) > (get_time(seconds,minutes,hours)[0])/2:
            pass
        else:
            progression += abs(get_time(seconds,minutes,hours)[1]-prior_time)
        prior_time = get_time(seconds,minutes,hours)[1]
    #draw_planet(base_planet,get_coords(get_time(seconds,minutes,hours),base_planet))
        
    for i in range(len(planetes)):
        draw_planet(planetes[i],get_coords(get_time(seconds,minutes,hours),planetes[i]))

    turtle.goto(0,0)
    screen.update()
    turtle.clear()
    
















