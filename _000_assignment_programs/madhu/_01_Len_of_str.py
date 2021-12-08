# P01. REQ : Find length of given string   ie., "Hello World"

'''
Topics:
--------
Operators
DM vs Loops
Data structure
'''

# 0. Mathematics
# Implement the solutions in white paper

# 1.Builtin functions

print("-----1. Built Functions--------")

message = 'Hello World'  # static way
# message = input("Enter any string : ")

print("Length of given string : ", len(message))


# 2. Algorithm

print("--------2. Algorithm----------")

message = 'Hello World'
le = 0
for char in message:
    le += 1
print("Length of given string : ", le)

# 3 Using Functions  ==>
print("--------3 Using Functions----------")
    # I. STATE
message = 'Hello World'
le = 0
    # BEHAVIOR
def get_str_len(msg):
    leng = 0
    for char in msg:
        leng += 1
    print("Length of given string : ", leng)

get_str_len(message)




# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")
# 5 Exception handling  ==> 2
print("--------5 Exception handling----------")
# 6 File Handling  ==> 1
print("--------6 File Handling----------")
# 6 Database interaction MVC  ==> 1
print("--------6 Database interaction----------")
# 7 UI Interaction   ==> 1
print("--------7 UI Interaction----------")
