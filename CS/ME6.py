# Given an input orderable list:
# 1. Find the smallest element and swap it with first element in list
# 2. Find the second smallest element and swap it with second element in list
# 3. Continue until all elements in input list are in-order
# 4. Output ordered list

N = int(input())

for i in range(N):

    # Enter input
    array_values = input()
    
    # Separate the array values by the whitespace
    array_list = array_values.split(" ")

    # Remove the colon
    array_list.remove(":")

    # Destructing or unpacking the list
    array = [int(num) for num in array_list]


    for i in range(len(array)):

        for j in range(i+1, len(array)):
            
            # Checks if the element at the j-th position in the array is smaller (less than) the element at the i-th position. 
            # If condition is true, it means that we've found a smaller element later in the array than the current i-th element.
            if array[j] < array[i]:
                
                # Since the the element at the j-th position is smaller, we temporarily store the element  at the i-th position
                temp = array[i]

                # The element at the i-th position will now be replaced with the element at the j-th position (since it's smaller)
                array[i] = array[j]
                
                # The element at the j-th position will now be replaced with the temporary variable (the element that was in the i-th position)
                array[j] = temp
        
    
    print(*array)