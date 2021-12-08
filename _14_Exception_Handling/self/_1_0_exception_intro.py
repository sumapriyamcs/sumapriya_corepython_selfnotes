'''
Traceback (most recent call last):
  File "C:/Users/madhu/git_projects/Batch_13/B13_PythonTraining/_13_Exception_handling/_1_Introduction.py", line 20, in <module>
    x = int(input("Enter numerator value :"))
ValueError: invalid literal for int() with base 10: 'dfgads'
'''
'''
Requirement: As an end user i will give 2 values,
             display division result for the same.

'''
# Before Exception handling
print("----Before Exception handling----")

x = int(input("Enter numerator value :"))
y = int(input("Enter denominator value :"))
print("Division :", x / y)  # 0/any value = 0   any value/0 = infinity
print("Remaining Code")
print("---------------------------------")

'''
blocks :if else elif for while  function class

blocks to handle the exception    
try*      : Code which causes the exception
except*   : to handle exception occured in try block
else
finally
'''

# After Exception handling
print("----After Exception handling----")
try:
    x = int(input("Enter numerator value :"))
    y = int(input("Enter denominator value :"))
    print("Division :", x / y)  # any value/0 = infinity
    print("---Division result usage---")
    print("---In try block3 ---")
except:
    print("Please enter denominator other than 0")
print("---Remaining code---")
print("---------------------------------")

'''
ATM money transfer
pinno
amount 
10,000
Amount: System Issue 

hdfc bank   : api call rest 
CANARA bank : atm machine exception 
'''
"""
#What is Exception?:?

An exception is an event, which occurs during the execution of a program
that disrupts the normal flow of the program's instructions.

#Handling an exception:?

If you have some suspicious code that may raise an exception,
you can defend your program by placing the suspicious code in a try: block.
After the try: block, include an except: statement,
followed by a block of code which handles the problem as elegantly as possible.

#Syntax
Here is simple syntax of try....except...else blocks

try:
   You do your operations here;
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block.

"""


#example:?

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()
"""
#The except Clause with No Exceptions:?

This kind of a try-except statement catches all the exceptions that occur. 
Using this kind of try-except statement is not considered a good programming practice 
though, because it catches all exceptions but does  not make the programmer 
identify the root cause of the problem that may occur.
"""
