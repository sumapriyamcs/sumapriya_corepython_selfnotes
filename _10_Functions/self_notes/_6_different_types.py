"""
# Function categories

1. Function with parameters, with return type
2. Function with parameters, without return type
3. Function without parameters, with return type
4. Function without parameters, without return type


4. Function without parameters, without return type:

 # Python Function with No Arguments, and No Return Value
def Adding():
    a = 20
    b = 30
    Sum = a + b
    print("After Calling the Function:", Sum)
Adding()

#print the message as user give?

def printt():
    print("This is Python 3.2 Tutorial")
    print("This is Python 3.2 Tutorial")
    print("This is Python 3.2 Tutorial")
printt()

3. Function without parameters, with return type:

# Python Function with No Arguments, and with Return Value
def Multiplication():
    a = 10
    b = 25
    Multi = a * b
    return Multi
print("After Calling the Multiplication Function: ", Multiplication())


2. Function with parameters, without return type

# Python Function with Arguments, and NO Return Value
def Multiplications(a, b):
    Multi = a * b
    print("After Calling the Function:", Multi)

Multiplications(10, 20)

#print the marks as a subject wise?

def marks(english, math = 85, science = 80):
print('Marks in : English is - ', english,', Math - ',math, ', Science - ',science)
marks(71, 77)
marks(65, science = 74)
marks(science = 70, math = 90, english = 75)

#average of two values?
def avg_number(x, y):
    print("Average of ",x," and ",y, " is ",(x+y)/2)
avg_number(3, 4)



1. Function with parameters, with return type:

# Python Function with Arguments, and Return Value
def Addition(a, b):
    Sum = a + b
    return Sum
# We are calling the Function Outside the Function Definition
print("After Calling the Function:", Addition(25, 45))


#average of the two values?
def average(x, y):
    return (x + y)/2
print(average(4, 3))

#sum of all the numbers present in the tuple?
def sum(*numbers):
     s = 0
     for n in numbers:
           s += n
     return s
#squares of the values?
def nsquare(x, y = 2):
    return (x*x + 2*x*y + y*y)
print("The square of the sum of 2 and 2 is : ", nsquare(2))
print("The square of the sum of 2 and 3 is : ", nsquare(2,4))


print(sum(1,2,3,4))



 """
