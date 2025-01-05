class cube:
    def __init__(s,x,y,z,radius):
        s.x = x
        s.y = y
        s.z = z
        s.r = radius


    def reset(s):
        p0 = [[s.x + s.r], #x
              [s.y + s.r], #y
              [s.z + s.r], #z
              [1]]
        
        p1 = [[s.x - s.r], #x
              [s.y + s.r], #y
              [s.z + s.r], #z
              [1]]
        
        p2 = [[s.x + s.r], #x
              [s.y - s.r], #y
              [s.z + s.r], #z
              [1]]
        
        p3 = [[s.x - s.r], #x
              [s.y - s.r], #y
              [s.z + s.r], #z
              [1]]

        p4 = [[s.x + s.r], #x
              [s.y + s.r], #y
              [s.z - s.r], #z
              [1]]
        
        p5 = [[s.x - s.r], #x
              [s.y + s.r], #y
              [s.z - s.r], #z
              [1]]

        p6 = [[s.x + s.r], #x
              [s.y - s.r], #y
              [s.z - s.r], #z
              [1]]
        
        p7 = [[s.x - s.r], #x
              [s.y - s.r], #y
              [s.z - s.r], #z
              [1]]

        s.points = [p0,p1,p2,p3,p4,p5,p6,p7]

class canonical_view_volume:
    def __init__(s,width,height,depth):
        s.r = +(width/2)
        s.l = -(width/2)

        s.t = +(height/2)
        s.b = -(height/2)

        s.n = +(depth/2)
        s.f = -(depth/2)
        
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

def mt(x,y,z):
    m = [[1,0,0,x],
         [0,1,0,y],
         [0,0,1,z],
         [0,0,0,1]]
    return(m)

def ms(x,y,z): # creates scaler matrix
  m = [[x,0,0,0],
       [0,y,0,0],
       [0,0,z,0],
       [0,0,0,1]]
  return(m)

def mr(x,y,z): # for rotating the matrix in each axis
    mx = [[      1,      0,      0,      0],
          [      0, cos(x), sin(x),      0],
          [      0,-sin(x), cos(x),      0],
          [      0,      0,      0,      1]]

    my = [[ cos(y),      0,-sin(y),      0],
          [      0,      1,      0,      0],
          [ sin(y),      0, cos(y),      0],
          [      0,      0,      0,      1]]

    mz = [[ cos(z), sin(z),      0,      0],
          [-sin(z), cos(z),      0,      0],
          [      0,      0,      1,      0],
          [      0,      0,      0,      1]]

    rotate = mxm(mxm(mx,my),mz)
    return(rotate)

def mxm(a,b): # multiplies two matrices
  result = [[sum(m*n for m,n in zip(a_row,b_col)) for b_col in zip(*b)] for a_row in a]
  return(result)

def pr(matrix): # prints matrix
  if len(matrix[0]) == 1:
      print("x = ",round(matrix[0][0],2))
      print("y = ",round(matrix[1][0],2))
      print("z = ",round(matrix[2][0],2))
      print()
  else:
      for i in range(len(matrix)):
          print(matrix[i])

import math
import turtle

size = 10
turtle.setworldcoordinates(-size/2,-size/2,+size/2,+size/2)
global t
t = turtle.Turtle()
t._tracer(0)
t.hideturtle()
t.screen.colormode(255)
t.pu()

c = cube(0,0,0,1)
c.reset()

a = [[5],[5],[5],[5]]
print(a)
r = mr(90,90,90)
print(r)
a = mxm(r,a)
print(a)

running = True
while running == True:
    t.screen.update()
    t.clear()
    for i in range(len(c.points)):       
        c.points[i] = mxm(mr(0.1,0,0),c.points[i])
        c.points[i] = mxm(mr(0,0.02,0),c.points[i])
        
        px = c.points[i][0][0]
        py = c.points[i][1][0]

        radius = 0.05
        
        t.goto(px,py - radius)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()

        


        
    
    









