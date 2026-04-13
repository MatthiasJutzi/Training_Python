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

