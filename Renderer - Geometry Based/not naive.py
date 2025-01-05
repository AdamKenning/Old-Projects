class triangle:
    def __init__(s,p1,p2,p3):
        s.p1 = p1
        s.p2 = p2
        s.p3 = p3
        
    @property
    def border_pixels(s):
        p1p2 = ints_on_line(s.p1,s.p2,resolution)
        p2p3 = ints_on_line(s.p2,s.p3,resolution)
        p3p1 = ints_on_line(s.p3,s.p1,resolution)
        pixels = p1p2 + p2p3 + p3p1
        return(pixels)

    @property
    def corner_pixels(s):
        pp1 = ints_on_line(s.p1,s.p2,resolution)[0]
        pp2 = ints_on_line(s.p2,s.p3,resolution)[0]
        pp3 = ints_on_line(s.p3,s.p1,resolution)[0]
        pixels = [pp1,pp2,pp3]
        return(pixels)

    @property
    def filler_pixels(s):
        pixels = fill_pixels(s)
        return(pixels)

def roundPartial(value, resolution):
    return round(value / resolution) * resolution

def ints_on_line(a,b,Resolution):
    resolution = Resolution
    d_x = b[0][0] - a[0][0] # delta xyz
    d_y = b[1][0] - a[1][0]
    d_z = b[2][0] - a[2][0]

    longest = math.ceil((max(abs(d_x),abs(d_y),abs(d_z))) * (resolution) ) 

    i_x = d_x/longest # incriments for xyz
    i_y = d_y/longest
    i_z = d_z/longest
    
    points = [[None]]
    
    for i in range(0,longest):
        p = [[roundPartial( (a[0][0] + i_x * i) , 1/resolution)],
             [roundPartial( (a[1][0] + i_y * i) , 1/resolution)],
             [roundPartial( (a[2][0] + i_z * i) , 1/resolution)],
             [1]]

        if p[0] != points[-1][0] or p[1] != points[-1][1]:
                points.append(p)
                
    del points[0]
        
    return(points)

def fill_pixels(triangle):
    
    fill = [[None]]
    
    corner = triangle.corner_pixels
    border = triangle.border_pixels
    
    min_x = +(float('inf'))
    max_x = -(float('inf'))

    min_y = +(float('inf'))
    max_y = -(float('inf'))

    for i in range(3):
        x = corner[i][0][0] * resolution
        y = corner[i][1][0] * resolution
        
        min_x = (x if x < min_x else min_x)
        max_x = (x if x > max_x else max_x)

        min_y = (y if y < min_y else min_y)
        max_y = (y if y > max_y else max_y)

    d_x = int(max_x - min_x)
    d_y = int(max_y - min_y)

    row = []
    grid = []
    for x in range(abs(d_x) + 1):
        row.append(None)
    for y in range(abs(d_y) + 1):
        grid.append(row[:])

    for i in range(len(border)):
        x = int(border[i][0][0] * resolution)
        y = int(border[i][1][0] * resolution)
        z = border[i][2][0]
        
        grid[y - int(min_y)][x - int(min_x)] = [x,y,z]

    for row in range(len(grid)-1,-1,-1):
        start_buffer = None
        start = None
        end = None
        for colomn in range(len(grid[row])):
            if grid[row][colomn] != None:
                try:
                    if grid[row][colomn+1] == None:
                        if start == None:
                            start_buffer = grid[row][colomn]
                            start = [[row,colomn],grid[row][colomn]]
                except: pass

            if start != None:
                if grid[row][colomn] != None and [row,colomn] != start[0]:
                    if grid[row][colomn-1] == None:
                        end = [[row,colomn],grid[row][colomn]]

        if end == None and start != None:
            grid[start[0][0]][start[0][1]] = start_buffer
            start = None
            start_buffer = None

        if start != None and end != None:
       
            dx = end[1][0] - start[1][0]
            dz = end[1][2] - start[1][2]
            #print("dx =",dx)

            for i in range(1,dx):
                x = (start[1][0] + i) / resolution
                y = (start[1][1])     / resolution
                z = roundPartial((start[1][2] + (dz/dx) * i),1/resolution)
                
                p = [[x],
                     [y],
                     [z],
                     [1]]
                
                if p[0] != fill[-1][0] or p[1] != fill[-1][1]:
                    fill.append(p)

    del fill[0]
    return(fill)
    
class t_pixel:
    def __init__(s,z):
        s.z = z
        s.color = None
        s.color_buffer = None
        s.triangle_color = None
        
        s.t = turtle.Turtle()
        s.t.pensize(0)

        s.t.speed(0)
        s.t._tracer(0)
        s.t.hideturtle()
        s.t.pu()

        
def draw_pixel(matrix,colour):
    x = matrix[0][0]
    y = matrix[1][0]
    z = matrix[2][0]
    try:
        t = pixel_grid[int(y*resolution)][int(x*resolution)]
        
        if z <= t.z:
            t.t.clear()
            t.t.fillcolor(colour)
            t.z = z
            t.color = colour
            t.triangle_color = colour

            t.t.goto(x               ,y)
            t.t.begin_fill()
            t.t.goto(x + 1/resolution,y)
            t.t.goto(x + 1/resolution,y + 1/resolution)
            t.t.goto(x               ,y + 1/resolution)
            t.t.goto(x               ,y)
            t.t.end_fill()
    except:
        pass


        
def draw_triangle(triangle,color):
    borders = triangle.border_pixels
    fillers = triangle.filler_pixels

    for i in range(len(fillers)):
        draw_pixel(fillers[i],color)

        percent = round((i/(len(fillers)))*100,2)
        if percent % 20 == 0:
            screen.update()

def anti_aliasing(pixel_grid):
    for y in range(len(pixel_grid)):
        for x in range(len(pixel_grid[0])):
            draw_pixel([[x/resolution],[y/resolution],[float('inf')]],background_color)
            
    screen.update()

    for y in range(len(pixel_grid)):
        for x in range(len(pixel_grid[0])):
            p = pixel_grid
            self = p[y][x].color
            
            try: up    = p[y+1][x].color
            except: up    = None
            
            try: down  = p[y-1][x].color
            except: down  = None
            
            try: left  = p[y][x-1].color
            except: left  = None
            
            try: right = p[y][x+1].color
            except: right = None

            neighbours = [up,down,left,right]
            ratio = 1

            rgb = color_weight(ratio,self,neighbours)

            d1 = abs(rgb[0]+rgb[1]+rgb[2] - (background_color[0]+background_color[1]+background_color[2]))
            d2 = abs(rgb[0]+rgb[1]+rgb[2] - (p[y][x].triangle_color[0]+p[y][x].triangle_color[1]+p[y][x].triangle_color[2]))
            
            pixel_grid[y][x].color_buffer = rgb
                
    for y in range(len(pixel_grid)):
        for x in range(len(pixel_grid)):
            p_m = [[x/resolution],[y/resolution],[p[y][x].z],[1]]
            color = pixel_grid[y][x].color_buffer
            draw_pixel(p_m,rgb)

        print(y," / ", len(pixel_grid))
            
    screen.update()
            
def color_weight(ratio,self,neighbours):
    
    n = []
    for i in range(len(neighbours)):    
        if neighbours[i] != None:
            n.append(neighbours[i])

    r = [self[0]]
    g = [self[1]]
    b = [self[2]] 

    for i in range(len(n)): ################## fix alll
        for j in range(ratio):
            r.append(n[i][0])
            g.append(n[i][1])
            b.append(n[i][2])

    rr = 0
    gg = 0
    bb = 0
    for i in range(len(r)):
        rr += r[i]
        gg += g[i]
        bb += b[i]
    
    RGB = [rr/ratio+1,gg/ratio+1,bb/ratio+1]

    return(RGB)
        
            
def pm(x,y,z):
    p = [[x],[y],[z],[1]]
    return(p)
    
import math
import turtle

background_color = (100, 100, 100)
resolution = 16
#1,2,4,5,8,10,16,20,32,40,64,80

size_width = 10
size_height = 10
turtle.setworldcoordinates(0,0,size_width,size_height)
screen = turtle.Screen()
screen.colormode(255)
screen.update()

#turtle.bgcolor(252, 190, 111)
turtle.bgcolor(background_color)

pixel_grid = []
for y in range(size_height * resolution):
    pixel_row = []
    for x in range(size_width * resolution):
        t = t_pixel(float('inf'))
        t.t.goto(x,y)
        pixel_row.append(t)
    pixel_grid.append(pixel_row)

    percent = round((y/(size_height*resolution))*100,2)
    if percent % 10 == 0:
        print(int(percent),"%")

#input()
print("start")
screen.update()

p1a = pm(1,7,0)
p1b = pm(7,5,0)
p1c = pm(3,0,0)
test1 = triangle(p1a,p1b,p1c)

p2a = pm(8,5,3)
p2b = pm(4,2,-8)
p2c = pm(0,2,-1)
test2 = triangle(p2a,p2b,p2c)
    
p3a = pm(0.5,8,2)
p3b = pm(5,4,-1)
p3c = pm(2,1,-3)
test3 = triangle(p3a,p3b,p3c)

p4a = pm(7,8,0)
p4b = pm(8,0,-4)
p4c = pm(4,1,3)
test4 = triangle(p4a,p4b,p4c)

p5a = pm(9,6,0)
p5b = pm(10,0,-4)
p5c = pm(5,1,0)
test5 = triangle(p5a,p5b,p5c)

p6a = pm(0,2,6)
p6b = pm(9,8,6)
p6c = pm(3,9,6)
test6 = triangle(p6a,p6b,p6c)


draw_triangle(test1,[240,125,125])
draw_triangle(test2,[125,240,125])
draw_triangle(test3,[125,125,240])

draw_triangle(test4,[125,240,240])
draw_triangle(test5,[240,125,240])
draw_triangle(test6,[240,240,125])

screen.update()

print("end")
#https://www.youtube.com/watch?v=t7Ztio8cwqM













