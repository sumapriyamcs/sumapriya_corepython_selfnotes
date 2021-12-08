"""
#Function Calling:

1.In Python, after the function is created, we can call it from another function.
2.A function must be defined before the function call; otherwise, the Python interpreter gives an error.
3.To call the function, use the function name followed by the parentheses.

#EX:
#function definition
def hello_world():
    print("hello world")
# function calling
hello_world()


#Requirement :  check Enter no is +ve or -ve
#State
num=int(input("Enter a no"))
# Behavior

def check(num): #Function Definition
# Function body
 if num>0:
  print(num,"is +ve no")
 else:
  print(num,"is -ve no")

check(num)     # calling function
------------------------------------------
#Requirement :  print table
# Behavior
def multi(n): #Function Definition
 print(n)
 i=1
 while i<11:
  result=i*n
  i += 1
  print("Table of",n, "is =",result)
#State
num = int(input("Enter a no"))
multi(num)     # calling function

-------------------------------------------------

#Requirement :  print table
# Behavior
def multi(n): #Function Definition
 print("Table of ", n ,"is")
 i=1
 while i<11:
  result=i*n
  i += 1
  print(result)
#State
num = int(input("Enter a no"))
multi(num)     # calling function
-------------------------------------------------
#Requirement :  Concatinate name enter name
# Behavior
def multi(fn,ln): #Function Definition
 full_name = fn +" "+ ln
 print("Full Name of student",full_name)
#State
fname= input("Enter first name of Student")
lname= input("Enter last name of Student")
multi(fname,lname)     # calling function

-------------------------------------------------
#Requirement :  Concatinate enter name and marks
# Behavior
def multi(fn,ln,m): #Function Definition
 details = fn +" "+ ln + "    Marks =", m
 print("Full Name of student",details)

#State
fname= input("Enter first name of Student")
lname= input("Enter last name of Student")
marks = int(input("Enter marks of student"))
multi(fname,lname,marks)     # calling function

"""