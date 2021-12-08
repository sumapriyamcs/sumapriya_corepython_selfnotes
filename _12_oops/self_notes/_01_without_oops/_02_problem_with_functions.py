"""
#Disadvantages of functions:

1.Writing pure functions is easy, but combining them into a complete
application is where things get hard.

2.The advanced math terminology (monad, monoid, functor, etc.) makes FP intimidating.
For many people, recursion doesn’t feel natural.

3.Because you can’t mutate existing data, you instead use a pattern that
I call, “Update as you copy.”

4.Pure functions and I/O don’t really mix.

5.Using only immutable values and recursion can potentially lead to performance
problems, including RAM use and speed.

# REQ: Find length of the string

  # 1. STATE
str1 = 'hello world'

  # 2.BEHAVIOR
def find_length(in_str):
    le = 0
    for char in in_str:
        le += 1
    return le


print("Length of string : ", find_length(str1))
str1 = str1 + 'python world'
print("Length of string : ", find_length(str1))
# Here the state variable str1 can be accessed and modified by anyone in entire project
# Solution is , combine both state and behavior and configure in a single entity(i.e, class)

"""
