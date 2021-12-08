"""
#There are mainly two types of functions.

1.User-define functions - The user-defined functions are those define by the user
to perform the specific task.

2.Built-in functions - The built-in functions are those functions that are pre-defined in Python.

# userdefined function programs::

1. write a program to add the two numbers?
# Program to illustrate
# the use of user-defined functions

def add_numbers(x,y):
   sum = x + y
   return sum

num1 = 5
num2 = 6

print("The sum is", add_numbers(num1, num2))

# builtin functions prgrams::
1.abs(-7)

output:7

2. all({'*','',''})
   all([' ',' ',' '])

output: false
        true
3.any((1,0,0))
any((0,0,0))

Output:
True
False

4.ascii()
output: “‘\\u0219′”


5.Python abs() Function Example

#  integer number
integer = -20
print('Absolute value of -40 is:', abs(integer))

#  floating number
floating = -20.83
print('Absolute value of -40.83 is:', abs(floating))

6.Python all() Function Example

# all values true
k = [1, 3, 4, 6]
print(all(k))

# all values false
k = [0, False]
print(all(k))

# one false value
k = [1, 3, 7, 0]
print(all(k))

# one true value
k = [0, False, 5]
print(all(k))

# empty iterable
k = []
print(all(k))

7.Python bin() Function Example

x =  10
y =  bin(x)
print (y)

8.python bool() function with example?
test1 = []
print(test1,'is',bool(test1))
test1 = [0]
print(test1,'is',bool(test1))
test1 = 0.0
print(test1,'is',bool(test1))
test1 = None
print(test1,'is',bool(test1))
test1 = True
print(test1,'is',bool(test1))
test1 = 'Easy string'
print(test1,'is',bool(test1))

9.Python bytes() Example

string = "Hello World."
array = bytes(string, 'utf-8')
print(array)

10.Python callable() Function Example

x = 8
print(callable(x))

11.Python compile() Function Example

# compile string source to code
code_str = 'x=5\ny=10\nprint("sum =",x+y)'
code = compile(code_str, 'sum.py', 'exec')
print(type(code))
exec(code)
exec(x)

12.Python exec() Function Example

x = 8
exec('print(x==8)')
exec('print(x+4)')


13.Python sum() Function Example

s = sum([1, 2,4 ])
print(s)

s = sum([1, 2, 4], 10)
print(s)

14.Python any() Function Example

l = [4, 3, 2, 0]
print(any(l))

l = [0, False]
print(any(l))

l = [0, False, 5]
print(any(l))

l = []
print(any(l))

15.Python ascii() Function Example

normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))

print('Pyth\xf6n is interesting')

16.Python bytearray() Example

string = "Python is a programming language."

# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)

17.Python eval() Function Example

x = 8
print(eval('x + 1'))


18.Python float() Example

# for integers
print(float(9))

# for floats
print(float(8.19))

# for string floats
print(float("-24.27"))

# for string floats with whitespaces
print(float("     -17.19\n"))

# string float error
print(float("xyz"))


19.Python format() Function Example

# d, f and b are a type

# integer
print(format(123, "d"))

# float arguments
print(format(123.4567898, "f"))

# binary format
print(format(12, "b"))


20.Python frozenset() Example

# tuple of letters
letters = ('m', 'r', 'o', 't', 's')

fSet = frozenset(letters)
print('Frozen set is:', fSet)
print('Empty frozen set is:', frozenset())

21.Python getattr() Function Example

class Details:
    age = 22
    name = "Phill"

details = Details()
print('The age is:', getattr(details, "age"))
print('The age is:', details.age)

22.Python globals() Function Example

age = 22

globals()['age'] = 22
print('The age is:', age)


23.Python hasattr() Function Example

l = [4, 3, 2, 0]
print(any(l))

l = [0, False]
print(any(l))

l = [0, False, 5]
print(any(l))

l = []
print(any(l))

24.Python iter() Function Example

# list of numbers
list = [1,2,3,4,5]

listIter = iter(list)

# prints '1'
print(next(listIter))

# prints '2'
print(next(listIter))

# prints '3'
print(next(listIter))

# prints '4'
print(next(listIter))

# prints '5'
print(next(listIter))

25.Python len() Function Example

strA = 'Python'
print(len(strA))

26.Python list() Example

# empty list
print(list())

# string
String = 'abcde'
print(list(String))

# tuple
Tuple = (1,2,3,4,5)
print(list(Tuple))
# list
List = [1,2,3,4,5]
print(list(List))


27.Python locals() Function Example

def localsAbsent():
    return locals()

def localsPresent():
    present = True
    return locals()

print('localsNotPresent:', localsAbsent())
print('localsPresent:', localsPresent())

28.Python map() Function Example

def calculateAddition(n):
  return n+n

numbers = (1, 2, 3, 4)
result = map(calculateAddition, numbers)
print(result)

# converting map object to set
numbersAddition = set(result)
print(numbersAddition)


29.Python memoryview () Function Example

#A random bytearray
randomByteArray = bytearray('ABC', 'utf-8')

mv = memoryview(randomByteArray)

# access the memory view's zeroth index
print(mv[0])

# It create byte from memory view
print(bytes(mv[0:2]))

# It create list from memory view
print(list(mv[0:3]))



30.Python object() Example

python = object()

print(type(python))
print(dir(python))

31.Python chr() Function Example

# Calling function
result = chr(102) # It returns string representation of a char
result2 = chr(112)
# Displaying result
print(result)
print(result2)
# Verify, is it string type?
print("is it string type:", type(result) is str)

32.Python complex() Example

# Python complex() function example
# Calling function
a = complex(1) # Passing single parameter
b = complex(1,2) # Passing both parameters
# Displaying result
print(a)
print(b)

33.Python enumerate() Function Example

# Calling function
result = enumerate([1,2,3])
# Displaying result
print(result)
print(list(result))

34.Python dict() Example

# Calling function
result = dict() # returns an empty dictionary
result2 = dict(a=1,b=2)
# Displaying result
print(result)
print(result2)

35.Python filter() Function Example

# Python filter() function example
def filterdata(x):
    if x>5:
        return x
# Calling function
result = filter(filterdata,(1,2,6))
# Displaying result
print(list(result))

36.Python hash() Function Example

# Calling function
result = hash(21) # integer value
result2 = hash(22.2) # decimal value
# Displaying result
print(result)
print(result2)


37.Python help() Function Example

# Calling function
info = help() # No argument
# Displaying result
print(info)

38.Python min() Function Example

# Calling function
small = min(2225,325,2025) # returns smallest element
small2 = min(1000.25,2025.35,5625.36,10052.50)
# Displaying result
print(small)
print(small2)

40.Python set() Function Example

# Calling function
result = set() # empty set
result2 = set('12')
result3 = set('javatpoint')
# Displaying result
print(result)
print(result2)
print(result3)

41.Python hex() Function Example

# Calling function
result = hex(1)
# integer value
result2 = hex(342)
# Displaying result
print(result)
print(result2)

42.Python id() Function Example

# Calling function
val = id("Javatpoint") # string object
val2 = id(1200) # integer object
val3 = id([25,336,95,236,92,3225]) # List object
# Displaying result
print(val)
print(val2)
print(val3)


43.Python slice() Function Example

# Calling function
result = slice(5) # returns slice object
result2 = slice(0,5,3) # returns slice object
# Displaying result
print(result)
print(result2)


44.Python sorted() Function Example

str = "javatpoint" # declaring string
# Calling function
sorted1 = sorted(str) # sorting string
# Displaying result
print(sorted1)

45.Python next() Function Example

number = iter([256, 32, 82]) # Creating iterator
# Calling function
item = next(number)
# Displaying result
print(item)
# second item
item = next(number)
print(item)
# third item
item = next(number)
print(item)


46. Python input() Function Example

# Calling function
val = input("Enter a value: ")
# Displaying result
print("You entered:",val)


47.Python int() Function Example

# Calling function
val = int(10) # integer value
val2 = int(10.52) # float value
val3 = int('10') # string value
# Displaying result
print("integer values :",val, val2, val3)

48.Python ord() function Example

# Code point of an integer
print(ord('8'))

# Code point of an alphabet
print(ord('R'))

# Code point of a character
print(ord('&'))


49.Python pow() function Example

# positive x, positive y (x**y)
print(pow(4, 2))

# negative x, positive y
print(pow(-4, 2))

# positive x, negative y (x**-y)
print(pow(4, -2))

# negative x, negative y
print(pow(-4, -2))

50.Python print() function Example

print("Python is programming language.")

x = 7
# Two objects passed
print("x =", x)

y = x
# Three objects passed
print('x =', x, '= y')


51.Python range() function Example

# empty range
print(list(range(0)))

# using the range(stop)
print(list(range(4)))

# using the range(start, stop)
print(list(range(1,7 )))


52.Python reversed() function Example

# for string
String = 'Java'
print(list(reversed(String)))

# for tuple
Tuple = ('J', 'a', 'v', 'a')
print(list(reversed(Tuple)))

# for range
Range = range(8, 12)
print(list(reversed(Range)))

# for list
List = [1, 2, 7, 5]
print(list(reversed(List)))

53.Python round() Function Example

#  for integers
print(round(10))

#  for floating point
print(round(10.8))

#  even choice
print(round(6.6))
Python tuple() Function Example

t1 = tuple()
print('t1=', t1)

# creating a tuple from a list
t2 = tuple([1, 6, 9])
print('t2=', t2)

# creating a tuple from a string
t1 = tuple('Java')
print('t1=',t1)

# creating a tuple from a dictionary
t1 = tuple({4: 'four', 5: 'five'})
print('t1=',t1)



------------------------------------------------------------------------------------
# Requirement : Sum of 2 given numbers

# A. With out functions
        # I. STATE
num1 = 10
num2 = 20
        # II. BEHAVIOR
result = num1 + num2
print("Addition is : ", result)


print("-----------Using functions--------")
# B. With Functions
        # I. STATE
num1 = 10
num2 = 20
        # II. BEHAVIOR

# Function definition
def sum(n1, n2):       # function signature
    result = n1 + n2   # function body
    print("Addition is : ", result)

# Function calling
sum(num1, num2)
sum(10, 20)
--------------------------------------------------------------------------

# Requirement : factorial of given numbers

# A. With out functions
        # I. STATE
num = int(input("Enter a no"))
f = 1
# II. Behavior
while num>1:
 f = f * num

 num -= 1

print("factorial of a no", f)


# B. With  functions
num = int(input("Enter a no"))
# II. Behavior
# Function Definition
def fact(i):
 f = 1
 while i>0:
  f = f * i
  i-=1
 print("Factorial of a no:" ,f)

fact(num)

-----------------------------------------------------------------------------------------

# Requirement : Check greatest no of  given 3 numbers

# A. With out functions
# I. STATE
num1 = int(input("Enter a 1st no"))
num2 = int(input("Enter a 2nd no"))
num3 = int(input("Enter a 3rd no"))

# II. Behavior
if num1 > num2 and num1 > num3:
    print("Greatest no :",num1)

elif num2 > num3:
    print("Greatest no :",num2)
else:
 print("Greatest no :",num3)


# A. With  functions

# II. Behavior
# Function Definition
def greatest(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        print("Greatest no :", n1)

    elif n2 > n3:
        print("Greatest no :", n2)
    else:
        print("Greatest no :", n3)


# I. STATE
num1 = int(input("Enter a 1st no"))
num2 = int(input("Enter a 2nd no"))
num3 = int(input("Enter a 3rd no"))
greatest(num1,num2,num3)

# print marks as a subject wise?

def marks(english, math = 85, science = 80):
print('Marks in : English is - ', english,', Math - ',math, ', Science - ',science)
marks(71, 77)
marks(65, science = 74)
marks(science = 70, math = 90, english = 75)

#average of two numbers?
def avg_number(x, y):
    print("Average of ",x," and ",y, " is ",(x+y)/2)
avg_number(3, 4)

#squares of two numbers?

def nsquare(x, y):
    return (x*x + 2*x*y + y*y)
print("The square of the sum of 2 and 3 is : ", nsquare(2, 3))

#print the marks as the subject wise?

def marks(english, math = 85, science = 80):
print('Marks in : English is - ', english,', Math - ',math, ', Science - ',science)
marks(71, 77)
marks(65, science = 74)
marks(science = 70, math = 90, english = 75)

#su of all the numbers present in the tuple?

def sum(*numbers):
     s = 0
     for n in numbers:
           s += n
     return s

print(sum(1,2,3,4))


"""