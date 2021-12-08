#loops in python:

'''Python programming language provides following types of loops to handle looping
requirements. Python provides three ways for executing the loops. While all the ways
provide similar basic functionality, they differ in their syntax and condition checking
time.'''


# While Loop:

'''1. In python, while loop is used to execute a block of statements repeatedly until a
given a condition is satisfied.
2.And when the condition becomes false, the line
immediately after the loop in program is executed.'''

 #while loop examples

'''count = 0 #state
while (count < 3): #condition
    count = count+1 #increment
    print (count)''' #business logic

#----------------------------------------------------------------------------------------------------------------------
'''count = 10;
while (count > 5):
    count = count-1
    print(count)'''

#--------------------------------------------------------------------------------------------------------------------------

# Print numbers from 1 to 10

'''num = 1             # state
while num <= 9:     # condition check each iteration(business logic)
    num = num + 1   #  increment
    print(num)      # part behaviour'''
#----------------------------------------------------------------------------------------------------------------
# print 1,2,3,4,5,......10
"""num = 0
while num <= 9:
    num = num + 1
    print(num,end=' ')
print() """
#----------------------------------------------------------------------------------------------------------------
# even number and odd numbers

"""num = 0
while num <= 10:
    num = num + 1
    if num %2 == 0:
        print("even number",num)
    else:
        print("odd number",num) """
#--------------------------------------------------------------------------------------------------------------------
# even number and odd numbers
"""
num = 0
while num <= 10:
    num = num + 1
    if num %2 == 0:
        print("even number",num)
    else:
        print("odd number",num) """
#----------------------------------------------------------------------------------------------------------------
"""
num = 0
while (num <=11):
    num = num + 1
    if num%3==0 :
        print(num,"divisible by 3")
"""
#------------------------------------------------------------------------------------------------------------------
# print numbers divisible by 3 and 5
"""num = 0
while num <= 100:
    num = num + 1
    if num % 3 == 0 and num % 5 == 0:
        print(" 3 and 5 divisibles are",num) """
#------------------------------------------------------------------------------------------------------------------------

# print numbers 20 to 40
'''a=20                     # state
while a <=40:            # defining conditional
    print(a)             # behaviour
    a+=1                 # increment'''

"""
a = int(input("enter a number"))
b = int(input("enter b number "))
if a < b:
    while a <= b:
        if a % 2 == 0:
            print(a)   """
#---------------------------------------------------------------------------------------------------------------------
# numbers between the even numbers
'''num1 = int(input("enter num1"))    # state, user input
num2 = int(input("enter num2 "))   # state   , user input
while num1 < num2:                 # defining condition (comparision num1 and num2)
    if num1 % 2 == 0:              # business logic
        print(num1)                # behaviour
    num1 = num1 +1                 # increment
print("-------------")
print("----end -----------")'''
#-------------------------------------------------------------------------------------------------
# odd numbers
'''num1 = int(input("enter number1"))
num2 = int(input("enter number2"))
while num1 <= num2:
    if num1%2 == 1:
        print("odd number is",num1)
    num1 +=1
print('------end--------')'''

#--------------------------------------------------------------------------------------------------------
# print 1 to 10
'''print("---------------------print 1 to 10----------------")
num = 1
while num <= 10:
    print(num, end=' ')
    num+=1
print('\n'"-----end ---------")'''
#--------------------------------------------------------------------------------------------------------------------------

# print 10 to 1
'''print("---------------------print 10 to 1----------------")
num = 10
while num >= 1:
    print(num, end=' ')
    num-=1
print('\n'"-----end ---------")'''

#--------------------------------------------------------------------------------------------------------------------------------------
# 8 multiples
'''print('---------------8 multiples------------------')
num = 1
while num <=100:
    if num % 8 == 0:
        print(num)
    num+=1
print("---------end--------------")'''
#--------------------------------------------------------------------------------------------------------------------------

#prime numbers
'''print("---------------prime numbers  between 1 to 100--------------")
num = 2
while num <= 100:
    if num%2 != 0 and num%3 != 0 and num%5 != 0:
        print(num)
    num+=1'''

#----------------------------------------------------------------------------------------------------------------------------------

# REQ : Print even numbers between 1 to 10
'''
  | 2  4          |   2)4(
'''
'''
# STATE    : num = 1

# BEHAVIOR : Print even numbers
             upper limit 10
'''
print("--------Print even numbers--------")
# STATE
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1

print("--------Print odd numbers--------")

# Print odd numbers betweeen 10 to 20
num = 10
while num <= 20:
    if num % 2 == 1:
        print(num)
    num += 1

# Print numbers between 500 to 1000 and divisible by 5

print("--Numbers divisible  with 5------")
num = 500
while num <= 600:
    if num % 5 == 0:
        print(num)
    num += 1


# Print numbers between 500 to 1000. It should be divisible by 5 and divisible by 8
print("--Numbers divisible  with 5 and 8------")
num = 500
while num <= 600:
    if num % 5 == 0 and num % 8 == 0:
        print(num)
    num += 1

# Print numbers between 500 to 1000. It should be divisible by 5 or divisible by 9
print("--Numbers divisible  with 5 or 9------")
num = 500
while num <= 600:
    if num % 5 == 0 or num % 9 == 0:
        print(num)
    num += 1


'''
S1 : REQUIREMENT : Print numbers which are divisible by 4 between 0 to 100

S2,S3 :Analysis,Design:
-----------------------
Step1: Take the user input,iterate till upper limit
Step2: Check whether the value divisible by 4 or not
Step3: If True, print the value
'''

# 0 1 2 3 4 5 6 7 8 9 10... 100
print("--------Numbers between 0 to 100---------")
x = 0
while x <= 100:
    if x % 4 == 0:
        print(x)
    x += 1


'''
# S1: REQUIREMENT : Print numbers which are divisible by 
                    either 3 or 8 between 1 to 1000
'''
print("-------------either 3 or 8 between 1 to 1000-------------")
x = 1
while x <= 1000:
    if x % 3 == 0 or x % 8 == 0:
        print(x)
    x += 1



'''
# S1: REQUIREMENT : Print numbers which are 
                    divisible by 5 and 10 between 1 to 100
'''
print("---------either 5 and 7 between 1 to 100-------------")
x = 1
while x <= 100:
    if x % 5 == 0 and x % 10 == 0:
        print(x)
    x += 1

x = 10
y = 20
print(x > y and y < 100)


# Program to add natural
# numbers up to
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)


'''Example to illustrate
the use of else statement
with the while loop'''

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")

# Prints all letters except 'e' and 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue

    print('Current Letter :', a[i])
    i += 1








