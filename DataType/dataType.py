# Part 1
# pas besoin de déclarer explicitemnt les types de variables en Python avec char, var, int , etc ...
name = 'John Doe'
age = 25

# en python, les noms des variables sont sensibles à la casse 
# Exemple : Name != name   
# de même, les noms de variables peuvent commener avec un _ underscore ou une lettre, mais pas avec un chiffre
# exemple qui génère une erreur :

# 5variable_name = "test" # ceci n'est pas valide
my_variable_name = 'freeCodeCamp' # est valide
userAge = 30 # est valide

# Part 2
# string name = 'John Doe'
# int age = 25

myIntergervar = 10
print('Integer:', myIntergervar) # Affiche Integer: 10

myFloatvar = 5.5
print('Float:', myFloatvar) # Affiche Float: 5.5

myStringvar= 'hello'
print('String:', myStringvar) # Affiche String: hello

myBooleanvar = True
print('myBooleanvar:', myBooleanvar) # Affiche Boolean: True

mySetvar = {1, 5, 8}
print('Set:', mySetvar) # Affiche Set: {1, 5, 8}

myDictionaryvar = {'name': 'Alice', 'age': 24}
print('Dictionary:', myDictionaryvar) # Affiche Dictionary: {'name': 'Alice', 'age': 24}

myTuplevar = (3, 5, 6)
print('Tuple:', myTuplevar) # Affiche Tuple: (3, 5, 6)

myRangevar = range(5)
print('Range:', myRangevar) # Affiche Range: range(0, 5)

myListvar = [22, 'Hello world', 3.14, True]
print('List:', myListvar) # Affiche List: [22, 'Hello world', 3.14, True]

myNonevar = None
print('None:', myNonevar) # Affiche None: None

# Part 3
myVar1 = 'Hello world!'
myVar2 = 19
print(type(myVar1)) # <class 'str'>
print(type(myVar2)) # <class 'int'>

my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 5, 8}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 5, 8)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>

# The built-in isinstance() function lets you check if a variable matches a specific data type. 
# It takes in an object and the type you want to check it against, then returns a boolean. 
# Here are some examples:

isinstance('Hello world', str) # True
isinstance(True, bool) # True
isinstance(42, int) # True
isinstance('John Doe', int) # False

