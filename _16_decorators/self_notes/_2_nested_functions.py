'''
#nested functions:?
Everything in Python is an object. Even function is a type of object in Python. Decorators are a special
type of function which return a wrapper function. They are considered very powerful in
Python and are used to modify the behaviour of a function temporarily without changing its actual value.

Nesting means placing or storing inside the other. Therefore, Nested Decorators means applying more
than one decorator inside a function. Python allows us to implement more than one decorator to a function.
It makes decorators useful for reusable building blocks as it accumulates the several effects together.

#How several decorators are applied?

A function can be decorated multiple times. We need to define the decorator first that we want to wrap the
output string with, and then apply them to the function using the ‘@’ .
'''


# Python program to demonstrate
# nested decorators

def italic(func):
    def wrapper():
        return '<i>' + func() + '</i>'

    return wrapper


def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'

    return wrapper


@italic
@strong
def introduction():
    return 'This is a basic program'


print(introduction())

def func(f):
    def deco(*args, **kwargs):
        return f(*args, **kwargs)
    return deco

@func
def sum(a, b):
    return a+b

print (sum(5, 10))

def func(num):
    def nested_func():
        return num
    return nested_func
print(func(5))

