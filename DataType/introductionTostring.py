my_str_1 = 'Hello'
my_str_2 = 'World'

# example du string multi-lignes
my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''
print(my_str_4)

msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

my_str = 'Hello world'
print(len(my_str))  # 11

my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w

my_str = 'Hello world'
print(my_str[-1])  # d
print(my_str[-2]) # l

greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment

#String length
my_string = 'Hello world!'
print(len(my_string))  # 13 

# Cancaténation
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World