my_int_1 = 56
my_int_2 = -4
print(type(my_int_1)) # <class 'int'>
print(type(my_int_2)) # <class 'int'>
# Integer Addition
sum_ints = my_int_1 + my_int_2
print('Integer Addition: ', sum_ints) # 52

my_int_1 = 56 
my_int_2 = 12
# Subtraction
sub_ints = my_int_1 - my_int_2 
print('Integer Subtraction: ', sub_ints) # 44

my_int_1 = 12
my_int_2 = 4

# Multiplication
product_ints = my_int_1 * my_int_2
print('Integer Multiplication:', product_ints)  # 48

my_int_1 = 56
my_int_2 = 12

# Division
div_ints = my_int_1 / my_int_2
print('Integer Division:', div_ints) # 4.666666666666667

my_float_1 = -12.0
my_float_2 = 4.9

print(type(my_float_1)) # <class 'float'>
print(type(my_float_2)) # <class 'float'>

my_float_1 = 5.4
my_float_2 = 12.0

float_addition = my_float_1 + my_float_2
print('Float Addition:', float_addition) # 17.4

my_float_1 = 5.4
my_float_2 = 12.0

float_subtraction = my_float_2 - my_float_1
print('Float Subtraction:', float_subtraction) # 6.6

my_float_1 = 5.4
my_float_2 = 12.0

float_multiplication = my_float_2 * my_float_1
print('Float Multiplication:', float_multiplication) # 64.8

my_float_1 = 5.4
my_float_2 = 12.0

float_division = my_float_2 / my_float_1
print('Float Division:', float_division) # 2.2222222222222223

my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float) # 61.4
print(type(sum_int_and_float)) # <class 'float'>

# The modulo operator (%) returns the remainder when the value on the left is divided by the value on the right:
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1
print('Integer Modulus:', mod_ints) # 8
print('Float Modulus:', mod_floats) # 1.999999999999993

# Floor division divides two numbers and returns the greatest integer less than or equal to the result. This is done with the double forward slash operator (//):
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats) # Float Floor Division: 2.0

my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation:', exp_ints) # Integer Exponentiation: 951166013805414055936
print('Float Exponentiation:',  exp_floats) # Float Exponentiation: 614787626.1765089

# Exponentiation raises a number to the power of another, and is done with the double asterisk operator (**):

my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation:', exp_ints) # Integer Exponentiation: 951166013805414055936
print('Float Exponentiation:',  exp_floats) # Float Exponentiation: 614787626.1765089

# Sometimes, you might notice that the result of an operation involving floats has more decimal digits than expected. 
# For example, the sum 0.1 + 0.2 equals 0.30000000000000004 instead of 0.3
# This happens because numbers are stored in binary format, and some fractions cannot be represented exactly in binary. 
# As a result, they are stored as finite approximations, in the same way the fraction 1/3 cannot be represented with a finite number of digits in decimal 
# and is truncated after a certain number of its infinite digits (0.33333...).

# This leads to small rounding errors.
# Python also provides built-in functions for converting either numeric data or strings into integers or floats.

# The float() function returns a floating-point number constructed from the given number:
my_int_1 = 56
my_float_1 = float(my_int_1)

print(my_float_1)  # 56.0
print(type(my_float_1))  # <class 'float'>

#The int() function returns an integer constructed from the given number:
my_float = 12.92563
my_int = int(my_float)

print(my_int)  # 12
print(type(my_int))  # <class 'int'>

# Also, you can use the same built-in functions to convert a string into either a float or integer:
my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))  # 45 <class 'int'>
print(converted_float, type(converted_float))  # 7.8 <class 'float'>

# Here are some other methods Python provides for working with integers and floats.
# round(): Rounds a number to the specified number of decimal places. 
# By default this function rounds to the nearest integer, and returns a whole number with no decimal places:

my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1) # 5
print(rounded_int_2) # 4.3

# abs(): returns the absolute value of a number,
num = -15

absolute_value = abs(num)
print(absolute_value) # 15

# pow(): raises a number to the power of another or performs modular exponentiation.
result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3

# variable <operator>= value is a shorthand for variable = variable <operator> value.
my_var = 10
my_var += 5

print(my_var) # 15

my_var = 10
my_var = my_var + 5

print(my_var) # 15

# The subtraction assignment operator (-=) subtracts the right operand from the left variable and stores the difference in the left variable:
count = 14
count -= 3

print(count) # 11

# The multiplication assignment operator (*=) multiplies the left variable by the right operand and stores the product back in the left variable:
product = 65
product *= 7

print(product) # 455

# The division assignment operator (/=) divides the left variable by the right and stores the result back in the left variable:
price = 100
price /= 4

print(price) # 25.0

# The floor division operator (//=) floor‑divides the left variable by the right and stores the result back in the left variable:
total_pages = 23
total_pages //= 5

print(total_pages) # 4

# The modulus assignment operator (%=) computes the remainder of the left variable divided by the right and stores it back in the left variable:
bits = 35
bits %= 2

print(bits) # 1

# The exponentiation assignment operator (**=) raises the left variable to the power of the right and stores the result back in the left variable:
power = 2
power **= 3

print(power) # 8

# You can use some augmented assignment operators with strings, too. For example, the addition assignment operator makes it easy to concatenate strings:
greet = 'Hello'
greet += ' World'

print(greet) # Hello World

# And the multiplication assignment operator can be used to repeat a string:    
greet = 'Hello'
greet *= 3

print(greet) # HelloHelloHello

# greet = 'Hello'
# greet -= ' World'

# print(greet) # TypeError: unsupported operand type(s) for -=: 'str' and 'str'


# greet = 'Hello'
# greet /= 'World'

# print(greet) # TypeError: unsupported operand type(s) for /=: 'str' and 'str' 

# If you're wondering if increment and decrement operators (++ and  --) work in Python, they don't. 
# That's because Python deliberately avoids C-style increment and decrement shortcuts in order to keep the language clear and explicit.
# Instead of x++, you can simply write x += 1, which makes it obvious that you're incrementing the value of x by 1.
# Writing ++x in Python just applies the unary plus twice, and does not increment anything:
my_var = 5

print(+my_var)   # 5
print(++my_var)  # 5
print(+++my_var) # 5

my_var += 1

print(my_var) # 6

