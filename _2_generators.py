'''
What is Python Generator?
Python Generators are the functions that return the traversal object and used to create iterators.
It traverses the entire items at once. The generator can also be an expression
in which syntax is similar to the list comprehension in Python.

There is a lot of complexity in creating iteration in Python;
we need to implement __iter__() and __next__() method to keep track of internal states.

It is a lengthy process to create iterators. That's why the generator plays
an essential role in simplifying this process. If there is no value found in iteration,
it raises StopIteration exception.

How to Create Generator function in Python?

It is quite simple to create a generator in Python. It is similar to the normal
function defined by the def keyword and uses a yield keyword instead of return. Or
we can say that if the body of any function contains a yield statement,
it automatically becomes a generator function.
'''


def simple():
    for i in range(10):
        if (i % 2 == 0):
            yield i

        # Successive Function call using for loop


for i in simple():
    print(i)
'''
#yield vs. return

The yield statement 
is responsible for controlling the flow of the generator function. 
It pauses the function execution by saving all states and yielded to the caller. 
Later it resumes execution when a successive function is called.
We can use the multiple yield statement in the generator function.

The return statement returns a value and terminates the whole 
function and only one return statement can be used in the function.

'''
#multiple yield:
def multiple_yield():
    str1 = "First String"
    yield str1

    str2 = "Second string"
    yield str2

    str3 = "Third String"
    yield str3


obj = multiple_yield()
print(next(obj))
print(next(obj))
print(next(obj))

def sum():
    a=10
    b=20
    res=a+b
    yield res
fun=sum()
print(next(fun))

def mul():
    a=100
    b=200
    res=a*b
    yield res
dec=mul()
print(next(dec))
'''
#Difference between Generator function and Normal function

Normal function contains only one Lreturn statement whereas generator 
function can contain one or more yield statement.
When the generator functions are called, the normal function is paused 
immediately and control transferred to the caller.
Local variable and their states are remembered between successive calls.
StopIteration exception is raised automatically when the function terminates.

#Generator Expression

We can easily create a generator expression without using user-defined function. 
It is the same as the lambda function which creates an anonymous function; 
the generator's expressions create an anonymous generator function.

The representation of generator expression is similar to the Python list comprehension. 
The only difference is that square bracket is replaced by round parentheses. 
The list comprehension calculates the entire list, whereas the generator 
expression calculates one item at a time.


'''
list = [1, 2, 3, 4, 5, 6, 7]

# List Comprehension
z = [x ** 3 for x in list]

# Generator expression
a = (x ** 3 for x in list)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(z)


def table(n):
    for i in range(1, 11):
        yield n * i
        i = i + 1


for i in table(15):
    print(i)

def my_gen(x):
  while(x>0):
    if x%2==0:
      yield 'Even'
    else:
      yield 'Odd'
    x-=1
for i in my_gen(7):
  print(i)

def mygen():
  i=7
  while i>0:
    yield i
    i-=1
for i in mygen():
  print(i)

mylist=[1,3,6,10]
res=(x**2 for x in mylist)
print(res)
a=(x**2 for x in mylist)
print(next(a))
print(next(a))
print(next(a))
print(next(a))


def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30
gen = mygenerator()
next(gen)
next(gen)
next(gen)

def square_of_sequence(x):
    for i in range(x):
        yield i*i
gen=square_of_sequence(5)
while True:
    try:
        print ("Received on next(): ", next(gen))
    except StopIteration:
        break

squres = square_of_sequence(5)
for sqr in squres:
    print(sqr)


squres = (x*x for x in range(5))
print(next(squres))
print(next(squres))
print(next(squres))
print(next(squres))
print(next(squres))


# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3

# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)

# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)

# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)

print(list_)
print(generator)

# Initialize the list
my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)
print(next(a))

print(next(a))

print(next(a))

print(next(a))

next(a)

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))

my_list = ['a', 'b', 'c', 'd', 'e']
my_gen = iter(my_list)
type(my_gen)
for i in my_gen:
   print(i)

   