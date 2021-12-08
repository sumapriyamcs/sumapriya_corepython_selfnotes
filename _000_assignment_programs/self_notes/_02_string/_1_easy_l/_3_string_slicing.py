"""
3. write a program to  find the slicing of string?

  I. CRUD            :  Retrieve
 II. State(variable) :  Datatype/strcuture   str = 'microchip'
III. Behavior        :  (Operators,DM,Loops)  =,:   for

#0. mathematics:
take a string to perform slicing operation
use the starting and ending index to get the ouput by using colon(:)

#1. by using builtin functions:
b = "Hello, World!"
print(b[2:5])

myText = "good morning"
mySlice = myText[0:5:1]
print(mySlice)

b = "Hello, World!"
print("slicing of the string is",(b[2:5])

#2.algorithm:
take a string for providing the slice operation
using the start and end index to get the output
return the final string
store that final string in one variable and print that variable

#3. functions

def str1(string):
    print(string[1:5])
    return str1
string="hellooo"
res=str1(string)
print(res)

# Python slice() function example
# Calling function
str1 ="microsoft solutions"
slic = slice(0,10,3) # returns slice object
slic2 = slice(-1,0,-3) # returns slice object
# We can use this slice object to get elements
str2 = str1[slic]
str3 = str1[slic2] # returns elements in reverse order
# Displaying result
print(str2)
print(str3)


"""

