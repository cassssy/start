char_values = input()


char_values = char_values.replace(" ", "")
letters = [str.lower(x) for x in char_values]
print (letters)