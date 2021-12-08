


# Variables
'''
if we want to use value in one place,
then directly use the value
'''
print(10)
print(10+20)
print(10+20+30)

'''
if we want to use value in multiple places,
then assign the value to a variable
'''
x = 10
print(x)
print(x+20)

res = 10+20
print(res)
print(res+100)


print("Addition is : ",10+20)

x = 40
y = 50
print("Addition is : ", x+y)
print("Subtraction is : ", x-y)
print("Mulitplication is : ", x*y)
print("Division is : ", x/y)

x = 10
y = 20
res = x+y
print("Addition is : ", res)
print("Addition is : ", res+100)

print("-----Single usage------")
for char in 'Hello World':
    print("Character : ", char)

print("-----Multiple usage-----")

msg = 'Hello World'
for char in msg:
    print("Character : ", char)

"""
A variable is any characteristics, number, or quantity that can be measured or counted.
A variable may also be called a data item. Age, sex, business income and expenses,
country of birth, capital expenditure,
class grades, eye colour and vehicle type are examples of variables.
"""

# An integer assignment
age = 45

# A floating point
salary = 1456.8

# A string
name = "John"

print(age)
print(salary)
print(name)

# declaring the var
Number = 100

# display
print( Number)

# declaring the var
Number = 100

# display
print("Before declare: ", Number)

# re-declare the var
Number = 120.3

print("After re-declare:", Number)

#assigning single value to multiple variables:?


a = b = c = 10

print(a)
print(b)
print(c)

#assigning different values to multiple variables:?
a, b, c = 1, 20.2, "GeeksforGeeks"

print(a)
print(b)
print(c)

#Can we use the same name for different types?
a = 10
a = "GeeksforGeeks"

print(a)

#How does + operator work with variables?

a = 10
b = 20
print(a + b)

a = "Geeksfor"
b = "Geeks"
print(a + b)

#Can we use + for different types also?
a = 10
b = "Geeks"
print(a+b)


x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))


x = "John"
# is the same as
x = 'John'


a = 4
A = "Sally"
#A will not overwrite a

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z =  x + y
print(z)


x = 5
y = 10
print(x + y)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

num = 100
str = "BeginnersBook"
print(num)
print(str)

x = 10
y = 20
print(x + y)

p = "Hello"
q = "World"
print(p + " " + q)

website = "apple.com"
print(website)

website = "apple.com"
print(website)

# assigning a new value to website
website = "programiz.com"

print(website)

