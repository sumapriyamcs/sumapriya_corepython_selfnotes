"""
1. write a program to swap the first and last character of a string?

I. CRUD            :  update
II. State(variable) :  Datatype/strcuture   str = 'pyspiders'
III. Behavior        :  (Operators,DM,Loops)  =,-   for

#0 mathematics:
step 1: take a string to swap first and last character
step 2: take a new variable to store the result
step 3: take last character as first by using slicing and first character as last
and mention how many characters you are going to swap by using slicing operation
step4: finally print the result

#1 by using inbuilt function

str = input("Enter a string : ")
new_str = str[-1:] + str[1:-1] + str[:1]
print(new_str)

#2. algorithm:

myString = "suma"
newString = (myString[1:len(myString)-1])
print(myString[len(myString)-1],newString,myString[0])

#3. functions:

def change(string):
   return string[-1: ] + string[1: -1] + string[: 1]
string = input("Enter string:")
print("Modified string:")
print(change(string))



"""