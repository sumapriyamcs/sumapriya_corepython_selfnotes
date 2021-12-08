
'''
    Exception
    ArithmeticError
    ZeroDivisionError

'''
try:
    x = 'Madhu'
    y = -5
    if y <= 0:
        raise ValueError("Only positive numbers are allowed") # here i am throwing exception manually
    if type(x) != int:
        raise TypeError("Type Error")  # here i am throwing exception manually
except Exception as e:
    print("Exception occured :: ", e)

print("------------------------------------")
try:
    x = -20
    y = 30
    # raise TypeError("Type Error")
    if x < 0 or y < 0:
        raise ArithmeticError("** Negative Values are not allowed **")
    #raise ArithmeticError("A ISSUE")
    #raise ZeroDivisionError("ZDE ISSUE")
except ZeroDivisionError as zde:
    print("In Zero Division Error")
except ArithmeticError as ae:
    print("In Arithmetic Error :: ", ae)
except ValueError as ve:
    print("In Value Error")
except Exception as e:    # Exception e = TypError("Value is not proper")   3 Upcasting
    print("In Exception ")

print("Hello world")

print("----------------------------------------")

try:
    x = 20
    y = 30
    raise ValueError("Value is not proper")
    #raise ZeroDivisionError("ZDE ISSUE")
    #raise ArithmeticError("A ISSUE")

except ZeroDivisionError as zde:  # ZeroDivisionErrorzde zde = ZeroDivisionError("ZDE ISSUE")  2
    print("In Zero Division Error ::", zde)  # XXX ZeroDivisionErrorzde zde = ArithmeticError("A ISSUE")  4
except ArithmeticError as ae:     # ArithmeticError ae = ArithmeticError("A ISSUE")            1
    print("In Arithmetic Error ::", ae)
except Exception as e:  # Exception e = ValueError("Value is not proper")  3
    print("In Exception :: ", e)
print("Hello world")




try:
    pass
except Exception as e:
    print("Exception occured")

#Compiliation Exceptions,Runtime Exceotions

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
    print(variable)
except NameError:
    print("Variable is not defined")
except:
    print("Seeems like something else went wrong")

# try block
try:
    a = int(input("Enter numerator number: "))
    b = int(input("Enter denominator number: "))
    print("Result of Division: " + str(a/b))
# except block handling division by zero
except(ZeroDivisionError):
    print("You have divided a number by zero, which is not allowed.")
# except block handling wrong value type
except(ValueError):
    print("You must enter integer value")

# try block
try:
    a = int(input("Enter numerator number: "))
    b = int(input("Enter denominator number: "))
    print("Result of Division: " + str(a/b))
# except block handling division by zero
except(ValueError, ZeroDivisionError):
    print("Please check the input value: It should be an integer greater than 0")

# try block
try:
    a = int(input("Enter numerator number: "))
    b = int(input("Enter denominator number: "))
    print("Result of Division: " + str(a/b))
# except block handling division by zero
except(ZeroDivisionError):
    print("You have divided a number by zero, which is not allowed.")
# except block handling wrong value type
except(ValueError):
    print("You must enter integer value")
# generic except block
except:
    print("Oops! Something went wrong!")



n = int(input("Please enter a number: "))
while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print("Great, you successfully entered an integer!")


def int_input(prompt):
    while True:
        try:
            age = int(input(prompt))
            return age
        except ValueError as e:
            print("Not a proper integer! Try it again")

try:
    inp = input()
    print ('Press Ctrl+C or Interrupt the Kernel:')
except KeyboardInterrupt:
    print ('Caught KeyboardInterrupt')
else:
    print ('No exception occurred')

try:
    a = 100 / 0
    print (a)
except ZeroDivisionError:
        print ("Zero Division Exception Raised." )
else:
    print ("Success, no error!")

try:
    import math
    print(math.exp(1000))
except OverflowError:
        print ("OverFlow Exception Raised.")
else:
    print ("Success, no error!")

try:
    a = 100
    b = "DataCamp"
    assert a == b
except AssertionError:
        print ("Assertion Exception Raised.")
else:
    print ("Success, no error!")

class Attributes(object):
    a = 2
    print (a)

try:
    object = Attributes()
    print (object.attribute)
except AttributeError:
    print ("Attribute Exception Raised.")

try:
    a = {1:'a', 2:'b', 3:'c'}
    print (a[4])
except LookupError:
    print ("Key Error Exception Raised.")
else:
    print ("Success, no error!")

try:
    a = ['a', 'b', 'c']
    print (a[4])
except LookupError:
    print ("Index Error Exception Raised, list index out of range")
else:
    print ("Success, no error!")

try:
    print (ans)
except NameError:
    print ("NameError: name 'ans' is not defined")
else:
    print ("Success, no error!")


try:
    a = 5
    b = "DataCamp"
    c = a + b
except TypeError:
    print ('TypeError Exception Raised')
else:
    print ('Success, no error!')


try:
    print (float('DataCamp'))
except ValueError:
    print ('ValueError: could not convert string to float: \'DataCamp\'')
else:
    print ('Success, no error!')

def f():
    try:
        x = int("four")
    except ValueError as e:
        print("got it in the function :-) ", e)

try:
    f()
except ValueError as e:
    print("got it :-) ", e)


print("Let's get on")


try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
except ValueError:
    print("You should have given either an int or a float")
except ZeroDivisionError:
    print("Infinity")
finally:
    print("There may or may not have been an exception.")

