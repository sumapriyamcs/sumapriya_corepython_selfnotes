#sequence_type:
"""In Python, sequence is the ordered collection of similar or different data types.
Sequences allows to store multiple values in an organized and efficient fashion. There
are several sequence types in Python"""

### STRING_DATATYPE

"""
-->The string formatting is used to print the string exactly the way we want. In the string formatting we use the {} as the place holders and use the format() method to fill the placeholders. We pass the values to the format() method.
exmaple:
--------
a = {'name': 'suma', 'age' : 26}
sentence = 'my name is {}, age is {}'.format(a['name'], a['age'])
print(sentence)

-->we can also grab the specific things. Directly write the values in placeholders.
example:
--------
a = {'name': 'suma', 'age' : 26}
sentence = 'my name is {0[name]}, age is {1[age]}'.format(a,a)
print(sentence)

-->In the above program we just write the dictionary a 2 times in the format(). Instead of the we can write the 'a' one time and write the 0 in the all the place holders. which means the values in the dictionary will be passed to the placeholders. 
example:
---------
a = {'name': 'suma', 'age' : 26}
sentence = 'my name is {0[name]}, age is {0[age]}'.format(a)
print(sentence)

-->This is the same way that we access the list values also.
exmaple:
----------
a = {'name': 'suma', 'age' : 26}
l = ['suma', 26]
sentence = 'my name is {0[0]}, age is {0[1]}'.format(l)
print(sentence)

-->we can put the numbers in the placeholders, like which value should by stored in which placeholder. the number in the placeholder denotes the order of the values we passed in the fomat() method.
exmpale:
---------
a = {'name': 'suma', 'age' : 26}
sentence = 'my name is {0}, age is {1}'.format(a['name'], a['age'])
print(sentence)

->we can also use the tags.
example:
--------
tag = h1
text  = 'this is the heading tag'
sentence = '<{0}> {1} </{0}>'.format(tag, text)
print(sentence)

----------------------------------------------------------------------------------------------------------

-->Shorthand if else statement
example:
--------
a = input(int("enter the fist number"))
b = input(int("entere the second number"))
print(" b is greater than a") if a < b else print("a is greater than b")
"""