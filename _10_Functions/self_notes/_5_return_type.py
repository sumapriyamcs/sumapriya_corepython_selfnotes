"""
#The return statement:

1.The return statement is used at the end of the function and returns the result of the function.
2.It terminates the function execution and transfers the result where the function is called.
3.The return statement cannot be used outside of the function.

#Syntax:

    return [expression_list]

4.It can contain the expression which gets evaluated and value is returned to the caller function.

5.If the return statement has no expression or does not exist itself in the function then it returns the None object.


#programs:

1. adding two values?

def adding(x, y):
    i = x + y
    return i
result = adding(16, 25)
print(f'Output of adding(16, 25) function is {result}')


2. write a program to returning the values for multiples times trough different functions names?

def adding(a, b):
    # this function is return the value of (a + b)
    return a + b
def boolean_function(a):
    # this function is return the Boolean value
    return bool(a)
# calling function
flag = adding(2, 3)
print("Output of first function is {}".format(flag))
flag = boolean_function(9 < 5)
print("\nOutput of second function is {}".format(flag))

3. wap to return the multiple values ?

def test():
    omg = "javatpoint is the best website to learn"
    i = 122
    return omg, i;
    # Return tuple, we could also.
# Driver code to test the above method.
omg, i = test()
# Assign return tuple
print(omg)
print(i)

        #and

def test():
    omg = "javatpoint"
    i = 122
    return [omg, i];
# Driver code to test the above method
list = test()
print(list)

        #and

def test():
    a = dict();
    a['omg'] = "javatpoint"
    a['i'] = 122
    return a
# Driver code to test the above method
a = test()
print(a)

4.wap to suares of the each value?

def square(x,y):
return x*x, y*y
t = square(2,3)
print(t)


5.wap to findout the minimum value?

def min_val(x,y):
if x < y :
return x
else :
return y
print( min_val(5,8) )
print( min_val(52,8) )


"""