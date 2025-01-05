def get_curve(a,b,c,d):
  p = [a,b,c,d]
  l1 = [[[],[]],[[],[]],[[],[]]]
  l2 = [[[],[]],[[],[]]]
  l3 = [[],[]]

  i = 0
  # making the first layer of lines
  for i in range (0,(incriment+1),1):   
    l1[0][0].append((i/incriment)*(p[1][0]-p[0][0])+p[0][0])
    l1[0][1].append((i/incriment)*(p[1][1]-p[0][1])+p[0][1])
      
    l1[1][0].append((i/incriment)*(p[2][0]-p[1][0])+p[1][0])
    l1[1][1].append((i/incriment)*(p[2][1]-p[1][1])+p[1][1])

    l1[2][0].append((i/incriment)*(p[3][0]-p[2][0])+p[2][0])
    l1[2][1].append((i/incriment)*(p[3][1]-p[2][1])+p[2][1])

  # making the second layer of lines    
  i = 0
  for i in range (0,(incriment+1),1):
    l2[0][0].append((i/incriment)*(l1[1][0][i]-l1[0][0][i])+l1[0][0][i])
    l2[0][1].append((i/incriment)*(l1[1][1][i]-l1[0][1][i])+l1[0][1][i])

    l2[1][0].append((i/incriment)*(l1[2][0][i]-l1[1][0][i])+l1[1][0][i])
    l2[1][1].append((i/incriment)*(l1[2][1][i]-l1[1][1][i])+l1[1][1][i])
    
  # making the third layer of lines
  i = 0
  for i in range (0,(incriment+1),1):
    l3[0].append((i/incriment)*(l2[1][0][i]-l2[0][0][i])+l2[0][0][i])
    l3[1].append((i/incriment)*(l2[1][1][i]-l2[0][1][i])+l2[0][1][i])

  return(p,l3)


def draw_curve(p,l3):
  # finding displacement to center line
  if center_on_line == True:
    displacement = [((sum(l3[0])/len(l3[0]))*enlarge),((sum(l3[1])/len(l3[1]))*enlarge)]
  else:
    displacement = [0,0]

  if draw_points == True:
      # drawing the points
    i = 0
    #for i in range ((len(p)-1),-1,-1):
    for i in range(1):
      turtle.penup()
      turtle.goto((p[i][0]*enlarge)-displacement[0],((p[i][1]*enlarge)-displacement[1])-point_radius)
      turtle.pendown()
      turtle.circle(point_radius)
  else:
    pass
    
  # drawing the line
  turtle.penup()
  turtle.goto(((l3[0][0]*enlarge)-displacement[0]),((l3[1][0]*enlarge)-displacement[1]))
  turtle.pendown()
  
  i = 0
  for i in range (0,(incriment+1),1):
    turtle.goto(((l3[0][i]*enlarge)-displacement[0]),((l3[1][i]*enlarge)-displacement[1]))
    

###############################################################################################

import math
import turtle
import random
import time
import copy

screen=turtle.Screen()
screensize = 50 # squared
turtle.setworldcoordinates(-screensize, -screensize, screensize, screensize)

turtle.bgcolor("black")
screen.colormode(255)
turtle.tracer(0)
turtle.hideturtle()
turtle.pensize(5)

#]turtle.hideturtle()
turtle.speed(0)

center_on_line = False
draw_points = False

speed = 0 # 0 = fastest
point_radius = 1 # size of points
enlarge = 1
incriment = 500  # "quality"


class line:
  def __init__(self,p1,p2,p3,p4):
    self.p1 = p1
    self.p2 = p2
    self.p3 = p3
    self.p4 = p4
  def p(self):
    print()
    print(self.p1)
    print(self.p2)
    print(self.p3)
    print(self.p4)


a = line([0,0],[0,0],[0,0],[0,0])


for i in range (100000):
  #a.p()
  #turtle.color([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
  rgb = [0,0,0]
  for j in range(3):
    x = (((i+j)*2))
    if x > 255:
      rgb[j] = 255-(x%255)
    else:
      rgb[j] = x  
  turtle.color([rgb[0],rgb[1],rgb[2]])
  
  if i%3 == 0:
    turtle.pensize(3)
    #turtle.color('red')
  elif i%3 == 1:
    turtle.pensize(3)
    #turtle.color('blue')
  else:
    turtle.pensize(3)
    #turtle.color('green')
  
  a.p1 = copy.deepcopy(a.p3)
  a.p2 = copy.deepcopy(a.p4)
  a.p3 = copy.deepcopy(a.p4)
  
  for i in range(2):
    a.p4[i] = random.randint(-50,50)

  draw_curve(((get_curve(a.p1,a.p2,a.p3,a.p4))[0]),((get_curve(a.p1,a.p2,a.p3,a.p4))[1]))
  screen.update()

  #time.sleep(0.1)




































