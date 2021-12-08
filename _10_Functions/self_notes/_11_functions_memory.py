"""
# introduction:
1.Memory management is very important for software developers to work efficiently
with any programming language. As we know, Python is a famous and widely used programming language.

2.It is used almost in every technical domain.
In contrast to a programming language, memory management is related to writing memory-efficient code.

3.memory is managed by the Python manager which determines where to put the application data in the memory.
The procedure of providing memory to objects is called allocation.

4.Memory management in Python involves a private heap containing all Python objects and data structures.
The management of this private heap is ensured internally by the Python memory manager.

#Python Memory Allocation:

Memory allocation is an essential part of the memory management for a developer. This process basically allots free space in the computer's virtual memory, and there are two types of virtual memory works while executing programs.

1.Static Memory Allocation
2.Dynamic Memory Allocation
3.Heap Memory Allocation

#programs:

1. def get_data():   # Function invocation
    print("Welcome to my method")
    return "Hello World"

res = get_data()   # Function calling
print("Result is : ", res)

print("Function details ", get_data)  # Get function body address

2.
def greet(name):

   # This function greets to
    the person passed in as
    a parameter

    print("Hello, " + name + ". Good morning!")
greet('Paul')


3.def absolute_value(num):
    #This function returns the absolute
    value of the entered number

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))

print(absolute_value(-4))

4.def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)

5. def hello():
  name = str(input("Enter your name: "))
  if name:
    print ("Hello " + str(name))
  else:
    print("Hello World")
  return

hello()

6.def plus(a,b):
  return a + b

a=10
b=20
res=plus(10,20)
print(res)

7.
# Define `plus()`
def plus(a,b):
  sum = a + b
  return (sum, a)

# Call `plus()` and unpack variables
sum, a = plus(3,4)

# Print `sum()`
print(sum)

8.def plus(*args):
  return sum(args)

# Calculate the sum
res=plus(1,4,5)
print(res)

9.def plus(a,b):
  return a + b

# Call `plus()` function with keyword arguments
res=plus(b=2, a=1)
print(res)

10.# Define `plus()` function
def plus(a,b):
  return a + b

# Call `plus()` function with parameters
res=plus(2,3)
print(res)
# Call `plus()` function with keyword arguments
res1=plus(a=1, b=2)
print(res1)


11.def plus(*args):
  total = 0
  for i in args:
    total += i
  return total

# Calculate the sum
res=plus(20,30,40,50)
print(res)

12.sum = lambda x, y: x + y;

# Call the `sum()` anonymous function
sum(4,5)

# "Translate" to a UDF
def sum(x, y):
  return x+y
res=sum(4,5)
print(res)

13.from functools import reduce

my_list = [1,2,3,4,5,6,7,8,9,10]

# Use lambda function with `filter()`
filtered_list = list(filter(lambda x: (x*2 > 10), my_list))

# Use lambda function with `map()`
mapped_list = list(map(lambda x: x*2, my_list))

# Use lambda function with `reduce()`
reduced_list = reduce(lambda x, y: x+y, my_list)

print(filtered_list)
print(mapped_list)
print(reduced_list)

14.Create a function with variable length of arguments?

def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)

15.Return multiple values from a function?

def calculation(a, b):
    addition = a + b
    subtraction = a - b
    # return multiple values separated by comma
    return addition, subtraction

# get result in tuple format
res = calculation(40, 10)
print(res)

def calculation(a, b):
    return a + b, a - b

# get result in tuple format
# unpack tuple
add, sub = calculation(40, 10)
print(add, sub)

16.Create a function with default argument?

# function with default argument
def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")

17. Create an inner function to calculate the addition in the following way?

# outer function
def outer_fun(a, b):
    square = a ** 2

    # inner function
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5

result = outer_fun(5, 10)
print(result)

18.Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)

19. Assign a different name to function and call it through the new name?

def display_student(name, age):
    print(name, age)

# call using original name
display_student("Emma", 26)

# assign new name
showStudent = display_student
# call using new name
showStudent("Emma", 26)

20.Generate a Python list of all the even numbers between 4 to 30?

print(list(range(4, 30, 2)))

21.Find the largest item from a given list?


x = [4, 6, 8, 24, 12, 2]
print(max(x))

#passbyvalue and pass by reference:

Pass by reference – It is used in some programming languages, where values
to the argument of the function are passed by reference which means that the address of the variable
is passed and then the operation is done on the value stored at these addresses.

Pass by value – It means that the value is directly passed as the value to
the argument of the function. Here, the operation is done on the value and then the value
is stored at the address. Pass by value is used for a copy of the variable.

#pass by reference
example 1:

student = {'Jim': 12, 'Anna': 14, 'Preet': 10}
def test(student):
    new = {'Sam':20, 'Steve':21}
    student.update(new)
    print("Inside the function", student)
    return
test(student)
print("Outside the function:", student)


def marks(list):
    list.append([11, 12, 13, 14, 15])
    print("Value inside the function: ", list)
    return
list = [10,20]
marks(list)
print("Value outside the function: ", list)

teacher = {'Peter':101, 'John':102, 'Suzain':103}
def test(teacher):
   new = {'kat':104, 'Satya':105}
   teacher.update(new)
   print("Inside the function",teacher)
   return
test(teacher)
print("Outside the function:",teacher)


#defining the function
def change_list(list1):
    list1.append(20)
    list1.append(30)
    print("list inside function = ",list1)

#defining the list
list1 = [10,30,40,50]

#calling the function
change_list(list1)
print("list outside function = ",list1)

#pass by value:
example 2:

student = {'Jim': 12, 'Anna': 14, 'Preet': 10}
def test(student):
    student = {'Sam':20, 'Steve':21}
    print("Inside the function", student)
    return
test(student)
print("Outside the function:", student)


my_string = "Python"
def test(my_string):
    my_string = "PythonGuides"
    print("Inside the function:",my_string)
test(my_string)
print("Outside the function:",my_string)




"""





