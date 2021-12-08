"""

to using pdb is causing the interpreter to enter the debugger when you want it to.
There are a few different ways to do that,
depending on your starting conditions and what you need to debug.


"""

class MyObj(object):

    def __init__(self, num_loops):
        self.count = num_loops

    def go(self):
        for i in range(self.count):
            print (i)
        return

if __name__ == '__main__':
    MyObj(5).go()



import pdb

def f(n):
    for i in range(n):
        j = i * n
        print (i, j)
    return

if __name__ == '__main__':
    pdb.set_trace()
    f(5)

import pdb

def calc(i, n):
    j = i * n
    return j

def f(n):
    for i in range(n):
        j = calc(i, n)
        print (i, j)
    return

if __name__ == '__main__':
    pdb.set_trace()
    f(5)


import pdb


def addition(a, b):
	answer = a + b
	return answer


pdb.set_trace()
x = input("Enter first number : ")
y = input("Enter second number : ")
sum = addition(x, y)
print(sum)


def multiply(a, b):
	answer = a * b
	return answer


x = input("Enter first number : ")
y = input("Enter second number : ")
result = multiply(x, y)
print(result)


def addition(a, b):
	answer = a + b
	return answer


x = input("Enter first number : ")
y = input("Enter second number : ")
sum = addition(x, y)
print(sum)


# importing pdb
import pdb

# make a simple function to debugg
def fxn(n):
	for i in range(n):
		print("Hello! ", i+1)


# starting point to debugg
pdb.set_trace()
fxn(5)


# a simple function
def fxn(n):
	for i in range(n):
		print("Hello! ", i+1)


# using breakpoint
breakpoint()
fxn(5)

 # Printing Variables or expressions

# importing pdb
import pdb

# define recursive function
def rec_fxn(r):
	if r > 0:

		# set trace
		pdb.set_trace()
		rec_fxn(r//2)
	else:
		print("recursion stops")
	return

# set trace at start
pdb.set_trace()
rec_fxn(5)
