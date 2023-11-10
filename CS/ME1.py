

#Enter number of lines
N = int(input())

for i in range(N):
    
    #Enter input
    xy_values = input()
    #Separate the x and y values by the whitespace
    xy_list = xy_values.split(" ")

    #Destructing or unpacking the list
    p = [int(num) for num in xy_list]

    #Assigning the numbers in the list with the respective x and y values
    x1 = int(p[0])
    y1 = int(p[1])
    x2 = int(p[2])
    y2 = int(p[3])
    x3 = int(p[4])
    y3 = int(p[5])
    x4 = int(p[6])
    y4 = int(p[7])

    #Get the first line equation
    a1 = y2 - y1
    b1 = x1 - x2
    c1 = y1 * (x2 - x1) - (y2 - y1) * x1

    #Get the second line equation
    a2 = y4 - y3
    b2 = x3 - x4
    c2 = y3 * (x4 - x3) - (y4 - y3) * x3

    #Solve for the point of intersection using the two line equations
    x = int( ( (b1 * c2) - (b2 * c1) ) / ( (a1 * b2) - (a2 * b1) ) )
    y = int( ( (c1 * a2) - (c2 * a1) ) / ( (a1 * b2) - (a2 * b1) ) )
    
    print( x, y)
   




    
    
