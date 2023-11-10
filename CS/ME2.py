# Output should show x, y if correct
# Output shouls be 'do not intersect' if they don't intersect
# Output should be 'invalid input' if two line segments were not formed and two lines intersect more than once (collinearity))
# Check if slopes are equal, check if the slopes are equal and they coincide with each other (collinear)


def do_not_intersect (line1, line2):
    
    # Defining lines
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    # Calculate differences in x and y coordinates
    dx1 = x2 - x1
    dx2 = x4 - x3
    dy1 = y2 - y1
    dy2 = y4 - y3

    # Calculate slopes of the segments
    m1 = dy1 / dx1 if dx1 != 0 else float('inf')
    m2 = dy2 / dx2 if dx2 != 0 else float('inf')

    # Check if the segments do not overlap on the x-axis
    if max(x1, x2) < min(x3, x4) or min(x1, x2) > max(x3, x4):
        return True

    # Check if the segments do not overlap on the y-axis
    if max(y1, y2) < min(y3, y4) or min(y1, y2) > max(y3, y4):
        return True
    
    # Check if the line segments are collinear (using area of triangle method)
    if m1 == m2:
        
        # If it's collinear, we return false so that it can indicate that the segments do interset
        if ( (1/2) * (x1 * (y2- y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)) ) == 0:
            return False

        return True
# With this, if the argument becomes true for this function, it will print "do not intersect" at the end 
# Meanwhile, it will just skip to the next thing if it's false
    


def invalid_input (line1, line2):
    
    # Defining lines
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    # Calculate differences in x and y coordinates
    dx1 = x2 - x1
    dx2 = x4 - x3
    dy1 = y2 - y1
    dy2 = y4 - y3

    # Calculate slopes of the segments
    m1 = dy1 / dx1 if dx1 != 0 else float('inf')
    m2 = dy2 / dx2 if dx2 != 0 else float('inf')

    # Checking if one of the input will form a point instead of a line
    if (x1 == x2 and y1 == y2) or (x3 == x4 and y3 == y4):
        return True
    
    if m1 != m2:
        return False

    # Check if the line segments are collinear (using area of triangle method)
    if m1 == m2:
    
        if ( (1/2) * (x1 * (y2- y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)) ) == 0:
            return True

        return False


######### Start of working code
    

# Enter number of lines
N = int(input())

for i in range(N):
    
    # Enter input
    xy_values = input()

    # Separate the x and y values by the whitespace
    xy_list = xy_values.split(" ")
    
    # Destructing or unpacking the list
    p = [int(num) for num in xy_list]
    
    # Assigning the numbers in the list with the respective x and y values
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, xy_list)
    
    # Defining lines
    line1 = x1, y1, x2, y2
    line2 = x3, y3, x4, y4

    # I placed the invalid input function first because if the condition is 1 line and 1 point, it can still mean that it does not intersect with each other
    # So we need to put the invalid input function first because if not it will print both the "do not intersect" and "invalid input"
    if invalid_input (line1, line2):
        print ("invalid input")
    
    # We use elif instead of if to make the if statement from above mutually exclusive so it won't print both the "do not intersect" and "invalid input"
    # With elif it means that it can only be either "input invalid" or "do not intersect" but not both (similar to XOR)
    elif do_not_intersect (line1, line2):
        print ("do not intersect")


    else: # Just a copy paste from ME1

        # Get the first line equation
        a1 = y2 - y1
        b1 = x1 - x2
        c1 = y1 * (x2 - x1) - (y2 - y1) * x1

        # Get the second line equation
        a2 = y4 - y3
        b2 = x3 - x4
        c2 = y3 * (x4 - x3) - (y4 - y3) * x3

        # Solve for the point of intersection using the two line equations
        x = int( ( (b1 * c2) - (b2 * c1) ) / ( (a1 * b2) - (a2 * b1) ) )
        y = int( ( (c1 * a2) - (c2 * a1) ) / ( (a1 * b2) - (a2 * b1) ) )
    
        print(x, y)



