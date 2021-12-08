"""

#The Anonymous Functions:

1.These functions are called anonymous because they are not declared in the standard manner
by using the def keyword. You can use the lambda keyword to create small anonymous functions.

2.Lambda forms can take any number of arguments but return just one value in the form of an expression.
They cannot contain commands or multiple expressions.

3.An anonymous function cannot be a direct call to print because lambda requires an expression

4.Lambda functions have their own local namespace and cannot access variables
other than those in their parameter list and those in the global namespace.


#Syntax:

lambda [arg1 [,arg2,.....argn]]:expression



#programs:

1.write a simple program byusing lambda function?

string ='GeeksforGeeks'

# lambda returns a function object
print(lambda string : string)

x ="GeeksforGeeks"

# lambda gets pass to print
(lambda x : print(x))(x)


2. write a program to print cube of number?

# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
    return y*y*y

lambda_cube = lambda y: y*y*y

# using the normally
# defined function
print(cube(5))

# using the lambda function
print(lambda_cube(5))


3. write a python program to get the values within given range by using lambda
function within list comprehension?

tables = [lambda x=x: x*10 for x in range(1, 11)]

for table in tables:
    print(table())


4.write a python program to find the greatest of two numbers?

# Example of lambda function using if-else
Max = lambda a, b : x if(a > b) else b
print(Max(1, 2))


5.write a python program to print the age off after 18 years?

ages = [13, 90, 17, 59, 21, 60, 5]

adults = list(filter(lambda age: age>18, ages))

print(adults)

6.write a python program to get the values doubled present in the list?

# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x*2, li))
print(final_list)

7. write a  lambda function to double the input values?

double = lambda x: x * 2
print(double(5))

8.write a python program to filterout only even values present in the list?

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)
----------------------------------------------------------------------------------------------------------------
# a is an argument and a+10 is an expression which got evaluated and returned.
x = lambda a:a+10
# Here we are printing the function object
print(x)
print("sum = ",x(20))
--------------------------------------------------------------------------------------------------------------

#program to filter out the tuple which contains odd numbers
lst = (10,22,37,41,100,123,29)
oddlist = tuple(filter(lambda x:(x%3 == 0),lst))
# the tuple contains all the items of the tuple for which the lambda function evaluates to true
print(oddlist)
-------------------------------------------------------------------------------------------------------------------------

#program to filter out the list which contains odd numbers
lst = (10,20,30,40,50,60)
square_list = list(map(lambda x:x**2,lst)) # the tuple contains all the items of the list for which the lambda function evaluates to true
print(square_tuple)

---------------------------------------------------------------------------------------------------------
#filter:
1.The filter() function extracts elements from an iterable (list, tuple etc.) ?


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# returns True if number is even
def check_even(number):
    if number % 2 == 0:
          return True

    return False

# Extract elements from the numbers list for which check_even() returns True
even_numbers_iterator = filter(check_even, numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)

# Output: [2, 4, 6, 8, 10]

2.wap to get the vowes from collection/group of characters?


letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# a function that returns True if letter is vowel
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False

filtered_vowels = filter(filter_vowels, letters)

# converting to tuple
vowels = tuple(filtered_vowels)
print(vowels)

3.write a program to get the even numbers by using the filter within lambda function?

numbers = [1, 2, 3, 4, 5, 6, 7]

# the lambda function returns True for even numbers
even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)


4.write a filter program by using the none ?

# random list
random_list = [1, 'a', 0, False, True, '0']

filtered_iterator = filter(None, random_list)

#converting to list
filtered_list = list(filtered_iterator)

print(filtered_list)

5.write a program to return the values higher than 5 present in the tuple?

# Python filter() function example
def filterdata(x):
    if x>5:
        return x
# Calling function
result = filter(filterdata,(1,2,6))
# Displaying result
print(list(result))

6.wap to return non zero and true values present in the collection?


# Python filter() function example
# Calling function
result = filter(None,(1,0,6)) # returns all non-zero values
result2 = filter(None,(1,0,False,True)) # returns all non-zero and True values
# Displaying result
result = list(result)
result2 = list(result2)
print(result)
print(result2)

7.write a program to the values which is multiplied by 3?

# Python filter() function example
def mulof3(val):
    if val%3==0:
        return val
# Calling function
result = filter(mulof3,(1,3,5,6,8,9,12,14))
# Displaying result
result = list(result)
print(result) # multiples of 3

--------------------------------------------------------------------------------------------------------------
#map:

1.write a program to square of each value present in the collections?


numbers = [2, 4, 6, 8, 10]

# returns square of a number
def square(number):
  return number * number

# apply square() function to each item of the numbers list
squared_numbers_iterator = map(square, numbers)

# converting to list
squared_numbers = list(squared_numbers_iterator)
print(squared_numbers)

# Output: [4, 16, 36, 64, 100]


#def calculateSquare(n):
    return n*n


numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)

2.write a program to get squares of numbers by using lambda function with map?
(how to use lambdafunction?)

numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)

3.write a python program to Passing Multiple Iterators to map() Using Lambda?

num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))

4.write a program to round the each value present in the collection?

my_list = [2.6743,3.63526,4.2325,5.9687967,6.3265,7.6988,8.232,9.6907]
updated_list = map(round, my_list)
print(updated_list)
print(list(updated_list))

5.write a program to get string as an iterator with uppercase characters by using map function?

def myMapFunc(s):
    return s.upper()
my_str = "welcome to mcs in bangalore!"
updated_list = map(myMapFunc, my_str)
print(updated_list)
for i in updated_list:
    print(i, end="")

6.write a program to multiply the numbers present in the list with given number by using map function?

def myMapFunc(n):
    return n*10

my_list = [2,3,4,5,6,7,8,9]

updated_list = map(myMapFunc, my_list)
print(updated_list)
print(list(updated_list))


7. write a program to print the words as a upper present in the tuple of strings by using map function?

def myMapFunc(n):
    return n.upper()

my_tuple = ('php','java','python','c++','c')

updated_list = map(myMapFunc, my_tuple)
print(updated_list)
print(list(updated_list)


8.write a python program to iterate the values  present in the dictionary with multiplication of 10  by using the map function?

def myMapFunc(n):
    return n*10
my_dict = {2,3,4,5,6,7,8,9}
finalitems = map(myMapFunc, my_dict)
print(finalitems)
print(list(finalitems))


def myMapFunc(n):
    return n*10
my_set = {2,3,4,5,6,7,8,9}
finalitems = map(myMapFunc, my_set)
print(finalitems)
print(list(finalitems))

9.using the lambda function inside the map to multiply the values with given values pesent in the collection?

my_list = [2,3,4,5,6,7,8,9]
updated_list = map(lambda x: x * 10, my_list)
print(updated_list)
print(list(updated_list))

10.write a program to pass the two list iterators to map function?
def myMapFunc(list1, list2):
    return list1+list2

my_list1 = [2,3,4,5,6,7,8,9]
my_list2 = [4,8,12,16,20,24,28]

updated_list = map(myMapFunc, my_list1,my_list2)
print(updated_list)
print(list(updated_list))


11.write a program to pass the one list and one tuple iterators to map function?

def myMapFunc(list1, tuple1):
    return list1+"_"+tuple1

my_list = ['a','b', 'b', 'd', 'e']
my_tuple = ('PHP','Java','Python','C++','C')

updated_list = map(myMapFunc, my_list,my_tuple)
print(updated_list)
print(list(updated_list))

--------------------------------------------------------------------------------------------------------------








"""