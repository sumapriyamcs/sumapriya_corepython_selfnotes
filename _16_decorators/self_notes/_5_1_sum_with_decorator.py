def decorateFun(func):
    def sumOfSquare(x, y):
        return func(x ** 2, y ** 2)

    return sumOfSquare


@decorateFun
def addTwoNumbers(a, b):
    c = a + b
    return c
c = addTwoNumbers(4, 5)
print("Addition of two numbers=", c)

def decorateFun(func):
    def addition(a,b,c):
        return func (a,b,c)
    return addition
@decorateFun
def multiplication(x,y,z):
    res=x*y*z
    return res
res=multiplication(5,7,8)
print("multiplication of three values are=",res)
'''
def decorateFun(func):
    def prime(num):
        num = 29

        # To take input from the user
        # num = int(input("Enter a number: "))

        # define a flag variable
        flag = False

        # prime numbers are greater than 1
        if num > 1:
            # check for factors
            for i in range(2, num):
                if (num % i) == 0:
                    # if factor is found, set flag to True
                    flag = True
                    # break out of loop
                    break

        # check if flag is True
        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
@decorateFun
def finds(num):
    for i in range(1,num+1):
        if num%2==0:
            print("even")
        else:
            print("odd")
    return finds(5)
print("the prime number values are=",res)'''
#res=sub(10,3)
#print("the subtraction of two numbers are=",res)
#res=n(5)
#print(res)

# Program to check if a number is prime or not



