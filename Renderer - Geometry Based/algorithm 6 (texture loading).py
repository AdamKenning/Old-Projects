def sin(num):
    num = math.sin(math.radians(num))
    return(num)

def cos(num):
    num = math.cos(math.radians(num))
    return(num)

def tan(num1,num2):
    num = math.degrees(math.atan2(num1,num2))
    return(num)

def sign(num):
    s = abs(num-0) / (num-0 + 10**-5) # 5 is prob overkill
    s = round(s)
    return(s)

# returns intersections of a ray
def get_intersects(a,b):
    inc_x = sign(b.x - a.x)
    dx    =  abs(b.x - a.x)

    inc_y = sign(b.y - a.y)
    dy    =  abs(b.y - a.y)

    xay = dx > dy
    cmpt = max(dx,dy)
    inc_d = -2*abs(dx-dy)
    inc_s =  2*min(dx,dy)

    err = inc_d + cmpt
    x = a.x
    y = a.y

    intersects = []
    while cmpt >= 0:
        p = point(x,y,0,0)
        
        intersects.append(p)
        cmpt -= 1
        if err >= 0 or xay:
            x += inc_x
        if err >= 0 or not(xay):
            y += inc_y
        if err >= 0:
            err += inc_d
        else:
            err += inc_s

    # dealing with uv
    for i in range(len(intersects)):
        p = intersects[i]
        percent = i/len(intersects)
        u = (percent * (b.u-a.u))+a.u
        v = (percent * (b.v-a.v))+a.v
        p.u = u
        p.v = v
        
    return(intersects)



# defiens a point
class point():
    def __init__(s,x,y,u,v):
        s.rx = x
        s.ry = y

        s.u = u
        s.v = v

        s.clicked = False
        s.change = False
        
    @property
    def x(s): return(round(s.rx))
    @property
    def y(s): return(round(s.ry))
    

class polygon():
    def __init__(s,fp,opacity):
        s.fp = fp
        
        s.opacity = opacity
        s.bp_buffer = []
        s.ap_buffer = []
     
    @property
    def bp(s):
        fp = s.fp
        new_bp = []
        
        for i in range(len(fp)):
            a = fp[i-1]
            b = fp[i]


            ab = get_intersects(a,b)
            new_bp.extend(ab)
        
        new_bp.extend(fp)
        return(new_bp)

    @property
    def ap(s):
        bp = s.bp
        new_ap = []
        new_ap.extend(bp)
        
        max_x = - float('inf')
        min_x = + float('inf')
        max_y = - float('inf')
        min_y = + float('inf')

        for i in range(len(bp)):
            x = bp[i].x
            y = bp[i].y

            if x > max_x : max_x = x
            if x < min_x : min_x = x
            if y > max_y : max_y = y
            if y < min_y : min_y = y

        array = []        
        for y in range(max_y - min_y + 1):
            row = []
            for x in range(max_x - min_x +1):
                row.append(None)
            array.append(row)
            
        added_points = [] # list to check against duplicates
        # adding the bp to the blank array
        for i in range(len(bp)):  
            x = bp[i].x-min_x
            y = bp[i].y-min_y

            if [x,y] not in added_points :
                added_points.append([x,y])
                array[y][x] = bp[i]

        # interpolating horizontally
        for y in range(len(array)):
            start = None # the acutal pointer towards where the start is 
            end = None
            start_found = 0 # a means of finding where the start is
            end_found = 0 # 0 means unfound, 2 means found, 1 is unsure

            for x in range(0,len(array[y]),+1):
                if (array[y][x] != None) and (start == None):
                    start = x  
            for x in range(len(array[y])-1,-1,-1):
                if (array[y][x] != None) and (end == None):
                    end = x

            if end - start > 1:
                for x in range(len(array[y])):
                    if x > start and x < end:
                        percent = (x - start) / (end - start)
                        
                        new_x = ((array[y][end].x - array[y][start].x)*(percent)) + array[y][start].x
                        new_y = y + min_y # doesnt matter will be replaced
          
                        u = ((array[y][end].u - array[y][start].u)*(percent)) + array[y][start].u

                        if array[y][x] != None:
                            v = array[y][x].v
                        else:
                            v = 0

                        p = point(new_x,new_y,u,v)

                        array[y][x] = p
                        
        # interpolating vertically now with the same array
        for x in range(len(array[0])):
            start = None
            end = None
            start_found = 0
            end_found = 0

            for y in range(0,len(array),+1):
                if (array[y][x] != None) and (start == None):
                    start = y

            for y in range(len(array)-1,-1,-1):
                if (array[y][x] != None) and (end == None):
                    end = y

            if end - start > 1:
                for y in range(len(array)):
                    if y > start and y < end:
                        percent = (y - start)/(end - start)

                        new_x = None
                        new_y = ((array[end][x].y - array[start][x].y)*(percent)) + array[start][x].y

                        v = ((array[end][x].v - array[start][x].v)*(percent)) + array[start][x].v

                        array[y][x].ry = new_y
                        array[y][x].v = v
 
                        new_ap.append(array[y][x])

        #remove duplicates
        filtered_ap = []
        xy_positions = []
        for i in range(len(new_ap)):
            xy = [new_ap[i].x,new_ap[i].y]
            if (xy not in xy_positions):
                xy_positions.append(xy)
                filtered_ap.append(new_ap[i])
                
        return(new_ap)


      
# draws a point / pixel        
def draw_p(x,y,color):
    if color != None:
        turtle.color(color)
    turtle.setpos(x+0.5,y+0.5)
    turtle.stamp()

def draw_p_uv(point):
    turtle.setpos(point.x+0.5,point.y+0.5)

    u = point.u
    v = point.v

    turtle.color(normalize_rgb(point.u,point.v,0,1))
    turtle.stamp()

def draw_p_texture(point,texture_data):
    turtle.setpos(point.x+0.5,point.y+0.5)

    raw_u = point.u
    raw_v = point.v

    u = int(round(texture_data.width * raw_u))
    v = int(round(texture_data.height * raw_v))

    turtle.color(texture_data.texture[v][u])

    turtle.stamp()
    
def normalize_rgb(r,g,b,m): #unnecasary 
    rt = (r - abs(r)) / 2
    gt = (g - abs(g)) / 2
    bt = (b - abs(b)) / 2

    t = -min(rt,gt,bt)

    try    : rss = m/(r+t)
    except : rss = 1
    try    : gss = m/(g+t)
    except : gss = 1
    try    : bss = m/(b+t)
    except : bss = 1
    
    rs = min( rss,1)
    gs = min( gss,1)
    bs = min( bss,1)

    s = min(rs,gs,bs)

    R = (r+t)*s
    G = (g+t)*s
    B = (b+t)*s

    return(R,G,B)


    
# class of mouse
class mouse:
    def __init__(s,x,y):
        s.x = x
        s.y = y

# sets the mouse coordinates
def mouse_position(event):
    m.x = +(event.x * (c_size/w_size)) 
    m.y = -(event.y * (c_size/w_size)) + c_size

# tells a point whether it should follow the mouse (if clicked)
def point_follow_mouse(points,mouse):
    m = mouse
    for i in range(len(points)):
        p = points[i]
        if p.clicked == True:
            p.rx = m.x
            p.ry = m.y
        else:
            pass

    def mouse_b1_click(x,y):
        m.b1 = [round(x,3),round(y)]

        # incase of multiple points occupying same space
        point_clicked = False
        for i in range(len(scene_points)):
            if point_clicked == True:
                scene_points[i].clicked = False
            if scene_points[i].clicked == True:
                point_clicked = True
 
                
        for i in range(len(points)):
            p = points[i]
            dx = abs(m.x-p.x)
            dy = abs(m.y-p.y)
            distance = math.sqrt(dx**2 + dy**2)

            if p.clicked == True:
                p.clicked = False
                
            else:
                if distance < 0.5:
                    p.clicked = True

    canvas.bind('<Motion>',mouse_position)
    turtle.Screen().onscreenclick(mouse_b1_click, btn=1, add=None)

# shows a "cursor"
def mouse_show():
    radius = 0.1
    turtle.fillcolor("green")
    turtle.goto(m.x,m.y-radius)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    radius = 0.5
    turtle.color("blacK")
    turtle.goto(m.x,m.y-radius)
    turtle.pd()
    turtle.circle(radius)
    turtle.pu()



def hex_to_dec(h,depth):
    max_value = 0
    for i in range(depth):
        max_value += 16**depth
        
    try:
        decimal = int(h)
    except:
        if   h == 'a': decimal = (10)
        elif h == 'b': decimal = (11)
        elif h == 'c': decimal = (12)
        elif h == 'd': decimal = (13)
        elif h == 'e': decimal = (14)
        elif h == 'f': decimal = (15)

    if depth != None:
        decimal = decimal/max_value
    return(decimal)

def load_texture(texture_name):
    # file = open(texture_name,"r").readlines()

    file = """1
fff000fff000fff000fff000fff000
000fff000fff000fff000fff000fff
fff000f00000fff000f00000fff000
000fff000f00000fff000f00000fff
fff000fff000fff000fff000fff000
000f00000fff000fff000fff00ffff
fff0fff00000fff000fff00fff0000
000fff0fff000f00f000fff0000fff
fff000fff0fff0ff0fff0000fff000
000fff000fff000fff000fff000fff"""

    raw_file = ["fff000fff000fff000fff000fff000",
                "000fff000fff000fff000fff000fff",
                "fff000f00000fff000f00000fff000",
                "000fff000f00000fff000f00000fff",
                "fff000fff000fff000fff000fff000",
                "000f00000fff000fff000fff00ffff",
                "fff0fff00000fff000fff00fff0000",
                "000fff0fff000f00f000fff0000fff",
                "fff000fff0fff0ff0fff0000fff000",
                "000fff000fff000fff000fff000fff"]
    depth = 1

    # for y in range(len(file)-1,-1,-1): # adds the raw lines to a list minus the "\n"
    #     if y == 0 :
    #         depth = int(file[y].strip())
    #     else:
    #         raw_file.append(file[y].strip())

    texture = []
    for y in range(len(raw_file)):
        line = []
        for i in range(int(len(raw_file[y])/(3*depth))):
            line.append([[],[],[]])

        for i in range(len(raw_file[y])):
            line[ (i//depth)//3 ][ (i//depth)%3 ].append(hex_to_dec(raw_file[y][i],depth))

        for i in range(len(line)):
            for j in range(len(line[i])):

                value = 0
                for k in range(len(line[i][j])):
                    value += line[i][j][k] * (16**(len(line[i][j]) - k - 1))

                line[i][j] = value
        texture.append(line)
    return(texture)

class texture_data():
    def __init__(s,file_name):
        s.file_name = file_name

        s.texture = load_texture(s.file_name)
        s.width = len(s.texture[0])-1
        s.height = len(s.texture)-1
                 


import turtle
import math

w_size = 1000 # pixel size of window
c_size = 20 # coordinate size in window
u_size = 21 # a random constant? 21 ish

turtle.setup(w_size ,w_size)
turtle.setworldcoordinates(0,0,c_size,c_size)

turtlesize = w_size  * 1/(c_size*u_size)
turtle.shapesize( turtlesize ) #sets the stamp size to be correct
turtle.shape("square")
turtle.hideturtle()

turtle.tracer(False)
turtle.speed(0)
turtle.pu()

a = point(00,00,0,0)
b = point(00,10,0,1)
c = point(10,10,1,1)

d = point(10,00,1,0)

scene_points = [a,b,c,d]

test_texture = texture_data("1_texture.txt")

test_poly = polygon([a,b,c,d],100)

canvas = turtle.getcanvas()
m = mouse(0,0)

running = True
while(running == True):
    #test_poly.ap


    turtle.shapesize(turtlesize*1)
    ap = test_poly.ap
    for i in range(len(ap)):
        draw_p_texture(ap[i],test_texture)
    """
    turtle.shapesize(turtlesize*1)
    bp = test_poly.bp
    for i in range(len(bp)):
        draw_p_texture(bp[i],test_texture)
    """
    """
    turtle.shapesize(turtlesize/2)
    fp = test_poly.fp
    for i in range(len(fp)):
        draw_p_uv(fp[i])
    """
    
    
    for i in range(len(test_poly.fp)):
        radius = 0.1
        turtle.goto(test_poly.fp[i].x,test_poly.fp[i].y-radius)
        turtle.fillcolor("pink")
        turtle.begin_fill()
        turtle.circle(radius*2)
        turtle.end_fill()
    

    mouse_show()
    point_follow_mouse(test_poly.fp,m)
 
    turtle.Screen().update()
    turtle.clear()

turtle.exitonclick()



"""
https://www.mathsisfun.com/algebra/line-equation-2points.html
https://gis.stackexchange.com/questions/164900/what-algorithm-allows-me-to-calculate-the-set-of-all-points-inside-a-polygon
https://en.wikipedia.org/wiki/Flood_fill
https://cs.stackexchange.com/questions/87902/efficient-way-to-get-integral-points-of-segment-from-two-points-in-grid
  #t.Screen().update()
"""





























  
