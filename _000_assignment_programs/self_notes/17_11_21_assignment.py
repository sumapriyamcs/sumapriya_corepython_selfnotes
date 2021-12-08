'''1.Mailing Address
Create a program that displays your name and complete mailing address formatted
in the manner that you would usually see it on the outside of an envelope.
Your program does not need to read any input from the user.'''

#solution 1:

def personal_details():
    name = "Suma priya"
    address = "Bangalore, Karnataka, India"
    print("Name:{}\nAddress:{}".format(name,address))
personal_details()


#solution2:

class add:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def get_det(self):
        print(f"name:{self.name}\naddress:{self.address}")
obj=add("suma priya","bangalore")
obj.get_det()


#solution 3:

name="suma priya"
address="bangalore,karnataka"
print("name:{}\naddress:{}".format(name,address))

#solution 4:

name="suma priya"
address="bangalore,karnataka"
print(name,address)


'''2: Hello
Write a program that asks the user to enter his or her name.
The program should respond with a message that says hello to the user, using his 
or her name
'''

#solution 1:

name=str(input("enter the user name"))
print("hello",name)
name="suma"
print("hello", name)

#solution 2:

def find():
    name=str(input("enter your name"))
    print("hello",name)
find()


def hello():
    name=str(input("enter the name : "))
    print("hello " + str(name))
    return
hello()

#solution 3:

class user():
    def __init__(self,name):
        self.name=name
    def display(self):
     print ('hello',self.name)
ob=user("suma")
ob.display()

'''3.Exercise 3: Area of a Room
Write a program that asks the user to enter the width and length of a room.
Once the values have been read, your program should compute and display the area 
of the room. The length and the width will be entered as floating point numbers. 
Include units in your prompt and output message; either feet or meters, 
depending on which unit you are more comfortable working with.'''

#solution 1:

length = float(input("Enter the length of the room in feet: "))
width = float(input("Enter the width of the room in feet: "))
area = length * width
print("The area of the room is", area, "square feet")

#solution 2:

def area():
    length = float(input("Enter the length of the room in feet: "))
    width = float(input("Enter the width of the room in feet: "))
    area = length * width
    return area


print("The area of the room is", area, "square feet")

#solution 3:

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print("the area of the room is",newRectangle.rectangle_area(),"square feet")
print(newRectangle.rectangle_area())

#solution 4:

a=float(input("enter the length of the room"))
b=float(input("enter the width of the room"))
c=a*b
print("The area of the room is",round(c,2),"square feet")

'''4.Area of a Field
Create a program that reads the length and width of a 
farmer’s field from the user in feet. Display the area of the field in acres.'''

#solution 1:

length=int(input("enter the length of the field"))
width=int(input("enter the width of the field"))
area=length*width
print("the area of the field is",area,"acres")
SQFT_PER_ACRE = 43560
length = float (input ("Enter the length of the field in feet: "))
width = float (input ("Enter the width of the field in feet: "))
acres = length * width / SQFT_PER_ACRE
print ("The area of the field is", acres, "acres")

#solution 2:

def field():
    length = int(input("enter the length of the field"))
    width = int(input("enter the width of the field"))
    area = length * width
    print("the area of the field is", area, "acres")
field()

def field():
    SQFT_PER_ACRE = 43560
    length=float(input("enter the length of the field"))
    width=float(input("enter the width of the field"))
    area=length*width/SQFT_PER_ACRE
    print("the area of the field is",area,"acres")
field()

#solution 3:

class field():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def display(self):
        return self.length*self.width
acres=field(12,15)
print("the area of field is",acres.display(),"acres")


class field():

    def __init__(self, length, width, sqft_per_acre):
        self.length = length
        self.width = width
        self.sqft_per_acre = sqft_per_acre
        # self.sqft_per_acre=sqft_per_acre

    def display(self):
        sqft_per_acre = 43560
        return self.length * self.width / sqft_per_acre
acres = field(12, 15, 43560)
print("the area of field is", acres.display(), "acres")

'''5.Bottle Deposits
In many jurisdictions a small deposit is added to drink containers to encourage
people to recycle them. In one particular jurisdiction, drink containers holding
one liter or less have a $0.10 deposit, and drink containers holding more than
one liter have a $0.25 deposit.Write a program that reads the number of
containers of each size from the user. Your program should continue by computing
and displaying the refund that will be received for returning those containers.
Format the output so that it includes a dollar sign and always displays exactly
two decimal places.'''

#solution 1:

container1 = int(input('enter number of containers with less than one litre:'))
container2 = int(input('enter number of containers with more than litre'))
less_prize = 0.10
more_prize = 0.25

total = (container1 * less_prize) + (container2 * more_prize)
print("refund for bottles $",total)


a=int(input("enter the containers less than one litre"))
b=int(input("enter the container more than one litre"))
c=a*0.12+b*0.25
print("refund for bottles $",c)

#solution 2:

def contain():
    a=int(input("enter the containers less than one litre"))
    b=int(input("enter the container more than one litre"))
    c=a*0.12+b*0.25
    print("refund for bottles $",c)
contain()

#solution 3:

class Contain():
    def __init__(self,prize1,prize2,a,b):
        self.prize1=prize1
        self.prize2=prize2
        self.a=a
        self.b=b
    def dis(self):
        a=4
        b=5
        prize1=0.12
        prize2=0.25
        return self.a*prize1+self.b*prize2
        #print(c)
        c = self.a * prize1 + self.b * prize2
        return c
shop=Contain(0.12,0.25,4,5)
print("refund for bottles are $",shop.dis())


'''6.Tax and Tip
The program that you create for this exercise will begin by reading the cost of a 
meal ordered at a restaurant from the user. Then your program will compute the tax 
and tip for the meal. Use your local tax rate when computing the amount of tax owing. 
Compute the tip as 18 percent of the meal amount (without the tax). The output from 
your program should include the tax amount, the tip amount, and the grand total for 
the meal including both the tax and the tip.Format the output so that all of the 
values are displayed using two decimal places.'''

#solution 1:

meal=int(input("enter the cost of the meal"))
tax=0.05
tip=0.18
tax = meal * tax
tip = meal * tip
res=meal+tax+tip
print("the total ammount for the restarunt bill is",tax,tip,res)

meal=int(input("enter the cost of the meal"))
tax=0.05
tip=0.18
res=meal+tax+tip
print(res)

#solution 2:

def res():

    meal=int(input("enter the cost of the meal"))
    tax=0.05
    tip=0.18
    tax = meal * tax
    tip = meal * tip
    res=meal+tax+tip
    print("the total ammount for the restarunt bill is",tax,tip,res)
res()
#solution 3:

class Res():
    def __init__(self,meal,tax,tip):
        self.meal=meal
        self.tax=tax
        self.tip=tip
    def dis(self):
        meal=200
        tax=0.05
        tip=0.18
        tax=tax*meal
        tip=tip*meal
        total=meal+tax+tip
        return total
bill=Res(200,0.05,0.18)
print("total bill for customer is",bill.dis())

'''7.Sum of the First n Positive Integers
(Solved—12 Lines) Write a program that reads a positive integer, n, from the user 
and then displays the sum of all of the integers from 1 to n. 
The sum of the first n positive integers can be computed using the formula:
sum = (n)(n + 1)/2'''
#solution 1:

n=int(input("enter the number"))
tot=0
for i in range(1,n+1):
    tot=n*(n+1)/2
print(tot)

n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print("Sum of the first", n ,"positive integers:", sum_num)

#solution 2:

def sum(n):
    n = int(input("Input a number: "))
    sum_num = (n * (n + 1)) / 2
    print("Sum of the first", n ,"positive integers:", sum_num)
sum(10)

#solution 3:

class Sum():
    def __init__(self,n):
        self.n=n
    def dis(self):
        n=10
        res=n*(n+1)/2
        return res
cal=Sum(10)
print("Sum of the first positive numbers are",cal.dis())

'''8.Widgets and Gizmos
An online retailer sells two products: widgets and gizmos. 
Each widget weighs 75 grams. Each gizmo weighs 112 grams. Write a program that 
reads the number of widgets and the number of gizmos in an order from the user. 
Then your program should compute and display the total weight of the order.'''

w=int(input("enter the widgets"))
g=int(input("enter the number of gizmos"))
weight=w*75+g*112
print(weight )

#solution 1:

w=int(input("enter the widgets"))
g=int(input("enter the number of gizmos"))
convert1=int(w)
convert2=int(g)
weightofwidgets=convert1*75
weightofgizmos=convert2*112
totalweight=weightofwidgets+weightofgizmos
print( totalweight )

widgets=int(input("enter the widgets"))
gizmos=int(input("enter the number of gizmos"))
wheightofwidgets=widgets*75
wheightofgizmos=gizmos*112
totalweight=wheightofwidgets+wheightofgizmos
print(totalweight)

#solution 2:

def compute():
    widgets = int(input("enter the widgets"))
    gizmos = int(input("enter the number of gizmos"))
    wheightofwidgets = widgets * 75
    wheightofgizmos = gizmos * 112
    totalweight = wheightofwidgets + wheightofgizmos
    print(totalweight)


compute()

'''9.Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent 
interest per year. The interest that you earn is paid at the end of the year, and 
is added to the balance of the savings account. Write a program that begins by 
reading the amount of money deposited into the account from the user. 
Then your program should compute and display the amount in the savings account 
after 1, 2, and 3 years.Display each amount so that it is rounded to 2 decimal places.'''
#solution 1:

rate_of_interest=0.04
deposit=int(input("enter the deposited amount"))
after_1year=deposit*rate_of_interest+deposit
print("the amount in the savings account after 1 {}".format(after_1year))
after_2year=(after_1year*rate_of_interest)+after_1year
print("the amount in the savings account after 2 {}".format(after_2year))
after_3year=(after_2year*rate_of_interest)+after_2year
print("the amount in the savings account after 3 {}".format(after_3year))

#solution 2:

def cal():
    import math
    a = 10
    b = 20
    add = a + b
    print("the sum of a and b is=", add)
    sub = a - b
    print("the subtraction of two valuesis=", sub)
    mul = a * b
    print("the multiplication of two values is=", mul)
    qu = a / b
    print("the quotient of two values is=", qu)
    rem = a % b
    print("the remainder of two values is", rem)
    result = math.log10(a)
    print("the result of log10 a=", result)
    res = a ** b
    print("the result of ab is=", res)


cal()

'''10.Arithmetic
Create a program that reads two integers, a and b, from the user. 
Your program should compute and display:

•	The sum of a and b
•	The difference when b is subtracted from a
•	The product of a and b
•	The quotient when a is divided by b
•	The remainder when a is divided by b
•	The result of log10 a
•	The result of ab'''

#solution 1:

import math
a=10
b=20
add=a+b
print("the sum of a and b is=" ,add)
sub=a-b
print("the subtraction of two valuesis=",sub)
mul=a*b
print("the multiplication of two values is=", mul)
qu=a/b
print("the quotient of two values is=",qu)
rem=a%b
print("the remainder of two values is",rem)
result=math.log10(a)
print("the result of log10 a=", result)
res=a**b
print("the result of ab is=",res)

#solution 2:

def cal():
    import math
    a = 10
    b = 20
    add = a + b
    print("the sum of a and b is=", add)
    sub = a - b
    print("the subtraction of two valuesis=", sub)
    mul = a * b
    print("the multiplication of two values is=", mul)
    qu = a / b
    print("the quotient of two values is=", qu)
    rem = a % b
    print("the remainder of two values is", rem)
    result = math.log10(a)
    print("the result of log10 a=", result)
    res = a ** b
    print("the result of ab is=", res)


cal()
'''
11.write a program to print alternative characters from
the string and those characters should be in upper case?'''


#s="suma priya"
#ms=s[::2]
#print(ms)
#print(ms.upper)











