'''
#List Comprehension
List comprehension offers a shorter syntax when you want to create
a new list based on the values of an existing list.

#The Syntax:

newlist = [expression for item in iterable if condition == True]


#Advantages of List Comprehension:

More time-efficient and space-efficient than loops.
Require fewer lines of code.
Transforms iterative statement into a formula.
'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Using list comprehension to iterate through loop
List = [character for character in 'Geeks 4 Geeks!']

# Displaying list
print(List)

# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]

print(matrix)

numbers= [i*10 for i in range(1,6)]

print(numbers)

# Getting square of even numbers from 1 to 10
squares = [n**2 for n in range(1, 11) if n%2==0]

# Display square of even numbers
print(squares)

# Reverse each string in tuple
List = [string[::-1] for string in ('Geeks', 'for', 'Geeks')]

# Display list
print(List)

h_letters = [ letter for letter in 'human' ]
print( h_letters)

number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common_num = [a for a in list_a for b in list_b if a == b]

print(common_num)

list_a = [1, 2, 3]
list_b = [2, 7]

different_num = [(a, b) for a in list_a for b in list_b if a != b]

print(different_num)

list_a = [1, 2, 3]

square_cube_list = [ [a**2, a**3] for a in list_a]

print(square_cube_list)


