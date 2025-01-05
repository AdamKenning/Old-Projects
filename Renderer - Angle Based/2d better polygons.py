# simple camera controlls via mouse
def move_click(x,y):
    cam.x = (x - offset_x)/scale
    cam.y = (y - offset_y)/scale
def look_click(x,y):
    x= (x - offset_x)/scale
    y= (y - offset_y)/scale
    cam.angle = get_angle2(cam.x,cam.y,x,y)
        
# camera movement only up here so its out of the way
def forward():
    cam.x += (cos(cam.angle) * 0.5)
    cam.y += (sin(cam.angle) * 0.5)    
def backward():
    cam.x -= (cos(cam.angle) * 0.5)
    cam.y -= (sin(cam.angle) * 0.5)
    
def left():
    cam.x -= (sin(cam.angle) * 0.5)
    cam.y += (cos(cam.angle) * 0.5) 
def right():
    cam.x += (sin(cam.angle) * 0.5)
    cam.y -= (cos(cam.angle) * 0.5) 
    
# camera rotation
def deosil(): #deosil #clockwise
    cam.angle = in_angle((cam.angle - 10))
def widdershins(): #widdershins #counter clockwise
    cam.angle = in_angle((cam.angle + 10))
    
# useful functions cause python handles trigonometry weirdly
def sin(num):
    num = math.sin(math.radians(num))
    return(num)

def cos(num):
    num = math.cos(math.radians(num))
    return(num)

def tan_min(num1,num2):
    num = math.degrees(math.atan2(num1,num2))
    return(num)

# function for returning distance
def get_distance(a,b):
    d_x = abs(a.x - b.x)
    d_y = abs(a.y - b.y)
    d = math.sqrt(d_x**2 + d_y**2)
    return(d)

def get_distance2(ax,ay,bx,by):
    d_x = abs(ax - bx)
    d_y = abs(ay - by)
    d = math.sqrt(d_x**2 + d_y**2)
    return(d)

# functions for returning angle between two points
def get_angle(a,b):
    d_x = a.x - b.x
    d_y = a.y - b.y
    angle = tan_min(d_y,d_x)
    return(angle)

def get_angle2(ax,ay,bx,by):
    d_x = bx - ax
    d_y = by - ay
    angle = tan_min(d_y,d_x)
    return(angle)

def in_angle(angle):
    if angle > 180:
        angle = angle - 2*180
    elif angle < -180:
        angle = angle + 2*180
    return angle
        

# sorts list_a and does the same operation to list_b as it does to list_a      
def list_sort(list_a,list_b,list_c,list_d,list_e):
    finished = False
    while finished == False:
        finished = True
        for i in range(len(list_a)-1):
            if list_a[i] > list_a[i+1]:
                finished = False

                buffer_a = list_a[i]
                del list_a[i]
                list_a.insert(i+1,buffer_a)
                
                buffer_b = list_b[i]
                del list_b[i]
                list_b.insert(i+1,buffer_b)

                if list_c == None:
                    pass
                else:
                    buffer_c = list_c[i]
                    del list_c[i]
                    list_c.insert(i+1,buffer_c)

                if list_d == None:
                    pass
                else:
                    buffer_d = list_d[i]
                    del list_d[i]
                    list_d.insert(i+1,buffer_d)
                    
                if list_e == None:
                    pass
                else:
                    buffer_e = list_e[i]
                    del list_e[i]
                    list_e.insert(i+1,buffer_e)
                    
# defines partilces/ objects
class polygon:
    def __init__(self,x,y,angle,radius,colour,sides):
        self.x = x
        self.y = y
        self.angle = angle
        self.radius = radius
        self.colour = colour
        self.sides = sides

        self.face = []

        self.update_vertices()
        self.update_faces()
        
    def update_vertices(self):
        self.vertices = [] # a list of the x & y of each vertex
        
        theta = (360/self.sides)/2
        hypotenuse = self.radius/cos(theta) # the distance from center to vertex (h for hypotenuse)
        for i in range(self.sides):
            interior_angle = (((360/self.sides)/2)+(i*(360/self.sides))) # the interior angle for each point on a arbitrary sided shape
            vertex = [(self.x+(cos(self.angle+interior_angle)*hypotenuse)),
                      (self.y+(sin(self.angle+interior_angle)*hypotenuse))] # the x & y values for each point
            self.vertices.append(vertex)

        self.lines = []
        for i in range(len(self.vertices)):
            self.vertices[i-1][0] = round(self.vertices[i-1][0],2)
            self.vertices[i-1][1] = round(self.vertices[i-1][1],2)
            v1 = self.vertices[i-1]
            v2 = self.vertices[i]
            self.lines.append([v1,v2])
            #self.lines.append([self.vertices[i-1],self.vertices[i]])
            
    def update_faces(self):
        self.faces = [] # a list of the x & y of each vertex
        
        theta = 0
        hypotenuse = self.radius # the distance from center to vertex (h for hypotenuse)
        for i in range(self.sides):
            interior_angle = (i*(360/self.sides)) # the interior angle for each point on a arbitrary sided shape
            face = [(self.x+(cos(self.angle+interior_angle)*hypotenuse)),
                    (self.y+(sin(self.angle+interior_angle)*hypotenuse))] # the x & y values for each point
            self.faces.append(face)

# gets the percentage of the screen the polygons take up
def get_angles(polygons,camera):
    c = camera
    for i in range(len(polygons)):
        p = polygons[i]
        p.pangles = []
        p.decimal = []
        for j in range(len(p.lines)):
            a = p.lines[j][0]
            b = p.lines[j][1]

            a_angle = in_angle( (get_angle2(c.x,c.y,a[0],a[1]) - c.angle))          
            b_angle = in_angle( (get_angle2(c.x,c.y,b[0],b[1]) - c.angle))
                   
            ab_angle = [a_angle,b_angle]
            p.pangles.append(ab_angle)
            
            a_dec = a_angle/(c.fov/2)
            b_dec = b_angle/(c.fov/2)
            
            ab_decimal = [a_dec,b_dec]

            p.decimal.append(ab_decimal)         

# orders the polygons & all their faces,vertices, faces,lines etc inside them
def order_polygons(polygons,camera):
    # ordering the whole polygons against each other
    polygons_distance = []
    for i in range(len(polygons)):
        distance = get_distance(polygons[i],camera)
        polygons_distance.append(distance)
    list_sort(polygons_distance,polygons,None,None,None)

    # ordering the faces of each polygon against each face in the same polygon
    for i in range(len(polygons)):
        p = polygons[i]
        faces_distance = []
        for j in range(len(polygons[i].faces)):
            x = p.faces[j][0]
            y = p.faces[j][1]
            distance = get_distance2(x,y,camera.x,camera.y)
            faces_distance.append(distance)
            
        list_sort(faces_distance,p.faces,p.vertices,p.lines,p.decimal)
               
# defines the camera        
class camera:
    def __init__(self,x,y,angle,fov,depth,colour):
        self.x = x
        self.y = y
        self.angle = angle
        self.fov = fov
        self.depth = depth
        self.colour = colour

        self.update_cam()
        
    def update_cam(self): # basically all the coordiantes for displaying the visaul camera image
        self.screen = 2*(sin(self.fov/2)*self.depth)
        
        self.endMx = (self.x+(cos(self.angle)*self.depth))
        self.endMy = (self.y+(sin(self.angle)*self.depth))

        self.endRx = (self.endMx+(cos(self.angle+90)*(self.screen/2)))
        self.endRy = (self.endMy+(sin(self.angle+90)*(self.screen/2)))

        self.endLx = (self.endMx+(cos(self.angle-90)*(self.screen/2)))
        self.endLy = (self.endMy+(sin(self.angle-90)*(self.screen/2)))

# draws the camera    
def draw_camera(camera):
    dot_size = 0.08
    c = camera
    turtle.pu()
    turtle.color(c.colour)
    turtle.goto((c.x*scale)+offset_x,(c.y*scale)+offset_y)
    
    turtle.pd()
    turtle.goto((c.endMx*scale)+offset_x,(c.endMy*scale)+offset_y)
    turtle.goto((c.endRx*scale)+offset_x,(c.endRy*scale)+offset_y)
    turtle.goto((c.x*scale)+offset_x,(c.y*scale)+offset_y)
    turtle.goto((c.endLx*scale)+offset_x,(c.endLy*scale)+offset_y)
    turtle.goto((c.endMx*scale)+offset_x,(c.endMy*scale)+offset_y)
    turtle.pu()
    
    turtle.color("red")
    turtle.goto((c.endLx*scale)+offset_x,((c.endLy-(dot_size))*scale)+offset_y)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(dot_size*scale)
    turtle.end_fill()
    turtle.pu()
    
    turtle.color("green")
    turtle.goto((c.endRx*scale)+offset_x,((c.endRy-(dot_size/2))*scale)+offset_y)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(dot_size*scale)
    turtle.end_fill()
    turtle.pu()
    
# draws the polygons in a top-down view
def temp_draw_polygons(polygons):
    turtle.color("black")
    turtle.pu()
    turtle.goto((+size*scale)+offset_x,(+size*scale)+offset_y)
    turtle.pd()
    turtle.goto((+size*scale)+offset_x,(-size*scale)+offset_y)
    turtle.goto((-size*scale)+offset_x,(-size*scale)+offset_y)
    turtle.goto((-size*scale)+offset_x,(+size*scale)+offset_y)
    turtle.goto((+size*scale)+offset_x,(+size*scale)+offset_y)
    turtle.pu()
    for i in range(len(polygons)):
        p = polygons[i]

        Top = math.ceil(len(p.vertices)/2)

        turtle.color(p.colour)
        for j in range(len(p.vertices)):
            if j >= Top:
                turtle.color(255, 158, 247)
            turtle.pu()
            '''
            turtle.goto(p.faces[j][0],p.faces[j][1])
            turtle.write(j)
            '''
            turtle.goto((p.lines[j][0][0]*scale)+offset_x,
                        (p.lines[j][0][1]*scale)+offset_y)
            turtle.pd()
            turtle.goto((p.lines[j][1][0]*scale)+offset_x,
                        (p.lines[j][1][1]*scale)+offset_y)
            turtle.pu()
 
        turtle.goto(0,0)

def draw_view(polygons,camera):
    placement = size
    max_height = 5
    min_distance = 1
    height_lights = 1
    
    for i in range(len(polygons)-1,-1,-1):
        p = polygons[i]
        Top = math.ceil(len(p.faces)/2)
        for j in range(Top,-1,-1):
            if abs(p.decimal[j][0]-p.decimal[j][1]) < 5:
                distance1 = get_distance2(p.lines[j][0][0],p.lines[j][0][1],camera.x,camera.y)
                distance2 = get_distance2(p.lines[j][1][0],p.lines[j][1][1],camera.x,camera.y)

                height1 = (max_height/distance1 if distance1 > min_distance else max_height)
                height2 = (max_height/distance2 if distance2 > min_distance else max_height)

                depth = j*(255/len(p.decimal))
                colour = []
                for i in range(3):
                    colour.append(round((p.colour[i] + depth)/2))
                turtle.color(colour)
                turtle.fillcolor(colour)

                turtle.pu()
                turtle.goto(p.decimal[j][0]*-size,size+height1-placement)
                
                turtle.pd()
                turtle.begin_fill()
                turtle.goto(p.decimal[j][1]*-size,size+height2-placement)
                turtle.goto(p.decimal[j][1]*-size,size-height2-placement)
                turtle.goto(p.decimal[j][0]*-size,size-height1-placement)
                turtle.goto(p.decimal[j][0]*-size,size+height1-placement)
                turtle.end_fill()
                turtle.pu()

    turtle.color("green")
    turtle.begin_fill()
    turtle.goto(-size - height_lights,size + height_lights-placement)
    turtle.goto(-size + height_lights,size + height_lights-placement)
    turtle.goto(-size + height_lights,size - height_lights-placement)
    turtle.goto(-size - height_lights,size - height_lights-placement)
    turtle.goto(-size - height_lights,size + height_lights-placement)
    turtle.end_fill()

    turtle.color("red")
    turtle.begin_fill()
    turtle.goto(size + height_lights,size + height_lights-placement)
    turtle.goto(size - height_lights,size + height_lights-placement)
    turtle.goto(size - height_lights,size - height_lights-placement)
    turtle.goto(size + height_lights,size - height_lights-placement)
    turtle.goto(size + height_lights,size + height_lights-placement)
    turtle.end_fill()
    turtle.pu()
                   
# some imports
import turtle
import math
import time

# seting the canvas size for the turtle
screen = turtle.Screen()
size = 10
turtle.setworldcoordinates(-size,-size,size,size)
screen.colormode(255)

# for drawing map + camera
scale = 1/5
offset_x = -size * (1-scale)
offset_y = size * (1-scale)
    
# useful stuff for turtle
turtle.pensize(1)
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0)
turtle.bgcolor(253, 237, 243)

# camera
cam = camera(5,0,180,90,1,[50,50,50])
cam.angle = 0
# particles
aaa = polygon(0,0,0,6,[86, 91, 175],200)
bbb = polygon(4,4,0,0.6,[240, 173, 40],3)
ccc = polygon(0,0,0,1,[0, 0, 0],4)
ddd = polygon(-4,4,0,1,[165, 203, 67],5)
eee = polygon(-4,-4,0,1,[82, 175, 230],6)
fff = polygon(4,-4,0,1,[246, 82, 71],8)

test = polygon(0,0,0,size,[0, 0, 0],4)


polygons = [bbb,ccc,ddd,eee,fff]
#polygons = [aaa,test]

running = True
while running == True:
    time.sleep(0.01)
    
    # updating the screen & "listening" for inputs
    screen.update()
    screen.listen()
    turtle.clear()

    # updating all code related items
    cam.update_cam()
    for i in range(len(polygons)):
        p = polygons[i]
        p.update_vertices()
        p.update_faces()
        
    get_angles(polygons,cam) 
    order_polygons(polygons,cam)

    # displaying the screen
    temp_draw_polygons(polygons)
    draw_camera(cam)
    draw_view(polygons,cam)
    
    
    #temp_draw_polygons(polygons)
    
    # taking in inputs
    turtle.onkeypress(forward,"w")
    turtle.onkeypress(backward,"s")
    turtle.onkeypress(left,"a")
    turtle.onkeypress(right,"d")

    turtle.onkeypress(deosil,"e")
    turtle.onkeypress(widdershins,"q")

    screen.onclick(move_click,1)
    screen.onclick(look_click,3)
            
    '''
    for i in range(len(polygons)):
        polygons[i].angle += 0.7
        pass
    '''
    #screen.update()
    #time.sleep(10000)

    
########### fix being on right side half way up looking in




































        
