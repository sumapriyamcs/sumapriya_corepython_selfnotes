'''1.Write a Python program to convert degree to radian.'''

pi=22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print(radian)

degree=int(input("enter the degree"))
radian=50*(3.14/180)
print("the total radians are",radian)

''' 2.) Write a Python program to calculate the area of a trapezoid. '''

height = float(input("Height of trapezoid: "))
base_1 = float(input('Base one value: '))
base_2 = float(input('Base two value: '))
area = ((base_1 + base_2) / 2) * height
print("Area is:", area)

'''  3.) Write a program that asks the user to enter two integers. 
Have the program output the two integers and the result when the first 
number entered is raised to the power of the second number entered.'''

a=int(input("enter the first number"))
b=int(input("enter the second number"))
print(a**b)

'''  4.) Write a computer program that asks the user to enter an integer (odd or even)
and have it report whether the integer entered is odd. 
You are required to implement this program using the modulus operator and 
an if ... Selection construct.'''

num=int(input("enter the number"))
if num%2==0:
        print("entered numbr is even")
else:
        print("entered number is odd")

'''5.) Write a Python program to calculate the area of a parallelogram.'''

base=int(input("enter the base value parallelogram"))
height=int(input("enter the height of parallelogram"))
print(base*height)