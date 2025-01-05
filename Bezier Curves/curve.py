import math
import turtle

screensize = 500 # squared
turtle.setworldcoordinates(-screensize, -screensize, screensize, screensize)

turtle.hideturtle()
turtle.speed(0)
turtle.pensize(1)

center_on_line    = True
draw_points       = True
draw_axis         = True

speed = 1 # 0 = fastest
point_radius = 3 # size of points
enlarge = 100
incriment = 200  # "quality"

#          x y
point_a = [1,1]
point_b = [1,4]
point_c = [4,2]
point_d = [-1,1] 

p = [point_a,point_b,point_c,point_d]

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

# finding displacement to center line
if center_on_line == True:
  displacement = [((sum(l3[0])/len(l3[0]))*enlarge),((sum(l3[1])/len(l3[1]))*enlarge)]
else:
  displacement = [0,0]

if draw_axis == True: 
  # drawing the x/y axis
  turtle.penup()
  turtle.goto(((-screensize*enlarge)-displacement[0]),(0-displacement[1]))
  turtle.pendown()
  turtle.goto(((+screensize*enlarge)-displacement[0]),(0-displacement[1]))         

  turtle.penup()
  turtle.goto(0-displacement[0],((-screensize*enlarge)-displacement[1]))
  turtle.pendown()
  turtle.goto(0-displacement[0],((+screensize*enlarge)-displacement[1])) 
  turtle.penup()
else:
  pass


if draw_points == True:
  # drawing the points
  i = 0
  for i in range ((len(p)-1),-1,-1):
    turtle.penup()
    turtle.goto((p[i][0]*enlarge)-displacement[0],((p[i][1]*enlarge)-displacement[1])-point_radius)
    turtle.pendown()
    turtle.circle(point_radius)
else:
  pass


turtle.speed(speed)
  
# drawing the line
i = 0
for i in range (0,(incriment+1),1):
  turtle.goto(((l3[0][i]*enlarge)-displacement[0]),((l3[1][i]*enlarge)-displacement[1]))
































