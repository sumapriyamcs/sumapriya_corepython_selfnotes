"""
# Passing Arguments

1. Positional arguments (Required arguments)
2. Default arguments
3. Keyword arguments (Named arguments)

1. positional arguments:

2.Default Arguments:

    1.Python allows us to initialize the arguments at the function definition.

    2.If the value of any of the arguments is not provided at the time of function call,
    then that argument can be initialized with the value given in the definition
    even if the argument is not specified at the function call.


3. Keyword arguments(**kwargs):

    1.Python allows us to call the function with the keyword arguments.
    This kind of function call will enable us to pass the arguments in the random order.

    2.The name of the arguments is treated as the keywords and matched in
    the function calling and definition.
    If the same match is found, the values of the arguments are copied in the function definition.


# programs:

#requirement : Add two no
#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
add(10,75)     # Argument



#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
add(10+60,75)     # Argument




#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
add(10+60,75-85)     # Argument




#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
n=int(input("Enter a no"))
add(n,75-85)     # Argument


#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
n=int(input("Enter a no"))
add(n,0)     # Argument


#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
#n=int(input("Enter a no"))
print("zero")
add(0,0)     # Argument



#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
n=int(input("Enter a no"))
print("zero")
add(0,0)     # Argument




#requirment : Increase 30% from current salary
#Behavior
def hike(sal=30000):     # Function defination
 fsal=sal+sal*30/100
 print("After hike sal =  ", fsal)        # Responsibility
 #State
hike()    # function calling without argument



#requirment : Deduct 10% from current salary
#Behavior
def deduct(sal):   #Function Calling
 fsal=sal-sal*10/100
 print("After deduction sal is =  " , fsal)    # Responsibility
#State
esal=int(input("Enter sal of employee"))
deduct(esal)     # function calling with argument

# print marks as a subject wise?

def marks(english, math = 85, science = 80):
print('Marks in : English is - ', english,', Math - ',math, ', Science - ',science)
marks(71, 77)
marks(65, science = 74)
marks(science = 70, math = 90, english = 75)


#arguments combinations:

def f(a, b, c):                # f(a=1, b=2, c=3) | f(1, b=2, c=3) | f(1, 2, b=3) | f(1, 2, 3)
def f(*, a, b, c):             # f(a=1, b=2, c=3)
def f(a, *, b, c):             # f(a=1, b=2, c=3) | f(1, b=2, c=3)
def f(a, b, *, c):             # f(a=1, b=2, c=3) | f(1, b=2, c=3) | f(1, 2, c=3)

def f(*args):                  # f(1, 2, 3)
def f(a, *args):               # f(1, 2, 3)
def f(*args, c):               # f(1, 2, c=3)
def f(a, *args, c):            # f(1, 2, c=3)

def f(**kwargs):               # f(a=1, b=2, c=3)
def f(a, **kwargs):            # f(a=1, b=2, c=3) | f(1, b=2, c=3)
def f(*, a, **kwargs):         # f(a=1, b=2, c=3)

def f(*args, **kwargs):        # f(a=1, b=2, c=3) | f(1, b=2, c=3) | f(1, 2, c=3) | f(1, 2, 3)
def f(a, *args, **kwargs):     # f(a=1, b=2, c=3) | f(1, b=2, c=3) | f(1, 2, c=3) | f(1, 2, 3)
def f(*args, b, **kwargs):     # f(a=1, b=2, c=3) | f(1, b=2, c=3)
def f(a, *args, c, **kwargs):  # f(a=1, b=2, c=3) | f(1, b=2, c=3) | f(1, 2, c=3)


def func(name):  #required arguments
    message = "Hi "+name
    return message
name = input("Enter the name:")
print(func(name))


#the function simple_interest accepts three arguments and returns the simple interest accordingly
def simple_interest(p,t,r):
    return (p*t*r)/100
p = float(input("Enter the principle amount? "))
r = float(input("Enter the rate of interest? "))
t = float(input("Enter the time in years? "))
print("Simple Interest: ",simple_interest(p,r,t))



#the function calculate returns the sum of two arguments a and b
def calculate(a,b):
    return a+b
calculate(10) # this causes an error as we are missing a required arguments b.


#default arguments
def printme(name,age=22):
    print("My name is",name,"and age is",age)
printme(name = "john")


def printme(name,age=22):
    print("My name is",name,"and age is",age)
printme(name = "john") #the variable age is not passed into the function however the default value of age is considered in the function
printme(age = 10,name="David") #the value of age is overwritten here, 10 will be printed as age

#variable length(*args)

def printme(*names):
    print("type of passed argument is ",type(names))
    print("printing the passed arguments...")
    for name in names:
        print(name)
printme("john","David","smith","nick")

#keyword arguments:

#function func is called with the name and message as the keyword arguments
def func(name,message):
    print("printing the message with",name,"and ",message)

    #name and message is copied with the values John and hello respectively
    func(name = "John",message="hello")

#providing the values in different order at the calling?

#The function simple_interest(p, t, r) is called with the keyword arguments the order of arguments doesn't matter in this case
def simple_interest(p,t,r):
    return (p*t*r)/100
print("Simple Interest: ",simple_interest(t=10,r=10,p=1900))


#The function simple_interest(p, t, r) is called with the keyword arguments.
def simple_interest(p,t,r):
    return (p*t*r)/100

# doesn't find the exact match of the name of the arguments (keywords)
print("Simple Interest: ",simple_interest(time=10,rate=10,principle=1900))


def func(name1,message,name2):
    print("printing the message with",name1,",",message,",and",name2)
#the first argument is not the keyword argument
func("John",message="hello",name2="David")



def func(name1,message,name2):
    print("printing the message with",name1,",",message,",and",name2)
func("John",message="hello","David")


#Many arguments using Keyword argument

def food(**kwargs):
    print(kwargs)
food(a="Apple")
food(fruits="Orange", Vagitables="Carrot")


 """

