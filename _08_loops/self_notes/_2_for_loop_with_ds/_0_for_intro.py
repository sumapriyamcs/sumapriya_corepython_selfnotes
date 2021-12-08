"""
A for loop will iteratively execute code for each item in a pre-defined list.
This list can be composed of numeric values, filenames,
individual characters in a text string and objects such as data structures.

A for loop is a programming statement that tells Python to iterate over a collection of objects,
performing the same operation on each object in sequence.

A Python for loop can be used to iterate over a list of items and perform a set
of actions on each item.


# Data types
x = 10
x = 10.5
x = True
msg = 'Hello World'
# Data structures
msg = 'Hello World'
list1 = [1,2,3,4,5]
tup1 = (1,2,3,4,5)
dict1 = {1:1, 2:2, 3:3}
set1 = {1, 2, 3, 4, 5, 6}

# while
i = 10
while i <= 10:
    print(i)
    i += 1


# for loop
'''
# collection of elements   : set   sequence    matrix
# sequence in python       : string list tuple
                             range   <bytearrays, buffers>

for <var> in <sequence>:
    # perform business logic
'''
print("--------For loop with String-------")
msg = 'Hello World'

for char in msg:
    print("Character : ", char)

for element in msg:
    print("Character : ", element)

"""