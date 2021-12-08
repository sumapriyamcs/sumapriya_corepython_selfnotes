'''
Requirement :
1. CRUD   Create,Retrieve,Update,Delete
2. Datatype
3. State, Behavior

Numbers : int float long complex  - Immutable
Boolean : bool   - Immutable
String  : " " ' ' -  Immutable, Sequence, char based
List*    : []      -  Mutable, Sequence, Insertion order, home/hetero, duplicates allowed
Tuple   : ()      -  Immutable, Sequence, Insertion order, home/hetero, duplicates allowed
Dict*    : {}      -  Mutable, key-value pair, keys Immutable&Unique
Set     : {}      -  Mutable, inside element Immutable& Unique , no order follows

Requirement :
1. Categorize req, input data parts
2. C R U D
3. Datatype
4. State, Behavior

Requirement : Find student grade based on given marks for each student

Step 1:  Input data   : Given marks for each student
         Req(Question): Find Student grade
Step 2:  RETRIEVAL    : We are getting student grade and displaying in console
Step 3:  Datatype     : if only student marks were given : [100,20,45,67,89,43,23]
                        If rollno, marks were given      :[[12345,100],[132111,20],[3243232,45]....]
                                                         :{12345:100,
                                                           132111:20,
                                                           3243232:45
                                                           }
                                                           {12345:[100,20,45,67,89,43,23],
                                                           132111:[100,20,45,67,89,43,23],
                                                           3243232:[100,20,45,67,89,43,23]
                                                           }


                        If complete info given            :{12345:['MadhuN','10th',90,'ATP'],
                                                            132111:['KiranG','10th',85,'ATP'],
                                                            ........
                                                            }
                        Grade: String 'A' - 75 to 100,
                                      'B' - 60 to 75,
                                      'C' - 50 to 60,
                                      'D' - 35 to 50
                                     'Fail'- <35

Step 4:  State :
         Behavior:
'''
# State  --> Variables
student_info = {12345: ['MadhuN', '10th', 90, 'ATP'],
                43232: ['KiranG', '10th', 85, 'CHR'],
                42422: ['Prakash', '10th', 34, 'KRN']
                }
print("-----------------------")
# Behavior --> Functions
for sid, sinfo in student_info.items():
    marks = sinfo[2]
    if marks >= 70 and marks <= 100:
        print(sid, " grade is : ", " A")
    elif marks >= 60 and marks < 70:
        print(sid, " grade is : ", " B")
    elif marks >= 50 and marks < 60:
        print(sid, " grade is : ", " C")
    elif marks >= 35 and marks < 50:
        print(sid, " grade is : ", " D")
    else:
        print(sid, " grade is : ", " Fail")

'''
Requirement :  Find length of String
1. Categorize req,input data parts
2. C R U D  
3. Datatype   
4. State, Behavior

Requirement : Find length of given string

Step 1:  Input data   : given string
         Req(Question): Find length
Step 2:  Retrieval    : We are getting length of string 
Step 3:  Datatype     : String : 'Hello World'
Step 4:  State :
         Behavior:
'''
print("-----------------------")
# State  --> Variables
msg = 'Hello World'
# Behavior --> Functions
length = 0
for each in msg:
    length += 1
print("Length of string : ", length)


# Different ways to write program
# 1. Builtin function
l1 = [1,2,3,4]
print("Lenght of list : ",len(l1))

# 2. Normal business logic using while,if,else,for
l1 = [1,2,3,4]
le = 0
for each in l1:
    le += 1
print("Length of list : ",le)

# 3. Using functions
l1 = [1,2,3,4]
def find_length(in_list):
    le = 0
    for each in l1:
        le += 1
    return le
print("Length of list : ",find_length(l1))


# 4. Using OOPs

class FindLength:
    l1 = [1, 2, 3, 4]

    def find_length(cls):
        le = 0
        for each in cls.l1:
            le += 1
        return le

print("Length of list : ", FindLength.find_length())


# 5. Take 2nd,3rd or 4th step and include exception handling
l1 = [1,2,3,4]
def find_length(in_list):
    try:
        le = 0
        for each in l1:
            le += 1
        return le
    except:
        pass
print("Length of list : ",find_length(l1))


# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
#difference between syntax errors and exceptions:

# initialize the amount variable
amount = 10000

# check that You are eligible to
# purchase Dsa Self Paced or not
if(amount > 2999):
    print("You are eligible to purchase Dsa Self Paced")

# initialize the amount variable
marks = 10000

# perform division with 0
a = marks / 0
print(a)


#Try and Except Statement – Catching Exceptions:?

# Python program to handle simple runtime error
#Python 3

a = [1, 2, 3]
try:
	print ("Second element = %d" %(a[1]))

	# Throws error since there are only 3 elements in array
	print ("Fourth element = %d" %(a[3]))

except:
	print ("An error occurred")

#Catching specific exception in Python:?
# Program to handle multiple errors with one
# except statement
# Python 3

def fun(a):
    if a < 4:
        # throws ZeroDivisionError for a = 3
        b = a / (a - 3)

    # throws NameError if a >= 4
    print("Value of b = ", b)


try:
    fun(3)
    fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")

#Try with else clause:?

# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#finally keyword:?
# Python program to demonstrate finally

# No exception Exception raised in try block
try:
	k = 5//0 # raises divide by zero exception.
	print(k)

# handles zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')

#raising exception
# Program to depict Raising Exception

try:
	raise NameError("Hi there") # Raise Error
except NameError:
	print ("An exception")
	raise # To determine whether the exception was raised or not

#zero division exception:?
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = a / b
print("a/b = %d" % c)

# other code:
print("Hi I am other part of the program")


#try-except blocks:?
try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a/b
except:
    print("Can't divide with zero")

#try-except-else:?
    try:
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        c = a / b
        print("a/b = %d" % c)
        # Using Exception with except statement. If we print(Exception) it will return exception class
    except Exception:
        print("can't divide by zero")
        print(Exception)
    else:
        print("Hi I am else block")

#except statement with no exception:?
    try:
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        c = a / b;
        print("a/b = %d" % c)
    except:
        print("can't divide by zero")
    else:
        print("Hi I am else block")

#The except statement using with exception variable:?


try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a/b
    print("a/b = %d"%c)
    # Using exception object with the except statement
except Exception as e:
    print("can't divide by zero")
    print(e)
else:
    print("Hi I am else block")

#multiple exceptions
try:
    a=10/0;
except(ArithmeticError, IOError):
    print("Arithmetic Exception")
else:
    print("Successfully Done")

#try-finally:?
try:
    fileptr = open("file2.txt","r")
    try:
        fileptr.write("Hi I am good")
    finally:
        fileptr.close()
        print("file closed")
except:
    print("Error")

#raise exception:?
try:
    age = int(input("Enter the age:"))
    if(age<18):
        raise ValueError
    else:
        print("the age is valid")
except ValueError:
    print("The age is not valid")

#example 2:?

try:
     num = int(input("Enter a positive integer: "))
     if(num <= 0):
# we can pass the message in the raise statement
         raise ValueError("That is  a negative number!")
except ValueError as e:
     print(e)

#example 3:?

try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    if b is 0:
        raise ArithmeticError
    else:
        print("a/b = ",a/b)
except ArithmeticError:
    print("The value of b can't be 0")

#custom exception:?
class ErrorInCode(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


try:
    raise ErrorInCode(2000)
except ErrorInCode as ae:
    print("Received error:", ae.data)

