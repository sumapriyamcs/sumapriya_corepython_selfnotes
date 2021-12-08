"""
1. write a program to remove the odd index values present in the string?

I. CRUD            :  delete
II. State(variable) :  Datatype/strcuture   str = 'happy diwali to everyone'
III. Behavior        :  (Operators,DM,Loops)  +=,%,==  for

#0 mathematics
step1: take a string to remove the odd index values
step2: take new string for storing the result
step3: take a for loop to iterate the characters present in the string
step4: use modules operator for removing odd indexing characetrs present in the string
step 5:store the each character in result string after removing the odd index characters
step6: print the result string

#1 by using inbuilt functions
s="hello"
  for i in range(len(s)):
    if i%2==0:
        print(i)

#2. algorithm:

str1 = input("Please Enter your Own String : ")

str2 = ''

for i in range(len(str1)):
    if(i % 2 == 0):
        str2 = str2 + str1[i]

print("Original String :  ", str1)
print("Final String :     ", str2)

#3.by using functions

def modify(string):
  final = ""
  for i in range(len(string)):
    if i % 2 == 0:
      final = final + string[i]
  return final
string=raw_input("Enter string:")
print("Modified string is:")
print(modify(string))

#4.loops



"""