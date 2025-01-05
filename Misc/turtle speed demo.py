# useful trigonometry functions
def sine(num):
    num = math.sin(math.radians(num))
    return(num)

def cosine(num):
    num = math.cos(math.radians(num))
    return(num)

def tan_min1(num1,num2):
    num = math.degrees(math.atan2(num1,num2))
    return(num)


import turtle
import random
import math

w_size = 1000 # window size
c_size = 100   # coordinate size within the window

turtle.setup(w_size ,w_size)
turtle.setworldcoordinates(-c_size,-c_size,c_size,c_size)
turtle.tracer(False)

def round(a,b = 1):
    if b == 1:return(int(math.floor(a) if (a - math.floor(a) < 0.5) else math.ceil(a)))
    else     :return(a//b + (1 if  a%b >= b/2 else 0)) * b

# sets up a new turtle with a given colour.
def turtle_setup(colour = "black"):
    temp_turtle = turtle.Turtle()

    temp_turtle.hideturtle()
    temp_turtle.speed(0)
    temp_turtle.pu()

    temp_turtle.color(colour)
    temp_turtle.shapesize(0.5)
    #temp_turtle.shape("square")
    temp_turtle.shape("circle")
    return(temp_turtle)

def test_1():
    # using just one turtle
    test_1_col = turtle_setup()
    
    for y in range(0,c_size,1):
        for x in range(0,c_size,1):

            # changing the colour on the same single turtle
            test_1_col.color(["red","green","blue"][random.randint(0,2)])

            test_1_col.goto(x,y)
            test_1_col.stamp()
     
        turtle.Screen().update()
        
    test_1_col.clear()
    
def test_2():
    # setting up 3 seperate turle for 3 diff colours
    test_2_red   = turtle_setup("red")
    test_2_green = turtle_setup("green")
    test_2_blue  = turtle_setup("blue")

    for y in range(0,c_size,1):
        for x in range(0,c_size,1):
            colour = ["red","green","blue"][random.randint(0,2)]

            # determining which turtle to use for the correct colour
            if colour == "red"  : demo_turtle = test_2_red
            if colour == "green": demo_turtle = test_2_green
            if colour == "blue" : demo_turtle = test_2_blue
            
            demo_turtle.goto(x,y)
            demo_turtle.stamp()
     
        turtle.Screen().update()

    # clearing each colour individually
    test_2_red.clear()
    test_2_green.clear()
    test_2_blue.clear()

def colour_divider(quality):
    colours = []
    step = 1/ (quality-1)
    for r in range(quality):
        for g in range(quality):
            for b in range(quality):
                R = r * step
                G = g * step
                B = b * step

                colours.append((R,G,B))
    return(colours)

def colour_aproximator(quality,r,g,b):
    step = 1/ (quality-1)
    R = round(r,step)
    G = round(g,step)
    B = round(b,step)

    aproximation = (R,G,B)

    index = (R / step) * (quality ** 2) + (G / step) * (quality ** 1) + (B / step) * (quality ** 0)

    return(index)

def test_3(quality):
    turtles = []
    turtles_used = []
    
    colours = colour_divider(quality)
    for i in range(len(colours)):
        turtles.append(turtle_setup(colours[i]))

    for y in range(0,c_size,1):
        for x in range(0,c_size,1):
            r = random.random()
            g = random.random()
            b = random.random()

            index = int(colour_aproximator(quality,r,g,b))
            turtles_used.append(index)

            turtles[index].goto(x,y)
            turtles[index].stamp()
            
     
        turtle.Screen().update()

    # clearing each colour individually
    turtles_used = list(dict.fromkeys(turtles_used))
    for index in turtles_used:
        turtles[index].clear()

def graph(quality):
    turtles = []
    turtles_used = []
    
    colours = colour_divider(quality)
    for i in range(len(colours)):
        turtles.append(turtle_setup(colours[i]))

    for y in range(-c_size,c_size,1):
        for x in range(-c_size,c_size,1):

            def F(x):
                s = 0.5
                return((math.sin(x * s) + 1)/2)
        
            r = F(x)
            g = F(y)
            b = F(0)

            index = int(colour_aproximator(quality,r,g,b))
            turtles_used.append(index)

            turtles[index].goto(x,y)
            turtles[index].stamp()
            
     
        turtle.Screen().update()

    # clearing each colour individually
    turtles_used = list(dict.fromkeys(turtles_used))
    for index in turtles_used:
        turtles[index].clear()
    
def splatter(quality):
    turtles = []
    turtles_used = []
    
    colours = colour_divider(quality)
    for i in range(len(colours)):
        turtles.append(turtle_setup(colours[i]))

    density = 5000
    for i in range(density):
        t = random.random() * 360
        d = i / density #random.random()

        def clamp(x,min_x,max_x):
            if x < min_x: return(min_x)
            if x > max_x: return(max_x)
            else: return(x)

        def Rand(blur):
            return((random.random() / blur) -0.5 / blur)

        Rand_grad = Rand(7)
        
        r = clamp(d + Rand_grad + Rand(2),0,1)
        g = clamp(d + Rand_grad + Rand(2),0,1)
        b = clamp(d + Rand_grad + Rand(2),0,1)


        x = cosine(t) * d * c_size
        y = sine(t) * d * c_size

        index = int(colour_aproximator(quality,r,g,b))
        turtles_used.append(index)

        turtles[index].goto(x,y)
        turtles[index].stamp()

        
    turtle.Screen().update()
    
    # clearing each colour individually
    turtles_used = list(dict.fromkeys(turtles_used))
    for index in turtles_used:
        pass
        #turtles[index].clear()

quality =  16#16 values for red, for blue and for green so 16^3 colours (4096)

test_3(quality)
test_2()
test_1()

splatter(quality)
graph(quality)


turtle.exitonclick()











