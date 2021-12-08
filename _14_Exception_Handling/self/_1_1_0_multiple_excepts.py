'''
# Without EH
print("Start of program")
x = int(input("Enter numerator value :"))   # ValueError
y = int(input("Enter denominator value:"))  # ValueError
li = [1,2,3,4]
print(li[3])   # IndexError
print("Division :", x / y)  # ZeroDivisionError
print("Hello world")
print("---------------------------------")
'''

# Handling multiple exceptions
'''
HANDLING MULITPLE EXCETIONS

To handle multiple exceptions,write mulitple except blocks
Below code is not proper 
'''
print("Start of program")
try:
    # print("----While Exception handling----")
    x = int(input("Enter numerator value :"))  # ValueError
    y = int(input("Enter denominator value:"))
    li = [1, 2, 3, 4]
    print("List val:", li[2])  # IndexError
    print("Division :", x / y)  # ZeroDivisionError
    print("Hello world")
    print("---------------------------------")
except Exception as e:
    print("** Error occured :  **", e)
'''
except:
    print("** Error occured :  **")

    5L Water <-- 1L 2L 2.5L 3L 3.5L 4L 5L

    Animal  a = Tiger()   5L CAN <---- 2L Water
    Animal  a = Lion()
    Animal  a = Cat()
    Animal  a = Dog()
'''

#Through Multiple except Blocks:?

# catching multiple exception with single try
# and multiple except block
x = [1, 2, 3, 4]
for i in range(0, 3):
    try:
        if i == 0:
            print(y)
        elif i == 1:
            5 / 0
        else:
            x[4]

    # Multiple except blocks to handle Exceptions
    except NameError as e:
        print("Seems variable not defined")

    except IndexError as e:
        print("Index out of bound")

    except ZeroDivisionError as e:
        print("Answer is infinity")

    except:
        print("Unknown Error Caught")
#Catch Multiple Exceptions in Single except block
# catch multiple exceptions in single except
x = [1, 2, 3, 4]
for i in range(0, 3):
    try:
        if i == 0:
            print(y)
        elif i == 1:
            5 / 0
        else:
            x[4]

    # Multiple Exceptions caught in single except
    except (NameError, IndexError, ZeroDivisionError) as e:
        print("{}: {}".format(type(e).__name__, e))

    except:
        print("Unknown Error Caught")
#Catching All Exception in single except clause:?
#catch All the exceptions in single except block
x=[1,2,3,4]
for i in range(0,4):
    try:
        if i == 0: print(y)
        elif i == 1: 5/0
        elif i == 2: int("xyz")
        else: x[4]

    #except catches all exceptions with Exception as Base
    except Exception as e:
        print("{}: {}".format(type(e).__name__,e))
#Ignore All exceptions:?
#ignore all the exceptions raised in block
x=[1,2,3,4]
for i in range(0,4):
    try:
        if i == 0: print(y)
        elif i == 1: 5/0
        elif i == 2: int("xyz")
        else: x[4]

    #catch all exceptions and ignore it
    except BaseException as e:
        pass

print("Try Block successfully executed")

#Python catch multiple exceptions:?

import math
integers = ['orange',6,-8,'apple']
for number in integers:
    try:
        number_factorial = math.factorial(number)
    except TypeError:
        print("The input is not supported.")
    except ValueError:
        print( number," is not a positive integer.")

#CATCH DIFFERENT TYPES OF EXCEPTON:?

import sys
try:
   n = 0
   m = 2
   c = m/n
except(ZeroDivisionError) as e:
    print("The zero can't be divided")
try:
       n = 2
       m = '3'
       p = m+n
except TypeError:
    print('The number is in the string format')

#CATCHING MUTIPLE EXCEPTIONS IN ONE LINE:?
import sys
try:
    number = 2
    number = number+'5'
except(TypeError, SyntaxError, ValueError)as e:
    print("The number is given in string format")
#ALL EXCEPTIONS:?
try:
  print(python)
except NameError:
  print("python is not defined")
try:
    list = [1,2,3]
    print(list[5])
except IndexError as e:
    print(e)
print("index error")
try:
    from cv import numpy
except Exception:
    print("improper module")
try:
  print(hello)
except:
  print("hello is not defined")
finally:
  print(" The finally is executed")
try:
    print(chair)
except NameError:
    print ("NameError:'cot' is not defined")
else:
    print ("word found no error")
#DIFFERENT TYPES OF EXCEPTION:?
try:
   n = 0
   m = 3
   c = m/n
except(ZeroDivisionError) as e:
    print("The zero can't be divided")
try:
       n = 2
       m = 'HEllo'
       p = m+n
except TypeError:
    print('The number is in the string format')
try:
    from cv import pandas
except Exception:
    print("improper module")

#MULTIPLE EXCEPTIONS:?
try:
  print(x)
except TypeError:
  print("x is not defined")
except:
  print("Error")
try:
  print(a+b)
except:
  print("exception occured")
try:
  print(hello)
except SyntaxError as e:
  print("Invalid syntax")
except:
    print("Invalid syntax")

