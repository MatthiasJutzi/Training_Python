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

# programming_languages = ['Python', 'Java', 'C++', 'Rust']
# programming_languages[10] = 'JavaScript'
"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list assignment index out of range
"""
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # ['Jane Doe', 'Python Developer']

programming_languages = ['Python', 'Java', 'C++', 'Rust']

'Rust' in programming_languages # True
'JavaScript' in programming_languages # False

developer = ['Alice', 25, ['Python', 'Rust', 'C++']]

developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2] # ['Python', 'Rust', 'C++']
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2][1] # 'Rust', here we are accessing the second element of the list at index 2, which is the list ['Python', 'Rust', 'C++'], and then we are accessing the second element of that list, which is 'Rust'.

developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'

developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']

# developer = ['Alice', 34, 'Rust Developer']
# name, age, job, city = developer
"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: not enough values to unpack (expected 4, got 3)
"""
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
desserts[1:4] # ['Cookies', 'Ice Cream', 'Pie'] here we are slicing the list from index 1 to index 4 (exclusive), which gives us the elements at index 1, 2, and 3.

numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2] # [2, 4, 6], here we are slicing the list starting from index 1 and then taking every second element (step of 2), which gives us the elements at index 1, 3, and 5.

# appened() method is used to add an element to the end of a list
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]