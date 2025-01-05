def write(pos=None, txt='', align="left", font=("Arial", 8, "normal")):
    #Write txt at pos in canvas with specified font and color.
    if pos is None:
        pos=turtle.position()
    x, y = pos
    x = x * screen.xscale
    y = y * screen.yscale
    anchor = {"left":"sw", "center":"s", "right":"se" }
    item = screen.cv.create_text(x-1, -y, text = txt, anchor = anchor[align],
                                    fill = turtle.pencolor(), font = font)

def draw_game():
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      p = grid[y][x]
      if len(p.nums) > 0: # >1
          for i in range(len(p.nums)):
            try:
              n = p.nums[i]
              xx = (((n-1)%3     )/3)+1/10
              yy = ((int((n-1)/3))/3)+1/10

              write((x+xx,y+yy),n)
            except:pass
      """
      else:
          try:
              write((x+0.433333,y+0.433333),p.nums[-1])
          except:pass
     """

def roundPartial(value, resolution):
    return round(value / resolution) * resolution
  
def draw_grid():
    for y in range(0,9):
        if y%3 == 0:
            t.pensize(3)
            t.color("red")
        else:
            t.pensize(1)
            t.color("black")
        t.goto(0,y)
        t.pd()
        t.goto(9,y)
        t.pu()
    for x in range(1,9):
        if x%3 == 0:
            t.pensize(3)
            t.color("red")
        else:
            t.pensize(1)
            t.color("black")
        t.goto(x,0)
        t.pd()
        t.goto(x,9)
        t.pu()
        
    t.color("black")

class point:
  def __init__(s,x,y,tag,visited):
    s.x = x
    s.y = y

    s.tag = tag
    s.visited = visited

    s.nums = [1,2,3,4,5,6,7,8,9]
    
class mouse_pos:
  def __init__(s,x,y):
    s.x = x
    s.y = y

def click(x,y): 
  mouse.x = roundPartial(x - 1/10,1/3) 
  mouse.y = roundPartial(y - 1/10,1/3)
  
  t.pu()
  t.goto(mouse.x + 1/10 ,mouse.y + 1/10-0.05)
  t.pd()
  t.circle(0.1)
  t.pu()

  square_x = math.floor(mouse.x)
  square_y = math.floor(mouse.y)
  
  num_x = round((mouse.x - square_x)/0.33)
  num_y = round((mouse.y - square_y)/0.33)

  number = (round((mouse.x - square_x)/0.33)) + (round((mouse.y - square_y)/0.33))*3
  number = int(number +1)

  initial = grid[square_y][square_x]

  if len(initial.nums) != 1:
      temp_list = []
      for i in range(len(initial.nums)):
          if initial.nums[i] == number:
              temp_list.append(initial.nums[i])
      initial.nums = temp_list

  to_update = [initial]
  while len(to_update) != 0:
      for i in range(len(to_update)):
          self = to_update[i]
          self.visited = True
          print(self)


          # gets their neighbours
          for yy in range(len(grid)):
              for xx in range(len(grid[yy])):
                  g = grid[yy][xx]
                  
                  if g.x == self.x or g.y == self.y or g.tag == self.tag:
                      if g.x != self.x or g.y != self.y:
                          
                          if len(self.nums) == 1 and len(g.nums) != 1:
                              try:
                                  g.nums.remove(self.nums[0])
                              except:pass
                          else:
                              pass
                              

                  
                  """
                  if (g.x == self.x or g.y == self.y) or (g.tag == self.tag):
                      if (g.x != self.x and g.y != self.y):
                  """
      to_update = []


    
    
grid = []
for y in range(0,9):
  row =[]
  for x in range(0,9):

    tag = (int((roundPartial(x-1, 3)/3) + (roundPartial(y-1, 3))))
    
    p = point(x,y,tag,False)

    row.append(p)
  grid.append(row)
  
import math
import turtle

screen = turtle.Screen()
turtle.setworldcoordinates(0,0,9,9)

t = turtle.Turtle()

t.hideturtle()
t.speed(0)
t._tracer(0)
t.pu()

global mouse
mouse = mouse_pos(x,y)

running = True
while running == True:

  screen.onclick(click,1)
  draw_grid()
  draw_game()
  
  screen.update()
  screen._delete("all")

    
