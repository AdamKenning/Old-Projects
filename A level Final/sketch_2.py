def sign(num): return( 1 if(num > 0) else 0 if (num == 0) else -1 )
 
def cos(num): return(math.cos(num * math.pi * 2))
def sin(num): return(math.sin(num * math.pi * 2))
def tan(num): return(math.tan(num * math.pi * 2))

def round(a,b = 1):
    if b == 1:return(int(math.floor(a) if (a - math.floor(a) < 0.5) else math.ceil(a)))
    else     :return(a//b + (1 if  a%b >= b/2 else 0)) * b

def percent(x,start = 0,finish = 100): return( float(x - start) / (finish - start) )
def map(x,a_start,a_end,b_start,b_end): return((b_end - b_start) * percent(x,a_start,a_end) + b_start)
def between(x,a = 0,b = 1): return((x >= a) and (x <= b))
                        
def copy_list(a):
    copy_of_list = []
    for i in range(len(a)):copy_of_list.append(a[i])
    return(copy_of_list)

def hex_to_dec(hex_num):
    try:
        decimal = int(hex_num)
    except:
        if   hex_num == 'a': decimal = (10)
        elif hex_num == 'b': decimal = (11)
        elif hex_num == 'c': decimal = (12)
        elif hex_num == 'd': decimal = (13)
        elif hex_num == 'e': decimal = (14)
        elif hex_num == 'f': decimal = (15)
    return(decimal)

def load_file(txt_name,path): 
    name_full = lambda txt_name : path + "\\" + txt_name + ".txt"
    def read_file():
        texture_name_full = name_full(txt_name)
        read = createReader(texture_name_full)
        
        raw_file = [] 
        finished_reading = False
        while finished_reading == False:
            try: 
                line = read.readLine()
                if line == None: 5/0
                line = unicode(line)
                raw_file.append(line)
            except:
                finished_reading = True
        return(raw_file)
    
    raw_file = read_file()
    if raw_file == []:
        texture_name = "missing"
        raw_file = read_file()
    return(raw_file)

def load_texture(texture_name, depth = 1):
    path = "D:\\NEA computing\\PYTHON PROCESSING maybe\\sketch_2\\Textures"
    raw_file = load_file(texture_name,path)
    
    texture = []
    for y in range(len(raw_file)):
        row = []
        for i in range(int(len(raw_file[y])/(3*depth))):
            row.append([[],[],[]])
            
        for i in range(len(raw_file[y])):
            decimal = hex_to_dec(raw_file[y][i])
            h = map(decimal,0,15,0,1)
            h = round(h,0.1)
            row[ (i//depth)//3 ][ (i//depth)%3 ].append(h)

        for i in range(len(row)):
            for j in range(len(row[i])):

                value = 0
                for k in range(len(row[i][j])):
                    value += row[i][j][k] * (16**(len(row[i][j]) - k - 1))

                row[i][j] = value
        texture.append(row)
    return(texture)

class character_data():
    def load_letter_file(s):
        path = "D:\\NEA computing\\PYTHON PROCESSING maybe\\sketch_2\\Letters"
        raw_data = load_file("_" + s.name,path)
        
        data = []
        for l in raw_data:
            row = []
            for c in l:
                row.append(int(c))
            data.append(row)
        
        s.data = data
        
    def __init__(s,name):
        s.name = name
            
        s.data = None
        s.load_letter_file(s)
        
        s.size_width  = len(s.data[0])
        s.size_height = len(s.data)

class characters():
    def __init__(s):    
        s.symbols        = [' ']
        s.alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        s.all_characters = s.symbols + s.alphabet_upper
        
        s.all_characters_data = []
        for c in s.all_characters:
            s.all_characters_data.append(character_data(c))
    
    def get(s,character):
        try: character = character.upper()
        except:pass
        
        index = 0
        for i in range(len(s.all_characters)):
            if s.all_characters[i] == character:
                index = i
        return(s.all_characters_data[index])
    
class vector_3d():
    def __init__(s,x = 0,y = 0,z = 0):
        s.x = x
        s.y = y
        s.z = z
    
    def get(s): return(s.x,s.y,s.z)
    
    def set(s,x = None,y = None,z = None):
        if x != None: s.x = x
        if y != None: s.y = y
        if z != None: s.z = z

    def p(s):
        right_shift = 3
        print(" x = ",str(s.x).rjust(right_shift))
        print(" y = ",str(s.y).rjust(right_shift))
        print(" z = ",str(s.z).rjust(right_shift))
        print()

    def add(s, x = 0, y = 0, z = 0):
        s.x += x
        s.y += y
        s.z += z

    def multiply(s, x = 1, y = 1, z = 1):
        s.x *= x
        s.y *= y
        s.z *= y
    
    def round(s):
        return( vector_3d( round(s.x), round(s.y), round(s.z)) )
    
    def percent(s,v_start,v_end):
        if v_start.x != v_end.x: px = percent(s.x,v_start.x,v_end.x)
        if v_start.y != v_end.y: py = percent(s.y,v_start.x,v_end.y)
        if v_start.z != v_end.z: pz = percent(s.z,v_start.x,v_end.z)
    

    def rotate(s,Rx = 0, Ry = 0, Rz = 0, x = 0, y = 0, z = 0):
        s.add(-x,-y,-z)

        buffer_0_x, buffer_0_y, buffer_0_z = s.get()
        buffer_1_x, buffer_1_y, buffer_1_z = 0,0,0

        if Rx % 1 != 0:
            buffer_1_y = buffer_0_y * cos(Rx) + buffer_0_z * - sin(Rx)
            buffer_1_z = buffer_0_y * sin(Rx) + buffer_0_z *   cos(Rx)
            buffer_0_y, buffer_0_z = buffer_1_y,buffer_1_z
        if Ry % 1 != 0:
            buffer_1_z = buffer_0_z * cos(Ry) + buffer_0_x * - sin(Ry)
            buffer_1_x = buffer_0_x * cos(Ry) + buffer_0_z *   sin(Ry)
            buffer_0_z, buffer_0_x = buffer_1_z, buffer_1_x
        if Rz % 1 != 0:
            buffer_1_x = buffer_0_x + cos(Rz) + buffer_0_y * - sin(Rz)
            buffer_1_y = buffer_0_x + sin(Rz) + buffer_0_y *   cos(Rz)
            buffer_0_x, buffer_0_y = buffer_1_x, buffer_1_y

        s.set(buffer_0_x,buffer_0_y,buffer_0_z)
        s.add(x,y,z)


class vector_9d():
    def __init__(s,x = 0,y = 0,z = 0,r = 0,g = 0,b = 0,u = 0,v = 0,t = 0):
        s.xyz = vector_3d(x,y,z)
        s.rgb = vector_3d(r,g,b)
        s.uvt = vector_3d(u,v,t)
        
                
class polygon_3():
    def __init__(s,texture_name):
        s.texture_name = texture_name
        s.vertex_1 = vector_9d()
        s.vertex_2 = vector_9d()
        s.vertex_3 = vector_9d()
        
        s.previous_state = [None,None,None]
        s.previous_face_pixles = []
    
    def get(s): return([s.vertex_1,s.vertex_2,s.vertex_3])
    
    def set(s,new_vector_1,new_vector_2,new_vector_3):
        s.vertex_1 = new_vector_1
        s.vertex_2 = new_vector_2
        s.vertex_3 = new_vector_3
    
    def check_update(s):
        no_change = (s.previous_state[0] == s.vertex_1) and (s.previous_state[1] == s.vertex_2) and (s.previous_state[2] == s.vertex_3)
        s.previous_state = [s.vertex_1,s.vertex_2,s.vertex_3]
        return(no_change)
            
    @property
    def vertex_pixels(s):
        s.vertex_1.uvt.set(None,None,s.texture_name)
        s.vertex_2.uvt.set(None,None,s.texture_name)
        s.vertex_3.uvt.set(None,None,s.texture_name)
        return(s.vertex_1,s.vertex_2,s.vertex_3)
    
    @property 
    def edge_pixels(s):
        vp = s.vertex_pixels
        
        edge_pixels_list = []
        
        for i in range(len(vp)):
            vertex_a = vp[i - 1]
            vertex_b = vp[i]
            
            a = vector_3d(*vertex_a.xyz.round().get())
            b = vector_3d(*vertex_b.xyz.round().get())

            incline_x = sign(b.x - a.x)
            delta_x    =  abs(b.x - a.x)

            incline_y = sign(b.y - a.y)
            delta_y    =  abs(b.y - a.y)

            xay = delta_x > delta_y
            counter = max(delta_x,delta_y)
            incline_d = -2*abs(delta_x - delta_y)
            incline_s =  2*min(delta_x,delta_y)

            error = incline_d + counter
            x_buffer = a.x
            y_buffer = a.y

            intersects = []
            while counter >= 0:
                
                temp_point = vector_9d(x_buffer,y_buffer,0,0,0,0,0,0,vertex_a.uvt.z)
                
                intersects.append(temp_point)
                counter -= 1
                if error >= 0 or xay:
                    x_buffer += incline_x
                if error >= 0 or not(xay):
                    y_buffer += incline_y
                if error >= 0:
                    error += incline_d
                else:
                    error += incline_s

            for i in range(len(intersects)):
                temp_point = intersects[i]
                percent = float(i)/len(intersects)

                z = (percent * (b.z-a.z))+a.z
                temp_point.xyz.z = z
        
                temp_point.uvt.x = (percent * (vertex_b.uvt.x-vertex_a.uvt.x))+vertex_a.uvt.x
                temp_point.uvt.y = (percent * (vertex_b.uvt.y-vertex_a.uvt.y))+vertex_a.uvt.y
            
                temp_point.rgb.x = (percent * (vertex_b.rgb.x-vertex_a.rgb.x))+vertex_a.rgb.x
                temp_point.rgb.y = (percent * (vertex_b.rgb.y-vertex_a.rgb.y))+vertex_a.rgb.y
                temp_point.rgb.z = (percent * (vertex_b.rgb.z-vertex_a.rgb.z))+vertex_a.rgb.z 
  
            edge_pixels_list.extend(intersects)
        return(edge_pixels_list)
    
    @property
    def face_pixels(s):
        if (s.check_update()):
            return(s.previous_face_pixles)
        else: 
            edge_pixels = s.edge_pixels
            t = edge_pixels[0].uvt.z
            
            face_pixels_list = []
            face_pixels_list.extend(edge_pixels)
            
            max_x = - infinity
            min_x = + infinity
            max_y = - infinity
            min_y = + infinity
            
            for i in range(len(edge_pixels)):
                x = edge_pixels[i].xyz.x
                y = edge_pixels[i].xyz.y
                
                if x > max_x : max_x = x
                if x < min_x : min_x = x
                if y > max_y : max_y = y
                if y < min_y : min_y = y
            
            grid = []
            
            for y in range(max_y - min_y + 1):
                row = []
                for x in range(max_x - min_x + 1):
                    row.append(None)
                grid.append(row)
            
            unique_xy = []
            for i in range(len(edge_pixels)):
                x = edge_pixels[i].xyz.x - min_x
                y = edge_pixels[i].xyz.y - min_y
                
                if [x,y] not in unique_xy :
                    unique_xy.append([x,y])
                    grid[y][x] = edge_pixels[i]
            
            for y in range(len(grid)):
                start_index = None 
                end_index = None
                start_found = 0 
                end_found = 0
    
                for x in range(0,len(grid[y]),+1):
                    if (grid[y][x] != None) and (start_index == None):
                        start_index = x  
                        
                for x in range(len(grid[y])-1,-1,-1):
                    if (grid[y][x] != None) and (end_index == None):
                        end_index = x

                if end_index - start_index > 1:
                    for x in range(len(grid[y])):
                        if x > start_index and x < end_index:
                            
                            percent = float(x - start_index) / (end_index - start_index)
                            
                            new_x = ((grid[y][end_index].xyz.x - grid[y][start_index].xyz.x)*(percent)) + grid[y][start_index].xyz.x
                            new_y = y + min_y 

                            new_z = ((grid[y][end_index].xyz.z - grid[y][start_index].xyz.z)*(percent)) + grid[y][start_index].xyz.z  
                            
                            new_r = ((grid[y][end_index].rgb.x - grid[y][start_index].rgb.x)*(percent)) + grid[y][start_index].rgb.x 
                            new_g = ((grid[y][end_index].rgb.y - grid[y][start_index].rgb.y)*(percent)) + grid[y][start_index].rgb.y
                            new_b = ((grid[y][end_index].rgb.z - grid[y][start_index].rgb.z)*(percent)) + grid[y][start_index].rgb.z
                            u = ((grid[y][end_index].uvt.x - grid[y][start_index].uvt.x)*(percent)) + grid[y][start_index].uvt.x
                        
                            if grid[y][x] != None:
                                v = grid[y][x].uvt.y
                            else:
                                v = 0

                            p = vector_9d(new_x,new_y,new_z,new_r,new_g,new_b,u,v,t)
                                
                            grid[y][x] = p  
           
            for x in range(len(grid[0])):
                start_index = None
                end_index = None
                start_found = 0
                end_found = 0
    
                for y in range(0,len(grid),+1):
                    if (grid[y][x] != None) and (start_index == None):
                        start_index = y
    
                for y in range(len(grid)-1,-1,-1):
                    if (grid[y][x] != None) and (end_index == None):
                        end_index = y
    
                if end_index - start_index > 1:
                    for y in range(len(grid)):
                        if y > start_index and y < end_index :
                            percent = float(y - start_index)/(end_index - start_index)
    
                            new_x = None
                            new_y = ((grid[end_index][x].xyz.y - grid[start_index][x].xyz.y)*(percent)) + grid[start_index][x].xyz.y
    
                            new_z = ((grid[end_index][x].xyz.z - grid[start_index][x].xyz.z)*(percent)) + grid[start_index][x].xyz.z
                            new_v = ((grid[end_index][x].uvt.y - grid[start_index][x].uvt.y)*(percent)) + grid[start_index][x].uvt.y
    
                            grid[y][x].xyz.z = (grid[y][x].xyz.z + new_z)/2
                            grid[y][x].xyz.y = new_y
                            grid[y][x].uvt.y = new_v
    
                            face_pixels_list.append(grid[y][x])
    
            face_pixels_list_unique = []
            unique_xy = []
            for i in range(len(face_pixels_list)):
                xy = [face_pixels_list[i].xyz.x,face_pixels_list[i].xyz.y]
                if (xy not in unique_xy):
                    unique_xy.append(xy)
                    face_pixels_list_unique.append(face_pixels_list[i])
            
            s.previous_face_pixles = face_pixels_list_unique
            return(face_pixels_list_unique)

class polygon_4():
    @property
    def vertices_update(s):
        new_vertices = []
        for v in s.vertices_default:
            new_v = vector_9d()
            
            new_v.xyz.set(*v.xyz.get())
            new_v.uvt.set(*v.uvt.get())
            
            new_v.xyz.rotate(s.rotation_matrix.x,s.rotation_matrix.y,s.rotation_matrix.z,0,0,0)
            new_v.xyz.multiply(*s.scale_matrix.get())
            new_v.xyz.add(s.move_matrix.x,s.move_matrix.y,s.move_matrix.z)
            
            new_vertices.append(new_v)
        s.vertices = new_vertices
    
    @property
    def centre(s):
        x_sum,y_sum,z_sum = 0,0,0
        for v in vertices:
            x_sum += v.xyz.x
            y_sum += v.xyz.y
            z_sum += v.xyz.z
            
        return(float(x_sum)/4,float(y_sum)/4,float(z_sum)/4)
    
    def __init__(s,texture_name):
        s.texture_name = texture_name
        
        s.rotation_matrix = vector_3d()
        s.scale_matrix = vector_3d(1,1,1)
        s.move_matrix = vector_3d()
        
        s.vertices_default = [vector_9d(),vector_9d(),vector_9d(),vector_9d()]
        for i in range(4):
            u = i//2
            v =  i%2
    
            x = u*2 - 1
            y = v*2 - 1
            
            s.vertices_default[i].xyz.set(x,y)
            s.vertices_default[i].uvt.set(u,v)
            
        s.vertices = []
        s.vertices_update
            
        s.vertices_buffer = copy_list(s.vertices)
        
        s.face_1_buffer = polygon_3(s.texture_name)
        s.face_1_buffer.set(s.vertices[0],s.vertices[1],s.vertices[2])
        
        s.face_2_buffer = polygon_3(s.texture_name)
        s.face_2_buffer.set(s.vertices[1],s.vertices[2],s.vertices[3])
            
    @property
    def face_1(s):
        v1,v2,v3 = s.vertices[0],s.vertices[1],s.vertices[2]
        b1,b2,b3 = s.vertices_buffer[0],s.vertices_buffer[1],s.vertices_buffer[2]
        if( (v1,v2,v3) == (b1,b2,b3) ):
            return(s.face_1_buffer)
        else:
            b1,b2,b3 = v1,v2,v3
            s.face_1_buffer.set(v1,v2,v3)
            return(s.face_1_buffer)
        
    @property
    def face_2(s):
        v1,v2,v3 = s.vertices[1],s.vertices[2],s.vertices[3]
        b1,b2,b3 = s.vertices_buffer[1],s.vertices_buffer[2],s.vertices_buffer[3]

        if( (v1,v2,v3) == (b1,b2,b3) ):
            return(s.face_2_buffer)
        else:
            b1,b2,b3 = v1,v2,v3
            s.face_2_buffer.set(v1,v2,v3)
            return(s.face_2_buffer)
        
    def face_pixels(s):
        s.vertices_update

        face_1_pixels = s.face_1.face_pixels
        face_2_pixels = s.face_2.face_pixels

        unique_pixels = []
        unique_xy     = []
        for i in range(len(face_1_pixels)):
            xy = [face_1_pixels[i].xyz.x,face_1_pixels[i].xyz.y]
            if xy not in unique_xy:
                unique_pixels.append(face_1_pixels[i])
                unique_xy.append(xy)    
        
        for i in range(len(face_2_pixels)):
            xy = [face_2_pixels[i].xyz.x,face_2_pixels[i].xyz.y]
            if xy not in unique_xy:
                unique_pixels.append(face_2_pixels[i])
                unique_xy.append(xy) 
        return(unique_pixels)

class texture_data():
    def __init__(s,name):
        s.name = name
        s.data = None
        if s.data == None: s.data = load_texture(s.name)
    
    def get_rgb(s,u,v):        
        w,h = len(s.data),len(s.data[0])
        
        u2 = int(round(map(u,0,1,0,w-1)))
        v2 = int(round(map(v,0,1,0,h-1)))

        rgb = s.data[u2][v2]
        
        r = map(rgb[0],0,1,0,255)
        g = map(rgb[1],0,1,0,255)
        b = map(rgb[2],0,1,0,255)
        
        rgb = [r,g,b]
        
        return(rgb)
            
class screen_pixels():
    def screen_setup(s):    
        s.pixel_width  = s.size_width  / s.pixel_columns
        s.pixel_height = s.size_height / s.pixel_rows
    
        for y in range(s.pixel_rows):
            row = []
            for x in range(s.pixel_columns):
                row.append(s.background_colour + [None])
                    
            s.grid.append(row)
     
    def clear_screen(s):
        for y in range(len(s.grid)):
            for x in range(len(s.grid[y])):
                s.grid[y][x] = s.background_colour + [None]
                
    def __init__(s):
        s.background_colour = [42, 47, 51]
        s.background_texture = "colour_black"

        s.size_width  = 1000
        s.size_height = 1000

        s.pixel_columns  = 100
        s.pixel_rows = 100

        s.grid = []
        
        s.loaded_textures = []
        
        s.screen_setup()
            
    def fetch_texture(s,texture_name,u,v):
        def fetch_texture():
            loaded_textures = s.loaded_textures
            for i in range(len(loaded_textures)):
                if loaded_textures[i].name == texture_name:
                    return(loaded_textures[i])
            t = texture_data(texture_name)
            s.loaded_textures.append(t)
            return(t)
        return(fetch_texture().get_rgb(u,v))
        
    def set_pixel(s,pixel):    
        if (between(pixel.xyz.x,0,s.pixel_columns)) and (between(pixel.xyz.y,0,s.pixel_rows)):

            percent_x = percent(pixel.xyz.x,0,s.pixel_rows)
            percent_y = percent(pixel.xyz.y,0,s.pixel_columns)
            
            if between(percent_x) and between(percent_y):
                index_x = int(round(percent_x * s.pixel_columns))
                index_y = int(round(percent_y * s.pixel_rows))
                
                index_x = int(map(index_x,0,s.pixel_columns,0,s.pixel_columns-1))
                index_y = int(map(index_y,0,s.pixel_rows,0,s.pixel_rows-1))
                
                if (pixel.xyz.z < s.grid[index_y][index_x][2]) or (s.grid[index_y][index_x][2] == None):
                    texture_name = pixel.uvt.z
                    u,v = pixel.uvt.x,pixel.uvt.y   
                    rgb = s.fetch_texture(texture_name,u,v)
                    
                    s.grid[index_y][index_x] = rgb + [pixel.xyz.z]
                    
    def set_pixels_polygon(s,polygon):
        face_pixels = polygon.face_pixels()
        
        for i in range(len(face_pixels)):
            print("ps = " + str(int(float(i)*100/len(face_pixels))) + "%")
            s.set_pixel(face_pixels[i])
                                        
import math

pi = math.pi
infinity = float('inf')

screen = screen_pixels()
character = characters()

def setup():
    size(screen.size_width,screen.size_height)
    global render_canvas
    global letter_canvas
    global button_canvas
    render_canvas = createGraphics(screen.size_width,screen.size_height)
    letter_canvas = createGraphics(screen.size_width,screen.size_height)
    button_canvas = createGraphics(screen.size_width,screen.size_height)

def draw_data(canvas,x,y,data,pixel_size = 1, rgb = [255,255,255]):
    for Y in range(len(data)):
        for X in range(len(data[0])):
            if data[Y][X] == 1:
                pos_x = x + X * pixel_size
                pos_y = y + Y * pixel_size
                
                canvas.fill(*rgb)
            
                canvas.rect(pos_x,pos_y,pixel_size,pixel_size)      

def draw_screen(screen):
    screen_grid = screen.grid
    
    render_canvas.beginDraw()
    render_canvas.noStroke()
            
    for row in range(len(screen_grid)):
        for column in range(len(screen_grid[0])):
            z = screen_grid[row][column][3]
            if z != None:
                rgb = screen_grid[row][column][:3]
                
                render_canvas.fill(*rgb)
                
                y = int((float(row) / screen.pixel_rows) * screen.size_height)
                x = int((float(column) / screen.pixel_columns) * screen.size_width)
                
                y = screen.size_height - y 
                render_canvas.rect(x, y, screen.pixel_width, screen.pixel_height)
    
    render_canvas.endDraw()
    image(render_canvas,0,0)
    render_canvas.clear()

def draw_sentance(x,y,sentance,pixel_size = 1,rgb = [255,255,255]):
    letter_canvas.beginDraw()
    letter_canvas.noStroke()
    
    running_in   = 0
    for c in sentance:
        raw_data = character.get(c)
        w = raw_data.size_width
        h = raw_data.size_height
        
        d = raw_data.data
        
        running_in += (w+1)*pixel_size
        draw_data(letter_canvas,x + running_in,y,d,pixel_size,rgb)
    
    letter_canvas.endDraw()
    image(letter_canvas,0,0)
    letter_canvas.clear()

class button():  
    def run_function(s):
        if s.name != "None":
            path = "D:\\NEA computing\\PYTHON PROCESSING maybe\\sketch_2\\Functions"
            data = load_file(s.name.replace(' ','_'),path)
            for l in data:
                c = l.split(".")
                if c[0] == 'b':
                    if c[1] == 'a':
                        name = c[2]
                        x_pos = int(c[3])
                        y_pos = int(c[4])
                        text_size = int(c[5])
                        button_rgb = []
                        letter_rgb = []
                        for num_string in (c[6].replace('[','').replace(']','').split(",")): button_rgb.append(int(num_string))
                        for num_string in (c[7].replace('[','').replace(']','').split(",")): letter_rgb.append(int(num_string))
                                   
                        b = button(name,x_pos,y_pos,text_size,button_rgb,letter_rgb)
                        buttons.append(b)
                        
                    if c[1] == 'd':
                        for i in range(len(buttons)-1,-1,-1):
                            if buttons[i].name == c[2]:
                                buttons.remove(buttons[i])
                    if c[1] == 'e':
                        for i in range(len(buttons)-1,-1,-1):
                            if buttons[i].name == c[2]:
                                name = c[2]
                                x_pos = int(c[3])
                                y_pos = int(c[4])
                                text_size = int(c[5])
                                button_rgb = []

                                letter_rgb = []
                                for num_string in (c[6].replace('[','').replace(']','').split(",")): button_rgb.append(int(num_string))
                                for num_string in (c[7].replace('[','').replace(']','').split(",")): letter_rgb.append(int(num_string))
                                
                                buttons[i] = button(name,x_pos,y_pos,text_size,button_rgb,letter_rgb)

                if c[0] == 'p':
                    if c[1] == 'a':
                        p4 = polygon_4("missing")
                        polygons.append(p4)
                    if c[1] == 'd':
                        try: polygons.pop()
                        except: pass

                    if c[1] == 'e':
                        import random
                        all_textures = ["checkerboard","face","missing","test_rgb_1","test_rgb_2","test_rgb_3_","test_rgb_4","test_rgb_5"]
                        rn = random.randint(0,len(all_textures)-1)

                        print(rn,len(all_textures))
                        t = all_textures[rn]
                        print(t)
                        polygons[-1].texture_name = t
                        print(polygons[-1].texture_name)
                        pass
                
    def __init__(s,name,x,y,text_size, button_rgb = [200,200,200],letter_rgb = [255,255,255]):
        s.name = name
        
        s.button_rgb = button_rgb
        s.letter_rgb = letter_rgb
        
        s.pressed_dim = 0.50
        s.was_pressed = False
        
        s.x = x 
        s.y = y 
        
        s.text_size = text_size
            
    @property
    def size_width(s) : return( s.text_size * (len(s.name) * 8 + 1) )
    @property
    def size_height(s): return( s.text_size * (11) )
    
    @property
    def pressed(s):
        if (mouse.pressed == True) and (mouse.x > s.x and mouse.x < s.x + s.size_width) and (mouse.y > s.y and mouse.y < s.y + s.size_height):
            s.was_pressed = True
            return(True)
        else:
            if s.was_pressed == True:
                s.run_function()
                s.was_pressed = False
            return(False)
        
    
    def draw_button(s):
        button_canvas.beginDraw()
        button_canvas.noStroke()
        
        button_rgb = s.button_rgb

        if s.pressed:
            button_rgb = [s.button_rgb[0] * s.pressed_dim, s.button_rgb[1] * s.pressed_dim, s.button_rgb[2] * s.pressed_dim]
            
        button_canvas.fill(*button_rgb)
        button_canvas.rect(s.x,s.y,s.size_width,s.size_height) 
    
        button_canvas.endDraw()
        image(button_canvas,0,0)
        button_canvas.clear()
        
        x = s.x - 7 * s.text_size
        y = s.y + 1 * s.text_size
        
        draw_sentance(x,y,s.name,s.text_size,s.letter_rgb)
        
class mouse_data():
    def __init__(s):
        s.x = 0
        s.y = 0
        s.pressed = False
    
    def set(s,x,y,pressed):
        s.x = x
        s.y = y
        s.pressed = pressed
mouse = mouse_data()

button_menu = button("menu",20,20,5,[7, 72, 91],[187, 182, 165])
buttons = [button_menu]

polygons = []
        
def draw():
    background(*screen.background_colour) 

    mouse.set(mouseX,mouseY,mousePressed)
    for p in polygons:
        screen.set_pixels_polygon(p)
    draw_screen(screen)
    screen.clear_screen()
    for b in buttons:
        b.draw_button()
    


    
