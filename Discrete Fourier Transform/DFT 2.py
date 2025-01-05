import math

pi = math.pi

s = [0.707,0,-0.707,-1,-0.707,0,0.707,1]


#def magnitude_print


N = len(s)


m = []
c = []

f_max = 30
for f in range(1,f_max+1):
    a = 0
    b = 0

    
    for n in range(N):
        a += s[n]*math.cos( (-2*pi*f*(n+1)) / N )
        b += s[n]*math.sin( (-2*pi*f*(n+1)) / N )
    
    M = ( 2*math.sqrt(a**2 + b**2) ) / N

    C = complex(a,b)
    c.append(C.real)
    
    m.append(round(M,3))

for i in range(len(m)):
    print(str(i<int(N/2)).ljust(5),
          str(i+1).ljust(3),
          ' = ',
          str(m[i]).ljust(5),
          end=' :')

    for n in range(int(m[i]*10)):
        print('■',end='')
        
    print()



    



#https://www.desmos.com/calculator/xeh5izd7oh
#https://www.desmos.com/calculator/osoexxrosl
