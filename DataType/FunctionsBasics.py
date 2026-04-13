# Part 1
# input() function is used to take input from the user. It always returns a string.
name = input("What is your name? ")
print("Hello " + name)

# int() converts a number, boolean, and a numeric string into an integer:
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 

# for custom function we uuse def keyword:
def hello():
    print("Hello World")

hello() # calling the function to execute the code inside it

# Exampe of function for an addition of two numbers:
def calculate_sum(a,b):
    print(a+b)

calculate_sum(1,2) #3

# Not the good way to use function, because it does not return any value, it just prints the result. We can use return statement to return the result from the function:
def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None

# Good way to use function with return statement:
def calculate_sum(a, b):
    return a + b    
my_sum = calculate_sum(3, 1) # 4
print(my_sum) # 4

# function return "None" if there is no return statement in the function or if the return statement does not return any value.

# Part 2
def my_func():
    my_var = 10
    print(my_var)

def my_func():
    my_var = 10 # Locally scoped to my_func
    print(my_var)

my_func() # 10

print(my_var) # NameError: name 'my_var' is not defined

def outer_func():
    msg = 'Hello there!'

    def inner_func():
        print(msg)

    inner_func()

outer_func() # Hello there!

def outer_func():
    msg = 'Hello there!'
    print(res)

    def inner_func():
        res = 'How are you?'
        print(msg)

    inner_func()

outer_func() # NameError: name 'res' is not defined

def outer_func():
    msg = 'Hello there!'
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal res  # Allow modification of an enclosing variable
        res = 'How are you?'
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(res)  # Now res is accessible and modified

outer_func()

# Output:
# Hello there!
# How are you?

my_var = 100

def show_var():
    print(my_var)

show_var() # 100
print(my_var) # 100

my_var_1 = 7

def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)

show_vars() # 7 10

# my_var_2 is now a global variable and can be accessed anywhere in the program
print(my_var_2) # 10

my_var = 10  # A global variable

def change_var():
    global my_var  # Allows modification of a global variable
    my_var = 20

change_var()

print(my_var)  # my_var is now modified globally to 20

print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False
