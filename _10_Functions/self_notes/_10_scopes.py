#scope of variable  LEGB rule in python

"""

#What is Python Variable Scope?

The scope of a variable in python is that part of the code where it is visible.

#Types of Python Variable Scope?
1.local scope
2. enclosing scope
3. global scope
4. builtin scope


1. local scope?

Whenever you define a variable within a function, its scope lies ONLY within the function.
It is accessible from the point at which it is defined until the end of the function
and exists for as long as the function is executing (Source).
Which means its value cannot be changed or even accessed from outside the function.


1.def print_number(): #local scope
    first_num = 1
    # Print statement 1
    print("The first number defined is: ", first_num)

print_number()
# Print statement 2
print("The first number defined is: ", first_num)


2.a=0
def func():
    print(a)
    a=1
    print(a)
func()

3.def func(a=0):
    a+=1
    print(a)
 func()

4.
def square(base):
    result = base ** 2
    print(f'The square of {base} is: {result}')
square(10)

5.
def cube(base):
     result = base ** 3
     print(f'The cube of {base} is: {result}')
cube(30)


2.Enclosing Scope:

1.def outer():#enclosing-scope
    first_num = 1
    def inner():
        second_num = 2
        # Print statement 1 - Scope: Inner
        print("first_num from outer: ", first_num)
        # Print statement 2 - Scope: Inner
        print("second_num from inner: ", second_num)
    inner()
    # Print statement 3 - Scope: Outer
    print("second_num from inner: ", second_num)

outer()


2.def outer():
    first_num = 1
    def inner():
        first_num = 0
        second_num = 1
        print("inner - second_num is: ", second_num)
    inner()
    print("outer - first_num is: ", first_num)

outer()

3. def red():
                a=1
                def blue():
                                b=2
                                print(a)
                                print(b)
                blue()
                print(a)
  red()
4.
def power_factory(exp):
    def power(base):
         return base ** exp
    return power
square = power_factory(2)
square(10)
100
cube = power_factory(3)
cube(10)
1000
cube(5)
125
square(15)
225

5.
def mean():
     sample = []
     def _mean(number):
         sample.append(number)
         return sum(sample) / len(sample)
     return _mean

current_mean = mean()
current_mean(10)
10.0
current_mean(15)
12.5
current_mean(12)
12.333333333333334
current_mean(11)
12.0
current_mean(13)
12.2

6.



3. global scope:

Whenever a variable is defined outside any function, it becomes a global variable,
and its scope is anywhere within the program. Which means it can be used by any function.


1.greeting = "Hello" #global scope

def greeting_world():
    world = "World"
    print(greeting, world)

def greeting_name(name):
    print(greeting, name)

greeting_world()
greeting_name("Samuel")

2.greeting = "Hello" #global keyword

def change_greeting(new_greeting):
    greeting = new_greeting

def greeting_world():
    world = "World"
    print(greeting, world)

change_greeting("Hi")
greeting_world()

# This area is the global or module scope
number = 100
def outer_func():
    # This block is the local scope of outer_func()
     # It's also the enclosing scope of inner_func()
    def inner_func():
         # This block is the local scope of inner_func()
        print(number)

     inner_func()

outer_func()
100

#global keyword:

3.greeting = "Hello"

    global greeting
    greeting = new_greeting

def greeting_world():
    world = "World"
    print(greeting, world)

change_greeting("Hi")
greeting_world()


4.a=1
def counter():
                a=2
                print(a)
counter()


5.a=1
def counter():
                global a
                a=2
                print(a)
counter()

6.
var = 100
def func():
     return var  # You can access var from inside func()

func()
100
var  # Remains unchanged
100

counter = 0  # A global name
 def update_counter():
     global counter  # Declare counter as global
     counter = counter + 1  # Successfully update the counter

update_counter()
counter
1
update_counter()
counter
2
update_counter()
counter
3

8. global_counter = 0  # A global name
def update_counter(counter):
     return counter + 1  # Rely on a local name

global_counter = update_counter(global_counter)
global_counter
1
global_counter = update_counter(global_counter)
global_counter
2
global_counter = update_counter(global_counter)
global_counter
3

9.def calculate(*args):
    sum=0
    for arg in args:
        sum = sum +arg
    print("The sum is",sum)
sum=0
calculate(10,20,30) #60 will be printed as the sum
print("Value of sum outside the function:",sum) # 0 will be printed  Output:


4.built-in scope:

All the special reserved keywords fall under this scope.
We can call the keywords anywhere within our program without having to define them before use.

Keywords are simply special reserved words. They are kept for specific purposes
and cannot be used for any other purpose in the program.

1.
import builtins  # Import builtins as a regular module
dir(builtins)
['ArithmeticError', 'AssertionError',..., 'tuple', 'type', 'vars', 'zip']
builtins.sum([1, 2, 3, 4, 5])
15
 builtins.max([1, 5, 8, 7, 3])
8
builtins.sorted([1, 5, 8, 7, 3])
[1, 3, 5, 7, 8]
builtins.pow(10, 2)
100

2.
import builtins
builtins.abs(-15)
15


#LEGB Rule:

LEGB (Local -> Enclosing -> Global -> Built-in) is the logic followed by a Python
interpreter when it is executing your program.


#Nonlocal Keyword:

This is another handy keyword that allows us to work more flexibly and tidily with variable scopes.
The nonlocal keyword is useful in nested functions.
It causes the variable to refer to the previously bound variable in the closest enclosing scope.

1.def outer():
    first_num = 1
    def inner():
        nonlocal first_num
        first_num = 0
        second_num = 1
        print("inner - second_num is: ", second_num)
    inner()
    print("outer - first_num is: ", first_num)

outer()

2.def red():
                a=1
                def blue():
                                a=2
                                b=2
                                print(a)
                                print(b)
                blue()
                print(a)
red()


3.  def red():
                a=1
                def blue():
                                nonlocal a
                                a=2
                                b=2
                                print(a)
                                print(b)
                blue()
                print(a)
red()

4.
def func():
    var = 100  # A nonlocal variable
     def nested():
         nonlocal var  # Declare var as nonlocal
         var += 100

     nested()
     print(var)

func()
200

5.

def mean():
     total = 0
     length = 0
     def _mean(number):
        nonlocal total, length
        total += number
        length += 1
        return total / length
     return _mean

current_mean = mean()
current_mean(10)
10.0
current_mean(15)
12.5
current_mean(12)
12.333333333333334
current_mean(11)
12.0
current_mean(13)
12.2


# copy:?
1. normal copy
2. deep copy
3. shallow copy


# normal copy
1.mylist= [2,3,7]
copylist= mylist
mydic= {'A':1, 'B':2}

copydic= mydic
myset= {4,'s', 8}
copyset= myset

print(mylist)
print("Id of mylist:", id(mylist))
print(copylist)
print ("Id of copylist:", id(copylist))

2.mylist= [2,3,7]

copylist= mylist
copylist.append('r')

print(mylist)
print(copylist)

3. #method to print the list
thisistech= [1, 2, 3],['#',"*","-"]
newtech=[0,9,8,7]
#the functions returns as it is
print('Old List:', thisistech)
#shallow copy

1.import copy

mylist= [2,3,7]
copylist= copy.copy(mylist)

print("Values before making changes:")
print(mylist)
print(copylist)

copylist[1] = 5

print("Values after making chnages:")
print(mylist)
print(copylist)

#output:

Values before making changes:
[2, 3, 7]
[2, 3, 7]
Values after making chnages:
[2, 3, 7]
[2, 5, 7]

#deep copy:

1.import copy

mylist= [2,3,7]
copylist= copy.deepcopy(mylist)

print("Values before making changes:")
print(mylist)
print(copylist)

copylist.append('s')

print("Values after making chnages:")
print(mylist)
print(copylist)

output:
Values before making changes:
[2, 3, 7]
[2, 3, 7]
Values after making chnages:
[2, 3, 7]
[2, 3, 7, 's']

2.
import copy
list1=[1,0,[7,9],6]
list2=copy.deepcopy(list1) #Making a deep copy
print( list1)

3. addition of nested loop

l=int(input("enter number"))
old__list = [[1, 1, 1], [2, 2, 2], [5, 5, 5]]

print("Old list:", old__list)

#Output:

enter number 67
Old list: [[1, 1, 1], [2, 2, 2], [5, 5, 5]]

#shallow copy:

import copy
list=1,0,[7,9],6
list_2=copy.copy(list) #Making a shallow copy
print(list)


#Passing Mutable Object (String)
#defining the function
def change_string (str):
    str = str + " Hows you "
    print("printing the string inside function :",str)

string1 = "Hi I am there"

#calling the function
change_string(string1)

print("printing the string outside function :",string1)

#Output:

printing the string inside function : Hi I am there Hows you
printing the string outside function : Hi I am there

"""


