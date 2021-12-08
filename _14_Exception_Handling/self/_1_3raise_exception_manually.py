
try:
    amt = 1000
    if amt < 5000:
        raise NameError("Insuff. Funds") # Raise exception manually
except NameError as name:
    print("AN EXCEPTION OCCURED ::", name)

'''
In Java, below line is object cration

Java   : NameError name = NameError("Insuff. Funds")

Python : name = NameError("Insuff. Funds")  # Rem. all scenarios
         NameError name = NameError("Insuff. Funds")   #Exception handling
'''


"""
The raise statement allows the programmer to force a specified exception to occur.

"""
#example:
try:
    raise NameError
except NameError:
    print('An exception flew by!')
    raise
"""
The raise statement allows an optional from which enables chaining exceptions
"""

def func():
    raise ConnectionError
try:
   func()
except ConnectionError as exc:
   raise RuntimeError('Failed to open database') from exc

"""
Exception chaining happens automatically when an exception is raised inside an except or finally section. 
This can be disabled by using from None idiom:
"""

try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

#example:
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

#Raise a TypeError if x is not an integer:

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

