myStr1 = 'Hello'
myStr2 = 'World'

str3Concat = myStr1 + ' ' + myStr2
print(str3Concat)

name = 'Matt Ju'
age = 26

nameAndAge = name + age
print(nameAndAge) ##Error Type

nameAndAge = name + ' '+ str(age)
print(nameAndAge)

name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26

name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15