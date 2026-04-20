name = 'John Doe'
age = 25

# This is a single line comment

"""
This is a multi-line string.
Here is some code commented out.

name = 'John Doe'
age = 25
"""

# isinstance() function checks if a variable is of a specific type
print(isinstance(name, str))  # True

# Which of the following is NOT a form of string concatenation ?

"""
developer = 'Jessica'
greeting = x'My name is {developer}.' # This is not a valid string concatenation method in Python. missing + between string (x) and variable

greeting = 'My name is '
developer = 'Jessica'

greeting += developer

developer = 'Jessica'
greeting = 'My name is ' + developer + '.'

developer = 'Jessica'
age = 30
greeting = 'My name is ' + developer + ' and I am ' + str(age) + ' years old.'
"""

# Which of the following functions is used to return the number of the characters in the string ?

len() # valid function to return the number of characters in a string
"""
length()
iscount()
counting()
# Not valid functions to return the number of characters in a string
"""

# What will result be in this example?

developer = 'Naomi'

result = developer.endswith('N') # ? -> False, because 'Naomi' does not end with 'N'
print(result)

# What happens when you add a float and an integer ?
""" 
The result will be a float. => In Python, when you add a float and an integer, the result is a float. The integer is implicitly converted to a float before the addition takes place.
The result will be an error message.
The result will be an integer.
The result will be None.
"""

 

# What will be printed to the console?

def greet():
    pass
    
print(greet()) # ? => None, because the function greet() does not return any value, so it returns None by default.

# What will be the result for the following code ?
message = 'Python is fun!'

print(message[0:6])  # ? => 'Python', because the slice [0:6] includes characters from index 0 to index 5 (6 is exclusive), which corresponds to the substring 'Python'.

# What will the following print to the console ?
example_list = ['example', 'dashed', 'name']

joined_str = ' '.join(example_list)
print(joined_str)  # ? => 'example dashed name', because the join() method concatenates the elements of the list into a single string, with a space (' ') as the separator between elements.

# str.maketrans() is a method in Python that creates a translation table for use with the str.translate() method. 
# It takes two arguments: the first is a string of characters to be replaced, and the second is a string of characters to replace them with. 
# The resulting translation table can then be used to perform character substitutions in a string using the translate() method.

# What will be the result for the following code?

int_1 = 4
int_2 = 2

print(int_1 ** int_2) # ? => 16, because 4 to the power of 2 is 16.

# What will be returned from the find() method if no substring occurrences are found in a string ?
# => -1, because the find() method returns the index of the first occurrence of the substring, or -1 if it is not found.

# What does floor division do in Python ?
# => Floor division (//) performs division and returns the largest integer less than or equal to the result.

# Which of the following functions is used to round a number to the nearest whole integer?
# => round(), because it returns the closest integer to the given number.