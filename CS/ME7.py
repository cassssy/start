N = int(input())

for i in range(N):

    # Enter input
    char_values = input()

    # Removing the space by replacing it with no space
    # If you use the .remove function you will have an error if the input doesn't have a space
    char_values = char_values.replace(" ", "")

    # Destructing or unpacking the list as well as making it all lowercase for uniformity
    letters = [str.lower(x) for x in char_values]

    # The set function makes it so that it gets the dinstict letters and removes any duplicates
    m = set(letters)

    # Initializes tha max variable to zero 
    max = 0

    # Loop starts iterate through the unique characters in the m set
    # The variable i represents each unique character in the set
    for i in m:

        # Checks if the count of a specific letter is greater than the max
        if letters.count(i) > max:
            
            # If it is, the max will now become the count of that specific character
            max = letters.count(i)

            # We then assign a variable to hold the letter with the highest count
            most_occuring_char = i

    print (most_occuring_char)
