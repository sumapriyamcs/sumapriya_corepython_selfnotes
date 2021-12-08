
"""
1. write a program to count the number of words present in the string?
 I. CRUD            :  Retrieve
 II. State(variable) :  Datatype/strcuture   str = 'good evening have a good day'
III. Behavior        :  (Operators,DM,Loops)  +=  for/while

#0 mathematics:

step 1: take a string to perform operation
step2:take initialization variable for storing the result
step 3: use for loop to split the words in string
step 4: store each words in initialization variable with +1 for incrementing
step 5: print that final result

# 1. by using inbuilt in functions:

s="hello world"
words=0
for i in s.split():
    words=words+1
print(words)

#2. algorithm:
s="hello world"



#3. using functions:

def count(str):
    words=0
    for i in str.split():
        words+=1
    return words
str="hello world hii"
res=count(str)
print(res)

#4.loops
"""



