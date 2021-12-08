"""
#PYTHON FUNCTIONS:

1.Functions are the most important aspect of an application.

2.A function can be defined as the organized block of reusable code, which can be called whenever required.

3.Python allows us to divide a large program into the basic building blocks known as a function.

4.The function contains the set of programming statements enclosed by {}.

5.A function can be called multiple times to provide reusability and modularity to the Python program.

6.The Function helps to programmer to break the program into the smaller part.

7.It organizes the code very effectively and avoids the repetition of the code.
As the program grows, function makes the program more organized.

8.Python provide us various inbuilt functions like range() or print().
Although, the user can create its functions, which can be called user-defined functions.

#There are mainly two types of functions.

1.User-define functions - The user-defined functions are those define by the user
to perform the specific task.

2.Built-in functions - The built-in functions are those functions that are pre-defined in Python.


#Advantage of Functions in Python:

There are the following advantages of Python functions.

1.Using functions, we can avoid rewriting the same logic/code again and again in a program.
2.We can call Python functions multiple times in a program and anywhere in a program.
3.We can track a large Python program easily when it is divided into multiple functions.
4.Reusability is the main achievement of Python functions.
5.However, Function calling is always overhead in a Python program.


#Creating a Function:

1.Python provides the def keyword to define the function.

The syntax of the define function is given below.

#Syntax:

def my_function(parameters):
      function_block
return expression

#Let's understand the syntax of functions definition.

1.The def keyword, along with the function name is used to define the function.
2.The identifier rule must follow the function name.
3.A function accepts the parameter (argument), and they can be optional.
4.The function block is started with the colon (:), and block statements must be at the same indentation.
5.The return statement is used to return the value. A function can have only one return


#Function Calling:

1.In Python, after the function is created, we can call it from another function.
2.A function must be defined before the function call; otherwise, the Python interpreter gives an error.
3.To call the function, use the function name followed by the parentheses.

#EX:
#function definition
def hello_world():
    print("hello world")
# function calling
hello_world()

#The return statement:

1.The return statement is used at the end of the function and returns the result of the function.
2.It terminates the function execution and transfers the result where the function is called.
3.The return statement cannot be used outside of the function.

#Syntax:

    return [expression_list]

4.It can contain the expression which gets evaluated and value is returned to the caller function.

5.If the return statement has no expression or does not exist itself in the function then it returns the None object.

#Arguments in function:

1.The arguments are types of information which can be passed into the function.
2.The arguments are specified in the parentheses.
3.We can pass any number of arguments, but they must be separate them with a comma.

#Call by reference in Python:

1.In Python, call by reference means passing the actual value as an argument in the function.

2.All the functions are called by reference, i.e.,

3.all the changes made to the reference inside the function revert back
to the original value referred by the reference.


#Types of arguments:

1.There may be several types of arguments which can be passed at the time of function call.

    1.1 Required arguments
    1.2 Keyword arguments
    1.3 Default arguments
    1.4 Variable-length arguments

2.Python. However, we can provide the arguments at the time of the function
Required Arguments Till now, we have learned about function calling in
arguments which are required to be passed at the time of function calling call.

3.As far as the required arguments are concerned, these are the definition.
If either of the arguments is not provided in the function call, or
the position of the arguments is changed, the Python interpreter will show the error.
with the exact match of their positions in the function call and function.


#Default Arguments:

1.Python allows us to initialize the arguments at the function definition.

2.If the value of any of the arguments is not provided at the time of function call,
then that argument can be initialized with the value given in the definition
even if the argument is not specified at the function call.

#Variable-length Arguments (*args):

1.In large projects, sometimes we may not know the number of arguments to be passed in advance.

2.In such cases, Python provides us the flexibility to offer the comma-separated values
which are internally treated as tuples at the function call.

3.By using the variable-length arguments, we can pass any number of arguments.

4.we define the variable-length argument using the *args (star) as *<variable - name >.

#Keyword arguments(**kwargs):

1.Python allows us to call the function with the keyword arguments.
This kind of function call will enable us to pass the arguments in the random order.

2.The name of the arguments is treated as the keywords and matched in the function calling and definition.
If the same match is found, the values of the arguments are copied in the function definition.


#a function definition that consists of the following components.



1.Keyword def that marks the start of the function header.

2.A function name to uniquely identify the function.
Function naming follows the same rules of writing identifiers in Python.-

3.Parameters (arguments) through which we pass values to a function. They are optional.

4.A colon (:) to mark the end of the function header.

5.Optional documentation string (docstring) to describe what the function does.

6.One or more valid python statements that make up the function body.
Statements must have the same indentation level (usually 4 spaces).

7.An optional return statement to return a value from the function.



#Scope of Variables:

1.All variables in a program may not be accessible at all locations in that program.
This depends on where you have declared a variable.

2.The scope of a variable determines the portion of the program where you can
access a particular identifier.

There are two basic scopes of variables in Python −

1.Global variables
2.Local variables

#Global vs. Local variables:

1.Variables that are defined inside a function body have a local scope,
and those defined outside have a global scope.

2.This means that local variables can be accessed only inside the function
in which they are declared, whereas global variables can be accessed
throughout the program body by all functions.

3.When you call a function, the variables declared inside it are brought into scope.

#Parameters or Arguments?:

1.The terms parameter and argument can be used for the same thing:
information that are passed into a function.

From a function's perspective:

1.1. A parameter is the variable listed inside the parentheses in the function definition.

2.2. An argument is the value that is sent to the function when it is called.

#Arbitrary Arguments, *args:

1.If you do not know how many arguments that will be passed into your function,
add a * before the parameter name in the function definition.

2.This way the function will receive a tuple of arguments, and can access the items accordingly:

Although it appears that lambda's are a one-line version of a function, they are not equivalent to inline statements in C or C++, whose purpose is by passing function stack allocation during invocation for performance reasons.






"""