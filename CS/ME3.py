    
def is_valid_date(dd, mm, yy):
    # Define the maximum number of days for each month
    max_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check for leap year and adjust February's maximum days
    if yy % 4 == 0 and (yy % 100 != 0 or yy % 400 == 0):
        max_days[2] = 29

    # Check if the month is valid (1-12)
    if mm < 1 or mm > 12:
        return False

    # Check if the day is within the valid range for the given month
    if dd < 1 or dd > max_days[mm]:
        return False

    return True



#Enter number of lines
N = int(input())

for i in range(N):
    
    #Enter input
    date_values = input()
    #Separate the date values by the whitespace
    date_list = date_values.split(" ")

    #Destructing or unpacking the list
    p = [int(num) for num in date_list]

    #Assigning the numbers in the list with the respective date values
    dd = int(p[0])
    mm = int(p[1])
    yy = int(p[2])

    #Import math module
    import math

    if is_valid_date(dd, mm, yy):
        if mm < 3:
            mm += 12
            yy -= 1    
        
        day_code = ((dd + (math.floor(13 * (mm + 1) / 5)) + yy + (math.floor(yy / 4)) - (math.floor(yy / 100)) + (math.floor(yy / 400)))%7)
        
        #Putting the days into a list
        days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]

        #Printing the the day name from the list depending on the result of the equation
        print (days[day_code])

    else:
        print ("invalid date")



