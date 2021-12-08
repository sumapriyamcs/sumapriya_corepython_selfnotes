# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
	for arg in argv:
		print (arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
myFun('suma','priya','ravi','kumar','sunandha','yeswanth')

def find(*args):
    for i in args:
        print(i)
find(1,2,3,'suma','nature','lover')

# Python program to illustrate
# *args with first extra argument
def myFun(arg1, *argv):
	print ("First argument :", arg1)
	for arg in argv:
		print("Next argument through *argv :", arg)

myFun('priya', 'good morning', 'to', 'myworld')

def adder(x,y,z):
    print("sum:",x+y+z)

adder(10,12,13)


def adder(*num):
    sum = 0

    for n in num:
        sum = sum + n

    print("Sum:", sum)


adder(3, 5)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')


def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)


def team(*employess):
    for i in employess:
        print(i)


team("rinky", "priya")

