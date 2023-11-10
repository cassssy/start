# Function to find the prime factorization of a number
def prime_factor(given_num):
    # Making a list for the factors (it's empty but we can add numbers to the list by using the append function)
    factors = []
    # The count will be how many times a certain factor is repeated
    count = 0

    # Checking if the number is 1, which will just return 1
    if given_num == 1:
        return [(1,1)] # We make it (1,1) to always make it a tuple since if its just (1) a TypeError will occur

    # We start checking if the number is divisible by 2 since we have already accounted for 1
    divisor = 2

    while given_num > 1:
        count = 0

        # The while loop will divide by the divisor (starting at 2) and if it has no remainder (meaning it's divisible by that factor), it will add 1 to the count
        while given_num % divisor == 0:    
            given_num //= divisor # Same as given_num = given_num // divisor (// is floor division)
            count += 1 # Same as count = count + 1

        # If the count for the prime factor is greater than 0, we append a tuple (2, count) to the factors list. 
        # So the tuple will represent the prime factor and it's exponent (how many time it appears)  
        if count > 0:
            factors.append((divisor, count))

        # If the prime factor is no longer divisble by 2, it will add 1 and continue checking
        divisor += 1

    return factors


# Function to format the ans 
# Example if the output is 2 2 2 the format will make it 2^3
def format(factors):

    # Making an empty list to store the formatted factors
    formatted_factors = []

    # Loop that checks the elements in the factors list (a touple containing the prime factor and its count)
    for factor, count in factors:
        
        # If a certain factor only appears once, the format makes it so that it just shows it by itself
        # So instead of 2^1, it will just show 1
        if count == 1:
            formatted_factors.append(str(factor))

        # If the count is greater than one, the format will make it so that we can see the (format)^(count)
        else:
            formatted_factors.append(f"{factor}^{count}") 
            # We need to put an f inside the parenthesis to make it a string because otherswise it will perform an operation

    return ' '.join(formatted_factors) 
    # This means that elements in the formatted factors list will be separated by a space (hence ' ') and the results will return




# Input for how many lines after it
N = int(input())

i = 0

# While i is less than N (number of lines) it will continue the while loop until the condition is no longer applicable (i is greater than N)

while (i < N):

    # Input to get a number
    given_num = int(input())
    
    # Getting the list with truples
    factors = prime_factor(given_num)

    # Formatting the list to make it pretty
    ans = format(factors)

    # Printing the final format ans
    print(ans)

    i = i + 1
    # i gets added by 1 and stops if i is greater than N (amount of lines)