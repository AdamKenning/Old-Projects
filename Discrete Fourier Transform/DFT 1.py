import math
pi = 3.14159265359

# samples
s = [0.707,0,-0.707,-1,-0.707,0,0.707,1]

# amount of samples
N = len(s)

max_frequency = 30 #int(N/2)

m = []
for k in range(max_frequency):  
    a = 0
    b = 0
    
    for n in range(0,N,1): a += s[n]*math.cos( (-2*pi*(k+1)*n)/N )
        
    for n in range(0,N,1): b += s[n]*math.sin( (-2*pi*(k+1)*n)/N )

    M = (2*math.sqrt(a**2+b**2)) / N
    
    m.append(round(M,3))

#print(*m,sep='\n')

for i in range(len(m)):
    print(str(i<int(N/2)).ljust(5),
          str(i+1).ljust(3),
          ' = ',
          str(m[i]).ljust(5),
          end=' :')

    for n in range(int(m[i]*10)):
        print('■',end='')
        
    print()
    


    

    

    
