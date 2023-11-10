# https://prepinsta.com/python-program/for-rotation-of-elements-of-array-left-and-right/
# Declare and initialize an array and number of rotatioins
# Save first element of array in temp variable 
# Shift remaining array elements one by one towards left 
# Copy temp value to last element in array 
# Repeat step 2 to 4 until condition satisfies


N = int(input())

for i in range(N):
    
    # Enter input
    array_values = input()
    
    # Separate the array values by the whitespace
    array_list = array_values.split(" ")

    # Destructing or unpacking the list
    array = [int(num) for num in array_list]

    size = array[(0)]
    rotation = array[(-1)]

    # Removing the first and last element in the list 
    array = array[1:len(array)-1]

    for i in range(rotation):

        # Storing the first value in a temporary variable
        temp = array[0]

        for j in range(size - 1):

            # Shift all elements towards the left side by one
            array[j] = array[j+1]
        
        #Copying the temporary value to the last element in the array
        array[size - 1] = temp

    print(*array) # The asterisk operator * is used to unpack an iterable into the argument list of a given function. Basically it removes the square bracket and commas.







