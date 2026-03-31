print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True

""" if condition:
    pass # Code to execute if condition is True """

age = 18

if age >= 18:
    print('You are an adult') # You are an adult

    age = 18

""" if age >= 18:
print('You are an adult') # IndentationError: expected an indented block after 'if' statement on line 20
 """
age = 12

if age >= 18:
    print('You are an adult') # Nothing shows up in the terminal

""" if condition:
   pass # Code to execute if condition is True
else:
   pass # Code to execute if condition is False """

age = 12

if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult yet') # You are not an adult yet

age = 12

""" if age >= 18:
    print('You are an adult')
print('Almost there!')
else: # SyntaxError: invalid syntax
    print('You are not an adult yet') """

""" if condition1:
   pass # Code to execute if condition1 is True
elif condition2:
   pass # Code to execute if condition1 is False and condition2 is True
else:
   pass # Code to execute if all conditions are False
 """

age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child') # You are a child

age = 2

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant') # You are a toddler or an infant

is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')

print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True

is_citizen = True
age = 25

print(is_citizen and age) # 25

is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')

age = 19
is_employed = False

print(age or is_employed) # 19

age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')

print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy

is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')

age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can watch the movie.")
else:
    print("You can't watch the movie.")
