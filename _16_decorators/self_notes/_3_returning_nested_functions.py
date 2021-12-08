def greeting(first, last):
  # nested helper function
  def getFullName():
    return first + " " + last

  print("Hi, " + getFullName() + "!")

greeting('Quincy', 'Larson')

def num1(x):
  def num2(y):
    return x + y
  return num2

print(num1(10)(5))

def num1(x):
   def num2(y):
      return x * y
   return num2
res = num1(10)

print(res(5))

def outer_function(x):
    # Hidden from the outer code
    def inner_increment(x):
        return x + 2
    y = inner_increment(x)
    print(x, y)

#inner_increment(5)
outer_function(5)

def function1(name):
    def function2():
        print('Hello ' + name)
    return function2

func = function1('suma priya')
func()

def find_power(num):  # outer function

    def power(n):
        return num ** n

    return power(2)  # calling inner function and returning the value returned by it

print(find_power(10))  # calling outer function


def print_even(lst):
    def find_even(num):
        if num % 2 == 0:
            return True
        else:
            return False

    new_list = []

    for num in lst:
        if find_even(num) == True:
            new_list.append(num)

    print("Final list:", new_list)


mylist = [1, 2, 4, 5, 6, 7, 10, 11, 12]
print_even(mylist)


def get_factorial(num):
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * factorial(num - 1)

    if not isinstance(num, int):
        raise TypeError("Failed! The value must be a number")

    if num < 0:
        raise ValueError("Failed! The number must be non-negative")

    return factorial(num)


print(get_factorial(5))
