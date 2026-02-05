myStr1 = 'Hello World'
print(myStr1[0])  # H
print(myStr1[6])  # W
print(myStr1[-1]) # d

# String slicing lets you extract a portion of a string or work with only a specific part of it. Here's the basic syntax:
# string[start:stop]

# If you want to extract characters from a certain index to another, you just separate the start and stop indices with a colon:
myStr2 = 'Hello World'
print(myStr2[1:4]) # ell

# Note that the stop index is non-inclusive, so [1:4] just extracted the characters from index 1, and up to, but not including, the character at index 4.
# You can also omit the start and stop indices, and Python will default to 0 or the end of the string, respectively. For example, here's what happens if you omit the start index:
myStr1 = 'Hello World'
print(myStr1[:7]) # Hello W

# This extracts everything from index 0 up to (but not including), the character at index 7. And here's what happens if you omit the stop index:
myStr1 = 'Hello World'
print(myStr1[8:]) # rld
# This extracts everything from the character at index 8 until the end of the string.

# Note that slicing a string does not modify the original string:
myStr1 = 'Hello World'
print(myStr1[8:]) # rld
print(myStr1) # Hello World

#You can also omit both the start and stop indices, which will extract the whole string:
myStr1 = 'Hello World'
print(myStr1[:]) # Hello World

# Apart from the start and stop indices, there's also an optional step parameter, which is used to specify the increment between each index in the slice.
# Here's the syntax for that:
# string[start:stop:step]

# In the example below, the slicing starts at index 0, stops before 11, and extracts every second character:
myStr1 = 'Hello World'
print(myStr1[0:11:2]) #  HloWrd

# A helpful trick you can do with the step parameter is to reverse a string by setting step to -1, and leaving start and stop blank:
myStr1 = 'Hello World'
print(myStr1[::-1]) # dlroW olleH

