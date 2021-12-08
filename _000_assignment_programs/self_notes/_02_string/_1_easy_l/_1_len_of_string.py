"""
# P01. REQ : Find length of given string   ie., "Hello World"


  I. CRUD            :  Retrieve
 II. State(variable) :  Datatype/strcuture   integer string/str = 'Hello World'
III. Behavior        :  (Operators,DM,Loops)  +=   for

# 0. Mathematics
# Implement the solutions in white paper

- Hello World
- initialize the counter to 0
- count each character
- while counting incrementing counter value +1 in each iteration
# 1.Builtin functions

str1 = "hello world"
print("The length of the string  is :", len(str1))

# 2. Algorithm

step1: take the string which you want to display the string
step2: take the initialization variable as count=0 to count the characters of the string
step3:take for loop to iterate the string
step4:store the each character in count and while adding the each character increment the count with +1
step5: return that count variable

message = 'Hello World'
le = 0
for char in message:
    le += 1
print("Length of given string : ", le)

# 3 Using Functions

print("before findng the length of the string")
print("hello world")
def findLength(str):
    counter = 0
    for i in str:
        counter += 1
    return counter


str = "hello world"
print("after finding the length of the string")
print("length of the given string is",findLength(str))


message = 'Hello World'

def get_len(in_str):
    le = 0
    for char in in_str:
        le += 1
    print("Length of given string : ", le)

get_len(message)


message = 'Hello World'

def get_len(in_str):
    le = 0
    for char in in_str:
        le += 1
    return le

le = get_len(message)
print("Length of given string : ", le)

"""