"""

1.Write a Python function to find the Max of three numbers.

def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))

2.Write a Python function to sum all the numbers in a list.?

Sample List : (8, 2, 3, 0, 7)
Expected Output : 20

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))

3. Write a Python function to multiply all the numbers in a list. ?

Sample List : (8, 2, 3, -1, 7)
Expected Output : -336

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply((8, 2, 3, -1, 7)))


4. Write a Python program to reverse a string. ?

Sample String : "1234abcd"
Expected Output : "dcba4321"


def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))

5. Write a Python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))


6. Write a Python function to check whether a number falls in a given range?

def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)


7. Write a Python function that accepts a string
and calculate the number of upper case letters and lower case letters?


Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12



def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')

8. Write a Python function that takes a list and returns a new list with unique elements of the first list. Go to the editor

Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]


def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5]))

9. Write a Python function that takes a number as a parameter and check
the number is prime or not.?

Note : A prime number (or a prime) is a natural number greater than 1
and that has no positive divisors other than 1 and itself.

def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
print(test_prime(9))



#type 2:
from math import sqrt
def is_prime(num):
  if num <= 1 or (num % 2 == 0 and num > 2):
    return False
  return all(num % i for i in range(3, int(sqrt(num)) + 1, 2))
print(is_prime(11))
print(is_prime(13))
print(is_prime(16))
print(is_prime(17))
print(is_prime(97))

10. Write a Python program to print the even numbers from a given list. ?

Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]


def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

11. Write a Python function to check whether a number is perfect or not?

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))

12. Write a Python function that checks whether a passed string is palindrome or not?

def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1

	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('aza'))


14.Write a Python function to check whether a string is a pangram or not?

import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print ( ispangram('The quick brown fox jumps over the lazy dog'))


15. Write a Python program that accepts a hyphen-separated sequence of words
as input and prints the words in a hyphen-separated sequence after sorting them
alphabetically. ?

Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow

items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))

16. Write a Python function to create and print a list where the values are
square of numbers between 1 and 30 (both included).?


def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l)

printValues()

17. Write a Python program to execute a string containing Python code.?

mycode = 'print("hello world")'
code = " "
def mutiply(x,y):
    return x*y

print('Multiply of 2 and 3 is: ',mutiply(2,3))
exec(mycode)
exec(code)

18.Write a Python program to access a function inside a function.?

def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a + b

    return add


func = test(4)
print(func(4))

19.Write a Python program to detect the number of local variables declared in a function.?

Sample Output:
3

def abc():
    x = 1
    y = 2
    str1= "w3resource"
    print("Python Exercises")

print(abc.__code__.co_nlocals)

20.Python Program to Find LCM?


# defining a function to calculate LCM
def calculate_lcm(x, y):
    # selecting the greater number
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

# taking input from users
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# printing the result for the users
print("The L.C.M. of", num1,"and", num2,"is", calculate_lcm(num1, num2))


21.Python Program to Find HCF?


def calculate_hcf(x, y):
    # selecting the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

# taking input from users
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# printing the result for the users
print("The H.C.F. of", num1,"and", num2,"is", calculate_hcf(num1, num2))

22.Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
# First, we will define the function to convert decimal to binary
def decimal_into_binary(decimal_1):
    decimal = int(decimal_1)

    # then, print the equivalent decimal
    print ("The given decimal number", decimal, "in Binary number is: ", bin(decimal))
# we will define the function to convert decimal to octal
def decimal_into_octal(decimal_1):
    decimal = int(decimal_1)

    # Then, print the equivalent decimal
    print ("The given decimal number", decimal, "in Octal number is: ", oct(decimal))
# we will define the function to convert decimal to hexadecimal
def decimal_into_hexadecimal(decimal_1):
    decimal = int(decimal_1)

    # Then, print the equivalent decimal
    print ("The given decimal number", decimal, " in Hexadecimal number is: ", hex(decimal))

# Driver program
decimal_1 = int (input (" Enter the Decimal Number: "))
decimal_into_binary(decimal_1)
decimal_into_octal(decimal_1)
decimal_into_hexadecimal(decimal_1)


23.Python Program To Find ASCII value of a character?
K = input("Please enter a character: ")

print ("The ASCII value of '" + K + "' is ", ord(K))

24.Python Program to Make a Simple Calculator?

def add(P, Q):
   # This function is used for adding two numbers
   return P + Q
def subtract(P, Q):
   # This function is used for subtracting two numbers
   return P - Q
def multiply(P, Q):
   # This function is used for multiplying two numbers
   return P * Q
def divide(P, Q):
   # This function is used for dividing two numbers
   return P / Q
# Now we will take inputs from the user
print ("Please select the operation.")
print ("a. Add")
print ("b. Subtract")
print ("c. Multiply")
print ("d. Divide")

choice = input("Please enter choice (a/ b/ c/ d): ")

num_1 = int (input ("Please enter the first number: "))
num_2 = int (input ("Please enter the second number: "))

if choice == 'a':
   print (num_1, " + ", num_2, " = ", add(num_1, num_2))

elif choice == 'b':
   print (num_1, " - ", num_2, " = ", subtract(num_1, num_2))

elif choice == 'c':
   print (num1, " * ", num2, " = ", multiply(num1, num2))
elif choice == 'd':
   print (num_1, " / ", num_2, " = ", divide(num_1, num_2))
else:
   print ("This is an invalid input")


25.Python Function to Display Calendar?

# First import the calendar module
import calendar
# ask of month and year
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
# display the calendar
print(calendar.month(yy,mm))


26.11. Write a python program using function to find the largest element in a list.?

def largest(L,n) :
    max = L[0]
    for i in range(1, n) :
        if L[i] > max :
            max =L[i]
    return max
M = [10, 24, 45, 90, 98]
n = len(M)
max= largest(M, n)
print ("Largest in the given List is", max)

27.write a python program to access the multiple functions?

def hello():
    print (“Hello there!”)
def goodbye():
    print (“See ya!”)

28. write a python program to calling the function inside the function?

def main():
    print (“I have a message for you.”)
    message()
    print (“Goodbye!”)
def message():
    print (“The password is ‘foo’”)
main()


29. write a python program to create a function by using local variables?

def newjersey():
    numbugs = 1000
    print (“NJ has”, numbugs, “bugs”)
def newyork():
    numbugs = 2000
    print (“NY has”, numbugs, “bugs”)
newjersey()
newyork()

30.write a python program to pass the arguments to a function?

def square(num):
    print (num**2) # num assumes the value of the
                   # argument that is passed to
                   # the function (5)
square(5)

31.write a python program to passing the multiple  arguments to a function?

def average(num1, num2, num3):
    sum = num1+num2+num3
    avg = sum / 3
    print (avg)
average(100,90,92)

32.write a python function program by using global variables?

name = 'Obama'
def showname():
 print ("Function:", name)
print ("Main program:", name)
showname()


#and
name = "Obama"
def showname():
    global name
    print ("Function 1:", name)
    name = "John"
    print ("Function 2:", name)
print ("Main program 1:", name)
showname()
print ("Main program 2:", name)


33.write a python function program to return a value?
def myfunction(arg1, arg2):
    statement
    statement
    …
    statement
    return expression
# call the function
returnvalue = myfunction(10, 50)

34. write a python function program add ages of two members/persons by using  iop?
# function: add_ages
# input: age1 (integer), age2 (integer)
# processing: combines the two integers
# output: returns the combined value
def add_ages(age1, age2):
 sum = age1+age2
 return sum


35.write a python program to return multiple values by using function?
def testfunction():
     x = 5
     y = 10
     return x, y
p, q = testfunction()









"""
