'''
@author: madhu
'''


def get_number(x, y):
    try:
        print("-----IN TRY BLOCK--------")
        result = x / y
        print("The result for division is : ", result)
        # float_res = round(24.601 / 0.01234, 4.6)
    except Exception as err:  # Exception err = ZeroDivisionError()
        print("---Error is being handled by super class Exception-----", err)
        """  
        except ZeroDivisionError as err:
            print("Please enter value other than Zero :: ",err, " is not supported programmatically")
        except TypeError as err:
            print("Plese check the calculation :::  ",err)
        except OverflowError as err:
            print("Please enter value other than Zero :: ",err, " is not supported programmatically")
        except Exception as err:
            print("---------------")

        """
    else:
        print("--------In ELSE block---------")
    finally:
        print("------Executing finally block--------------")


get_number(20, 5)


def main():
    try:
        height = float(input('Enter your height (meters):'))
        weight = float(input('Enter your weight (kilograms):'))

    except ValueError as error:
        print('Error! please enter a valid number.')
    else:
        bmi = round(calculate_bmi(height, weight), 1)
        evaluation = evaluate_bmi(bmi)

        print(f'Your body mass index is {bmi}')
        print(f'This is considered {evaluation}!')

def calculate_bmi(height, weight):
    """ calculate body mass index (BMI) """
    return weight / height**2


def evaluate_bmi(bmi):
    """ evaluate the bmi """
    if 18.5 <= bmi <= 24.9:
        return 'healthy'

    if bmi >= 25:
        return 'overweight'

    return 'underweight'


def main():
    try:
        height = float(input('Enter your height (meters):'))
        weight = float(input('Enter your weight (kilograms):'))

    except ValueError as error:
        print(error)
    else:
        bmi = round(calculate_bmi(height, weight), 1)
        evaluation = evaluate_bmi(bmi)

        print(f'Your body mass index is {bmi}')
        print(f'This is considered {evaluation}!')

main()



fruits = {
    'apple': 10,
    'orange': 20,
    'banana': 30
}

key = None
while True:
    try:
        key = input('Enter a key to lookup:')
        fruit = fruits[key.lower()]
    except KeyError:
        print(f'Error! {key} does not exist.')
    except KeyboardInterrupt:
        break
    else:
        print(fruit)
    finally:
        print('Press Ctrl-C to exit.')

# Else block will execute only when no exception occurs.:?

# Python code to illustrate
# working of try()
def divide(x, y):
	try:
		# Floor Division : Gives only Fractional
		# Part as Answer
		result = x // y
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")
	else:
		print("Yeah ! Your answer is :", result)

# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)

def handle_error():
    try:
        raise RuntimeError('oops!')
    except RuntimeError as error:
        print('handled a RuntimeError, no big deal.')
    else:
        print('if this prints, we had no error!') # won't print!
    print('And now we have left the try block!')  # will print!

try:
    this_should_raise_TypeError()
except TypeError:
    pass
except:
    assert False, "Raised the wrong exception type"
else:
    assert False, "Didn't raise any exception"

try:
    data = something_that_can_go_wrong()
except Exception as e: # yes, I know that's a bad way to do it...
    handle_exception(e)
else:
    do_stuff(data)
finally:
    clean_up()


a = [1,2,3]
try:
    something = a[2]
except:
    print ("out of bounds")
else:
    print (something)

try:
    age=int(input('Enter your age: '))
except:
    print ('You have entered an invalid value.')
else:
    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')

