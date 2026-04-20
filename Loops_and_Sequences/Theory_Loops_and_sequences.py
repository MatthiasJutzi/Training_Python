# Theory loops and sequences
# Loops are used to repeat a block of code multiple times. There are two types of loops in Python: for loops and while loops.

# exemple of a list
swiss_cities = ["Zurich", "Geneva", "Basel", "Bern"]

swiss_cities[0]
print(swiss_cities[0]) # ? => 'Zurich', because list indexing starts at 0, so swiss_cities[0] refers to the first element of the list, which is 'Zurich'.
swiss_cities[-1]
print(swiss_cities[-1]) # ? => 'Bern', because negative indexing starts from the end of the list, so swiss_cities[-1] refers to the last element of the list, which is 'Bern'.

citie_name = "Geneva"
list(citie_name) # ? => ['G', 'e', 'n', 'e', 'v', 'a'], because the list() function converts a string into a list of its individual characters.

# to calculate the length of a list, we can use the len() function
numbers_list = [1, 2, 3, 4, 5]
len(numbers_list) # ? => 5, because the len() function returns the number of items in the list, and there are 5 items in numbers_list.

#to update the avalue of an element in a list, we can use indexing to assign a new value to that index. For example:
swiss_cities[1] = "Lausanne"
print(swiss_cities) # ? => ['Zurich', 'Lausanne', 'Basel', 'Bern'], because we assigned the value "Lausanne" to the index 1 of the swiss_cities list, which replaced the previous value "Geneva".

