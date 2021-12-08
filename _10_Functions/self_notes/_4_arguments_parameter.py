"""

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


#arguments:

#defining the function
def func (name):
    print("Hi ",name)
#calling the function
func("Devansh")


#Python function to calculate the sum of two variables
#defining the function
def sum (a,b):
    return a+b;

#taking values from the user
a = int(input("Enter a: "))
b = int(input("Enter b: "))

#printing the sum of a and b
print("Sum = ",sum(a,b))




"""