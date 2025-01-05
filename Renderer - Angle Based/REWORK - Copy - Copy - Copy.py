# imports
import math
import turtle
from turtle import *
from turtle import Screen

# controls
# wsad refer to up down left right & tg refer to forwards & backwards

# setting the turtle screen size
screen = turtle.Screen()
screen.screensize(500, 500)
turtle.setworldcoordinates(-10, -10, 10, 10)

# setting some turtle settings
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0)

# getting starting positions
correct_ans = False
while correct_ans == False:
  question_starting=input("initial coords of quadrilateral\n preset = 1\n custom = 2 \n")
  if question_starting == "1":
    correct_ans = True
    v = [0,0,15]

    a = [-1,5,0]
    b = [4,5,0]
    c = [-1,0,0]
    d = [4,0,0]
    
    new_v    = [0,0,0]
    new_abcd = [0,0,0]

    movement_amount = 1
    rotation_amount = 15
    
  elif question_starting == "2":
    correct_ans = True
    v = []

    a = []
    b = []
    c = []
    d = []

    new_v    = []
    new_abcd = []

    movement_amount = 1
    rotation_amount = 15
    ############################# add rotaino question
    for i in range (3):      
      v.append(int(input("enter coord of v (eg: 10)\n")))
    print("v coords =",v)
    for i in range (3):
      a.append(int(input("enter coord of a (eg: 10)\n")))
    print("a coords =",a)
    for i in range (3):
      b.append(int(input("enter coord of b (eg: 10)\n")))
    print("b coords =",b)
    for i in range (3):
      c.append(int(input("enter coord of c (eg: 10)\n")))
    print("c coords =",c)
    for i in range (3):
      d.append(int(input("enter coord of d (eg: 10)\n")))#
    print("d coords =",d)
    for i in range (3):
      new_v.append(int(input("enter coord of intitial v disposition (eg: 10)\n")))
    print("v disposition =",new_v)
    for i in range (3):
      new_abcd.append(int(input("enter coord of intitial polygon abcd disposition (eg: 10)\n")))
    print("abcd disposition =",new_abcd)
    movement=int(input("enter movement incriment (eg:  1)\n"))

    print("\nv coords =",v,"\na coords =",a,"\nb coords =",b,"\nc coords =",c,"\nd coords =",d,"\nv disposition =",new_v,"\nabcd disposition =",new_abcd,"movement incriment =",movement)
    
for i in range(100):
  # end positions (empty, because unknown)
  e = []
  f = []
  g = []
  h = []

  # making abcd1
  a1 = a.copy()
  b1 = b.copy()
  c1 = c.copy()
  d1 = d.copy()

  # moving abcd1 & v
  for i in range (3):
    a1[i-1] = a1[i-1] + new_abcd[i-1]
    b1[i-1] = b1[i-1] + new_abcd[i-1]
    c1[i-1] = c1[i-1] + new_abcd[i-1]
    d1[i-1] = d1[i-1] + new_abcd[i-1]
    
    v[i-1] = v[i-1] + new_v[i-1]
  # math for a
  a_line_v_a2 = v[2] - a1[2]
  a_line_v_a1 = math.sqrt((math.sqrt(a_line_v_a2**2 + a1[0]**2))**2 +a1[1]**2)
  a_line_a1_a2 = math.sqrt((a1[0]-v[0])**2 + (a1[1]-v[1])**2)
  a_angl_a1_a2_v = 90
  a_angl_v_a1_a2 = math.degrees(math.asin((math.sin(math.radians(a_angl_a1_a2_v))*a_line_v_a2)/a_line_v_a1))
  a_angl_a1_v_a2 = 180 - a_angl_v_a1_a2 - a_angl_a1_a2_v
  a_angl_v_e_q = 180 - a_angl_a1_v_a2 - a_angl_a1_a2_v
  a_line_e_q = (math.sin(math.radians(a_angl_a1_v_a2))*v[2])/math.sin(math.radians(a_angl_v_e_q))

  a_line_v_e = (math.sin(math.radians(90))*v[2])/math.sin(math.radians(a_angl_v_e_q))
  a_line_a1_e = a_line_v_e - a_line_v_a1
  a_disposition = (a_line_v_a1/a_line_v_a1)+(a_line_a1_e/a_line_v_a1)
  a_diff_a1_v = []
  for i in range (3):
    a_diff_a1_v.append(a1[i] - v[i])
  for i in range (3):
    e.append(v[i] + (a_diff_a1_v[i]*a_disposition))

  # math for b
  b_line_v_b2 = v[2] - b1[2]
  b_line_v_b1 = math.sqrt((math.sqrt(b_line_v_b2**2 + b1[0]**2))**2 +b1[1]**2)
  b_line_b1_b2 = math.sqrt((b1[0]-v[0])**2 + (b1[1]-v[1])**2)
  b_angl_b1_b2_v = 90
  b_angl_v_b1_b2 = math.degrees(math.asin((math.sin(math.radians(b_angl_b1_b2_v))*b_line_v_b2)/b_line_v_b1))
  b_angl_b1_v_b2 = 180 - b_angl_v_b1_b2 - b_angl_b1_b2_v
  b_angl_v_f_q = 180 - b_angl_b1_v_b2 - b_angl_b1_b2_v
  b_line_f_q = (math.sin(math.radians(b_angl_b1_v_b2))*v[2])/math.sin(math.radians(b_angl_v_f_q))

  b_line_v_f = (math.sin(math.radians(90))*v[2])/math.sin(math.radians(b_angl_v_f_q))
  b_line_b1_f = b_line_v_f - b_line_v_b1
  b_disposition = (b_line_v_b1/b_line_v_b1)+(b_line_b1_f/b_line_v_b1)
  b_diff_b1_v = []
  for i in range (3):
    b_diff_b1_v.append(b1[i] - v[i])
  for i in range (3):
    f.append(v[i] + (b_diff_b1_v[i]*b_disposition))

  # math for c
  c_line_v_c2 = v[2] - c1[2]
  c_line_v_c1 = math.sqrt((math.sqrt(c_line_v_c2**2 + c1[0]**2))**2 +c1[1]**2)
  c_line_c1_c2 = math.sqrt((c1[0]-v[0])**2 + (c1[1]-v[1])**2)
  c_angl_c1_c2_v = 90
  c_angl_v_c1_c2 = math.degrees(math.asin((math.sin(math.radians(c_angl_c1_c2_v))*c_line_v_c2)/c_line_v_c1))
  c_angl_c1_v_c2 = 180 - c_angl_v_c1_c2 - c_angl_c1_c2_v
  c_angl_v_g_q = 180 - c_angl_c1_v_c2 - c_angl_c1_c2_v
  c_line_g_q = (math.sin(math.radians(c_angl_c1_v_c2))*v[2])/math.sin(math.radians(c_angl_v_g_q))

  c_line_v_g = (math.sin(math.radians(90))*v[2])/math.sin(math.radians(c_angl_v_g_q))
  c_line_c1_g = c_line_v_g - c_line_v_c1
  c_disposition = (c_line_v_c1/c_line_v_c1)+(c_line_c1_g/c_line_v_c1)
  c_diff_c1_v = []
  for i in range (3):
    c_diff_c1_v.append(c1[i] - v[i])
  for i in range (3):
    g.append(v[i] + (c_diff_c1_v[i]*c_disposition))

  # math for d
  d_line_v_d2 = v[2] - d1[2]
  d_line_v_d1 = math.sqrt((math.sqrt(d_line_v_d2**2 + d1[0]**2))**2 +d1[1]**2)
  d_line_d1_d2 = math.sqrt((d1[0]-v[0])**2 + (d1[1]-v[1])**2)
  d_angl_d1_d2_v = 90
  d_angl_v_d1_d2 = math.degrees(math.asin((math.sin(math.radians(d_angl_d1_d2_v))*d_line_v_d2)/d_line_v_d1))
  d_angl_d1_v_d2 = 180 - d_angl_v_d1_d2 - d_angl_d1_d2_v
  d_angl_v_h_q = 180 - d_angl_d1_v_d2 - d_angl_d1_d2_v
  d_line_h_q = (math.sin(math.radians(d_angl_d1_v_d2))*v[2])/math.sin(math.radians(d_angl_v_h_q))

  d_line_v_h = (math.sin(math.radians(90))*v[2])/math.sin(math.radians(d_angl_v_h_q))
  d_line_d1_h = d_line_v_h - d_line_v_d1
  d_disposition = (d_line_v_d1/d_line_v_d1)+(d_line_d1_h/d_line_v_d1)
  d_diff_d1_v = []
  for i in range (3):
    d_diff_d1_v.append(d1[i] - v[i])
  for i in range (3):
    h.append(v[i] + (d_diff_d1_v[i]*d_disposition))

  # center point of abcd
  abcd_center = []
  for i in range (3):
    abcd_center.append((a[i] + b[i] + c[i] + d[i])/4)
    
  # drawing  
  turtle.clear()
  
  #pencolor((0, 0, 0))
  #turtle.penup()
  #turtle.goto(-10,0)
  #turtle.pendown()
  #turtle.goto(10,0)
  #turtle.penup()
  #turtle.goto(0,-10)
  #turtle.pendown()
  #turtle.goto(0,10)

  turtle.penup()
  turtle.goto(e[0],e[1])
  turtle.pendown()
      
  turtle.goto(f[0],f[1])
  pencolor(1, 0, 0)
  
  turtle.goto(h[0],h[1])
  pencolor(0, 1, 0)
  
  turtle.goto(g[0],g[1])
  pencolor(0, 0, 1)
  
  turtle.goto(e[0],e[1])
  pencolor(0, 0, 0)
  
  screen.update()
  
  # resetting the new_abcd & new_v
  #new_v = [0,0,0]
  #new_abcd = [0,0,0]

  # getting quadrilateral disposition
  correct_ans = False
  while correct_ans == False:
    question_movement = input("1 = move self\n2 = move quadrilateral \n3 = rotate quadrilateral\n")
    
    if question_movement == "1":
      correct_ans = True
      question_movement_self = input("choose movement (wsad tg) \n")        
      if question_movement_self == "w":        
        new_v[1] = new_v[1] + movement_amount
      elif question_movement_self == "s":
        new_v[1] = new_v[1] - movement_amount
      elif question_movement_self == "a":
        new_v[0] = new_v[0] - movement_amount
      elif question_movement_self == "d":
        new_v[0] = new_v[0] + movement_amount
      elif question_movement_self == "t":
        new_v[2] = new_v[2] - movement_amount
      elif question_movement_self == "g":
        new_v[2] = new_v[2] + movement_amount
        
    elif question_movement == "2":
      correct_ans = True
      question_movement_quad = input("choose movement (wsad tg) \n")
      if question_movement_quad == "w":
        new_abcd[1] = new_abcd[1] + movement_amount
      elif question_movement_quad == "s":
        new_abcd[1] = new_abcd[1] - movement_amount
      elif question_movement_quad == "a":
        new_abcd[0] = new_abcd[0] - movement_amount
      elif question_movement_quad == "d":
        new_abcd[0] = new_abcd[0] + movement_amount
      elif question_movement_quad == "t":
        new_abcd[2] = new_abcd[2] - movement_amount
      elif question_movement_quad == "g":
        new_abcd[2] = new_abcd[2] + movement_amount
        
    elif question_movement== "3":
      correct_ans = True
      question_rotation_quad = input("choose rotation (wsad tg) \n")

      if question_rotation_quad == "w":
        a[1]=((a[1]-abcd_center[1])*(math.cos(math.radians(-rotation_amount)))) - ((a[2]-abcd_center[2])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[1]
        a[2]=((a[2]-abcd_center[2])*(math.cos(math.radians(-rotation_amount)))) + ((a[1]-abcd_center[1])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[2]

        b[1]=((b[1]-abcd_center[1])*(math.cos(math.radians(-rotation_amount)))) - ((b[2]-abcd_center[2])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[1]
        b[2]=((b[2]-abcd_center[2])*(math.cos(math.radians(-rotation_amount)))) + ((b[1]-abcd_center[1])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[2]

        c[1]=((c[1]-abcd_center[1])*(math.cos(math.radians(-rotation_amount)))) - ((c[2]-abcd_center[2])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[1]
        c[2]=((c[2]-abcd_center[2])*(math.cos(math.radians(-rotation_amount)))) + ((c[1]-abcd_center[1])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[2]

        d[1]=((d[1]-abcd_center[1])*(math.cos(math.radians(-rotation_amount)))) - ((d[2]-abcd_center[2])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[1]
        d[2]=((d[2]-abcd_center[2])*(math.cos(math.radians(-rotation_amount)))) + ((d[1]-abcd_center[1])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[2]

      elif question_rotation_quad == "s":
        a[1]=((a[1]-abcd_center[1])*(math.cos(math.radians(rotation_amount)))) - ((a[2]-abcd_center[2])*(math.sin(math.radians(rotation_amount)))) + abcd_center[1]
        a[2]=((a[2]-abcd_center[2])*(math.cos(math.radians(rotation_amount)))) + ((a[1]-abcd_center[1])*(math.sin(math.radians(rotation_amount)))) + abcd_center[2]

        b[1]=((b[1]-abcd_center[1])*(math.cos(math.radians(rotation_amount)))) - ((b[2]-abcd_center[2])*(math.sin(math.radians(rotation_amount)))) + abcd_center[1]
        b[2]=((b[2]-abcd_center[2])*(math.cos(math.radians(rotation_amount)))) + ((b[1]-abcd_center[1])*(math.sin(math.radians(rotation_amount)))) + abcd_center[2]

        c[1]=((c[1]-abcd_center[1])*(math.cos(math.radians(rotation_amount)))) - ((c[2]-abcd_center[2])*(math.sin(math.radians(rotation_amount)))) + abcd_center[1]
        c[2]=((c[2]-abcd_center[2])*(math.cos(math.radians(rotation_amount)))) + ((c[1]-abcd_center[1])*(math.sin(math.radians(rotation_amount)))) + abcd_center[2]

        d[1]=((d[1]-abcd_center[1])*(math.cos(math.radians(rotation_amount)))) - ((d[2]-abcd_center[2])*(math.sin(math.radians(rotation_amount)))) + abcd_center[1]
        d[2]=((d[2]-abcd_center[2])*(math.cos(math.radians(rotation_amount)))) + ((d[1]-abcd_center[1])*(math.sin(math.radians(rotation_amount)))) + abcd_center[2]

      elif question_rotation_quad == "a":
        a[0]=((a[0]-abcd_center[0])*(math.cos(math.radians(-rotation_amount)))) - ((a[2]-abcd_center[2])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[0]
        a[2]=((a[2]-abcd_center[2])*(math.cos(math.radians(-rotation_amount)))) + ((a[0]-abcd_center[0])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[2]

        b[0]=((b[0]-abcd_center[0])*(math.cos(math.radians(-rotation_amount)))) - ((b[2]-abcd_center[2])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[0]
        b[2]=((b[2]-abcd_center[2])*(math.cos(math.radians(-rotation_amount)))) + ((b[0]-abcd_center[0])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[2]

        c[0]=((c[0]-abcd_center[0])*(math.cos(math.radians(-rotation_amount)))) - ((c[2]-abcd_center[2])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[0]
        c[2]=((c[2]-abcd_center[2])*(math.cos(math.radians(-rotation_amount)))) + ((c[0]-abcd_center[0])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[2]

        d[0]=((d[0]-abcd_center[0])*(math.cos(math.radians(-rotation_amount)))) - ((d[2]-abcd_center[2])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[0]
        d[2]=((d[2]-abcd_center[2])*(math.cos(math.radians(-rotation_amount)))) + ((d[0]-abcd_center[0])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[2]
        
      elif question_rotation_quad == "d":
        a[0]=((a[0]-abcd_center[0])*(math.cos(math.radians(rotation_amount)))) - ((a[2]-abcd_center[2])*(math.sin(math.radians(rotation_amount)))) + abcd_center[0]
        a[2]=((a[2]-abcd_center[2])*(math.cos(math.radians(rotation_amount)))) + ((a[0]-abcd_center[0])*(math.sin(math.radians(rotation_amount)))) + abcd_center[2]

        b[0]=((b[0]-abcd_center[0])*(math.cos(math.radians(rotation_amount)))) - ((b[2]-abcd_center[2])*(math.sin(math.radians(rotation_amount)))) + abcd_center[0]
        b[2]=((b[2]-abcd_center[2])*(math.cos(math.radians(rotation_amount)))) + ((b[0]-abcd_center[0])*(math.sin(math.radians(rotation_amount)))) + abcd_center[2]

        c[0]=((c[0]-abcd_center[0])*(math.cos(math.radians(rotation_amount)))) - ((c[2]-abcd_center[2])*(math.sin(math.radians(rotation_amount)))) + abcd_center[0]
        c[2]=((c[2]-abcd_center[2])*(math.cos(math.radians(rotation_amount)))) + ((c[0]-abcd_center[0])*(math.sin(math.radians(rotation_amount)))) + abcd_center[2]

        d[0]=((d[0]-abcd_center[0])*(math.cos(math.radians(rotation_amount)))) - ((d[2]-abcd_center[2])*(math.sin(math.radians(rotation_amount)))) + abcd_center[0]
        d[2]=((d[2]-abcd_center[2])*(math.cos(math.radians(rotation_amount)))) + ((d[0]-abcd_center[0])*(math.sin(math.radians(rotation_amount)))) + abcd_center[2]

      elif question_rotation_quad == "t":
        a[0]=((a[0]-abcd_center[0])*(math.cos(math.radians(rotation_amount)))) - ((a[1]-abcd_center[1])*(math.sin(math.radians(rotation_amount)))) + abcd_center[0]
        a[1]=((a[1]-abcd_center[1])*(math.cos(math.radians(rotation_amount)))) + ((a[0]-abcd_center[0])*(math.sin(math.radians(rotation_amount)))) + abcd_center[1]

        b[0]=((b[0]-abcd_center[0])*(math.cos(math.radians(rotation_amount)))) - ((b[1]-abcd_center[1])*(math.sin(math.radians(rotation_amount)))) + abcd_center[0]
        b[1]=((b[1]-abcd_center[1])*(math.cos(math.radians(rotation_amount)))) + ((b[0]-abcd_center[0])*(math.sin(math.radians(rotation_amount)))) + abcd_center[1]

        c[0]=((c[0]-abcd_center[0])*(math.cos(math.radians(rotation_amount)))) - ((c[1]-abcd_center[1])*(math.sin(math.radians(rotation_amount)))) + abcd_center[0]
        c[1]=((c[1]-abcd_center[1])*(math.cos(math.radians(rotation_amount)))) + ((c[0]-abcd_center[0])*(math.sin(math.radians(rotation_amount)))) + abcd_center[1]

        d[0]=((d[0]-abcd_center[0])*(math.cos(math.radians(rotation_amount)))) - ((d[1]-abcd_center[1])*(math.sin(math.radians(rotation_amount)))) + abcd_center[0]
        d[1]=((d[1]-abcd_center[1])*(math.cos(math.radians(rotation_amount)))) + ((d[0]-abcd_center[0])*(math.sin(math.radians(rotation_amount)))) + abcd_center[1]

      elif question_rotation_quad == "g":
        a[0]=((a[0]-abcd_center[0])*(math.cos(math.radians(-rotation_amount)))) - ((a[1]-abcd_center[1])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[0]
        a[1]=((a[1]-abcd_center[1])*(math.cos(math.radians(-rotation_amount)))) + ((a[0]-abcd_center[0])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[1]

        b[0]=((b[0]-abcd_center[0])*(math.cos(math.radians(-rotation_amount)))) - ((b[1]-abcd_center[1])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[0]
        b[1]=((b[1]-abcd_center[1])*(math.cos(math.radians(-rotation_amount)))) + ((b[0]-abcd_center[0])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[1]

        c[0]=((c[0]-abcd_center[0])*(math.cos(math.radians(-rotation_amount)))) - ((c[1]-abcd_center[1])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[0]
        c[1]=((c[1]-abcd_center[1])*(math.cos(math.radians(-rotation_amount)))) + ((c[0]-abcd_center[0])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[1]

        d[0]=((d[0]-abcd_center[0])*(math.cos(math.radians(-rotation_amount)))) - ((d[1]-abcd_center[1])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[0]
        d[1]=((d[1]-abcd_center[1])*(math.cos(math.radians(-rotation_amount)))) + ((d[0]-abcd_center[0])*(math.sin(math.radians(-rotation_amount)))) + abcd_center[1]



  # print("\nE =",e,"\nF =",f,"\nG =",g,"\nH =",h,"\n")






























