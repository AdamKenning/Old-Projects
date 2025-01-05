# functions cause trigonometry in python is scuffed
def sine(num):
    num = math.sin(math.radians(num))
    return(num)

def cosine(num):
    num = math.cos(math.radians(num))
    return(num)

# gets the xy coordinates of all cornes of the defined shape "c"
def get_shape_corners(c):
  mid_of_side=[[],[]]
  for i in range (c[4]):
      mid_of_side[0].append(c[0]+(cosine(c[2]+((360/c[4])*i))*c[3]))
      mid_of_side[1].append(c[1]+(sine(c[2]+((360/c[4])*i))*c[3]))

  corners=[[],[]]
  for i in range(c[4]):
      corners[0].append(mid_of_side[0][i]+(cosine(c[2]+((360/c[4])*(i+1)))*c[3]))
      corners[1].append(mid_of_side[1][i]+(sine(c[2]+((360/c[4])*(i+1)))*c[3]))

  return(corners)

# gets a list of points on a side of shape "c"
def get_shape_points(c):
    corners = get_shape_corners(c)
    points=[]
    for i in range (c[4]):
        points.append([[],[]])
    for j in range(len(points)):
        for i in range (0,quality):
            points[j][0].append((i/quality)*(corners[0][j-1]-corners[0][j])+corners[0][j])
            points[j][1].append((i/quality)*(corners[1][j-1]-corners[1][j])+corners[1][j])
    return(points)

# gets 
def get_line(k):
    k_ends = [[k[0],k[1]],[]]
    k_ends[1].append((k[0])+(cosine(k[2]))*k[3])
    k_ends[1].append((k[1])+(sine(k[2]))*k[3])

    
    k_points = [[],[]]
    for i in range(quality):
        k_points[0].append((i/quality)*(k_ends[0][0]-k_ends[1][0])+k_ends[1][0])
        k_points[1].append((i/quality)*(k_ends[0][1]-k_ends[1][1])+k_ends[1][1])
        #print("i =",i," k_point x =",k_points[0][i]," k_points y =",k_points[1][i])
    return(k_ends,k_points)

# finds if and where a line intersects
def find_reflect(c,k,quality,error_margin):
    error = 1/error_margin
    intersect = []
    hold=777
    reflect = False
    temp_list=[]
    for l in range(len(get_line(k)[1][0])):
        #print("l =",l)
        for j in range (c[4]):
            for i in range(len(get_shape_points(c)[0][0])):
                #print("line = ",get_line(k)[1][0][l],get_line(k)[1][1][l])
                #print("shape= ",get_shape_points(c)[j][0][i],get_shape_points(c)[j][1][i])
                #print()
                
                temporary = math.sqrt((abs(get_line(k)[1][0][l]-get_shape_points(c)[j][0][i]))**2+(abs(get_line(k)[1][1][l]-get_shape_points(c)[j][1][i]))**2)
                temp_list.append(temporary)
                
                if temporary < hold:
                    hold = temporary
                    intersect = [[get_line(k)[1][0][l],get_line(k)[1][1][l]],[get_shape_points(c)[j][0][i],get_shape_points(c)[j][1][i]]]
                    if temporary <= error:
                        reflect=True
                else:
                    pass
                pass
    #print(sorted(temp_list))
    return(reflect,intersect,hold)
    ############### not getting the correct points    

    
def draw_shape(c):
    # draws the shape
    turtle.penup()
    turtle.goto(get_shape_corners(c)[0][0]*zoom,get_shape_corners(c)[1][0]*zoom)
    turtle.pendown()
    #turtle.circle(10)
    for i in range (c[4]):
      turtle.goto(get_shape_corners(c)[0][i]*zoom,get_shape_corners(c)[1][i]*zoom)
    turtle.goto(get_shape_corners(c)[0][0]*zoom,get_shape_corners(c)[1][0]*zoom)

    # extra bit to ensure turtle finishes drawing before stopping
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    
    
######################################################################################################

import turtle
import math

'''
x = x axis
y = y axis
θ = angle
r = radius
s = sides
'''

#    x y θ radius sides   <---- definitions of a regular 2d shape
c = [0,0,90,3,10]
#    0 1 2  3 4

#    x y θ length  <------- definitios for a line 
k = [2,0,30,10]
#    0 1 2  3

error_margin = 10
quality = 13

zoom = 30 # determine size of drawing
turtle.tracer(0)  # determine speed of drawing 
turtle.pensize(0) # width of lines


draw_shape(c)

# drawing circle where the "points" are

for j in range(c[4]):
    for i in range (quality-1,0,-1):
        turtle.penup()
        turtle.goto(get_shape_points(c)[j][0][i]*zoom,get_shape_points(c)[j][1][i]*zoom)
        turtle.pendown()
        turtle.circle(2)

for i in range(len(get_line(k)[1][0])):
        turtle.penup()
        turtle.goto(get_line(k)[1][0][i]*zoom,get_line(k)[1][1][i]*zoom)
        turtle.pendown()
        turtle.circle(2)
        
turtle.penup()
turtle.goto(find_reflect(c,k,quality,error_margin)[1][0][0]*zoom,find_reflect(c,k,quality,error_margin)[1][0][1]*zoom)
turtle.pendown()
turtle.circle(5)
turtle.penup()
turtle.goto(find_reflect(c,k,quality,error_margin)[1][1][0]*zoom,find_reflect(c,k,quality,error_margin)[1][1][1]*zoom)
turtle.pendown()
turtle.circle(5)

#print(get_shape_corners(c))
#print(get_shape_points(c))

print(find_reflect(c,k,quality,error_margin))

turtle.penup()
turtle.goto(0,0)



'''
c = [-30,0,90,5,3]
for i in range (5):
    draw_shape(c)
    c[4] += 1
    c[3] -= 0.7
    c[0] += 15
'''

turtle.exitonclick()














