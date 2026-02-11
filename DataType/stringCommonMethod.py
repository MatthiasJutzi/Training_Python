# upper()
myStr1 = 'Hello World'
uppercase_myStr1 = myStr1.upper()
print(uppercase_myStr1) # HELLO WORLD

# lower()
myStr2 = 'Hello World'
lowercase_myStr2 = myStr2.lower()
print(lowercase_myStr2) # hello world

# strip()
myStr3 = ' hello world '
stripmyStr3 = myStr3.strip()
print(stripmyStr3) # "hello world"

# replace(old, new)
myStr4 = 'hello world'
replacemyStr4 = myStr4.replace('hello', 'hi')
print(replacemyStr4) # hi world

# split()
myStr5 = 'hello world'
splitmyStr5 = myStr5.split()
print(splitmyStr5) # ['hello', 'world']

# join()
myList1 = ['hello', 'world']
joinmyList1 = ' '.join(myList1)
print(joinmyList1) # hello world

# startwith(prefix)
myStr6 = 'hello world'
startwithmyStr6 = myStr6.stratwith('hello')
print(startwithmyStr6) # True

# enwith(suffix)
myStr7 = 'hello world'
endwithmyStr7 = myStr7.endwith('world')
print(endwithmyStr7) # True

# find(substring)
myStr8 = 'hello world'
findmyStr8 = myStr8.find('world')
print(findmyStr8) # 6

# count(substring)
myStr9 = 'hello world'
countmyStr9 = myStr9.count('o')
print(countmyStr9) # 2

# capitalize()
myStr10 = 'hello world'
capitalizemyStr10 = myStr10.capitalize()
print(capitalizemyStr10)

# isupper()
myStr11 = 'hello world'
isuppermyStr11 = myStr11.usupper()
print(isuppermyStr11)

# islower()
myStr12 = 'hello world'
islowermyStr12 = myStr12.islower()
print(islowermyStr12)

# title()
myStr13 = 'hello world'
titlemyStr13 = myStr13.title()
print(titlemyStr13)


myList1 = ['Red','Green','Blue']
for i in myList1:
    print(i)

mySet1 = {'Red','Green','Blue'}
for i in mySet1:
    print(i)

MyDict1 = {'name':'John','age':30,'city':'New York'}
for value in MyDict1.values():
    print(value)


