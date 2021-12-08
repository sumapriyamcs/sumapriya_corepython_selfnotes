"""
2. count the characters of string?

 I. CRUD            :  update
 II. State(variable) :  Datatype/strcuture   integer string/str = 'good morning'
III. Behavior        :  (Operators,DM,Loops)  +=   for


#0: mathematics
take the string from the user
take the initialization variable as len=0 to count the characters of a string
use for loop to iterate a string characters
store each character in len with +1 increment
return/print the len function  at end of the program

#1. built in functions:

str1 = "good morning"

x = len(str1)

print(x)

#2.algorithm
step1: take the string from the user
step2: take result variable to strore all characters count
step3:iterate the each character by using for loop
step4: store each character in result variable wirh +1
step5: return that result as a total count of characters

def count(st):
    res=0
    for i in st:
        res+=1
    return res
st="goodmorning"
print(count(st))

#3. using functions:

def count_chars(txt):
	result = 0
	for char in txt:
		result += 1
	return result
txt="goodmorning"
print (count_chars(txt))

#4. using oops:

"""