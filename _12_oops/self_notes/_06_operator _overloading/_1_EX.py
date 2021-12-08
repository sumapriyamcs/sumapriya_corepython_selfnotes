"""
#What is Operator Overloading in Python
The operator overloading in Python means provide extended meaning beyond their
predefined operational meaning. Such as, we use the "+" operator for adding two
integers as well as joining two strings or merging two lists. We can achieve this as the "+"
operator is overloaded by the "int" class and "str" class. The user can notice that the
same inbuilt operator or function is showing different behaviour for objects of different classes.
This process is known as operator overloading.


"""
"""
#Mathematical Operator:
Name	                Symbol	            Special Function
Addition	                +	             __add__(self, other)
Subtraction	                -	             __sub__(self, other)
Division                	/	             __truediv__(self, other)
Floor Division	            //	             __floordiv__(self, other)
Modulus(or Remainder)	    %	             __mod__(self, other)
Power	                    **	             __pow__(self, other)

#Assignment Operator:
Name	                Symbol	                Special Function
Increment	                +=	                __iadd__(self, other)
Decrement	                -=	                __isub__(self, other)
Product	                    *=	                __imul__(self, other)
Division	                /=	                __idiv__(self, other)
Modulus	                    %=	                __imod__(self, other)
Power	                    **=	                __ipow__(self, other)

#Relational Operator:
Name	                  Symbol	                Special Function
Less than	                <	                    __lt__(self, other)
Greater than	            >	                    __gt__(self, other)
Equal to	                ==	                    __eq__(self, other)
Not equal	                !=	                    __ne__(self, other)
Less than or equal to	    <=	                    __le__(self, other)
Greater than or equal to	> =	                    __gt__(self, other)
"""
#overloading +operator::

class Complex:
    # defining init method for class
    def __init__(self, r, i):
        self.real = r
        self.img = i

    # overloading the add operator using special function
    def __add__(self, sec):
        r = self.real + sec.real
        i = self.img + sec.img
        return complex(r,i)

    # string function to print object of Complex class
    def __str__(self):
        return str(self.real)+' + '+str(self.img)+'i'

c1 = Complex(5,3)
c2 = Complex(2,4)
print("sum = ",c1+c2)

#operator > operator:

class Complex:
    # defining init method for class
    def __init__(self, r, i):
        self.real = r
        self.img = i

    # overloading the less than operator using special function
    def __lt__(self, other):
        if self.real < other.real:
            return True
        elif self.real == other.real:
            if self.img < other.real:
                return True
            else:
                return False
        else:
            return False

    # string function to print object of Complex class
    def __str__(self):
        return str(self.real)+' + '+str(self.img)+'i'

c1 = Complex(5,3)
c2 = Complex(2,4)
print("Is c1 less than c2: ",c1<c2)


# Python program to show use of
# + operator for different purposes.

print(1 + 2)

# concatenate two strings
print("prutor"+'DOT')

# Product two numbers
print(3 * 4)

# Repeat the String
print("prutor"*4)


# Python Program illustrate how
# to overload an binary + operator

class A:
    def __init__(self, a):
        self.a = a

# adding two objects
def __add__(self, o):
    return self.a + o.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("prutor")
ob4 = A('DOT')

print(ob1 + ob2)
print(ob3 + ob4)


# Python Program to perform addition
# of two complex numbers using binary
# + operator overloading.

class Sample():

    def __init__(self,a ):
        self.a  = a

    def __add__(self, other):
        return self.a + other.a

s1 = Sample(10)
s2 = Sample(20)
s3 = Sample(30)

print(s1 + s2 + s3)

# Python program to overload
# a comparison operators

class A:
    def __init__(self, a):
        self.a = a
    def __gt__(self, other):
        if(self.a>other.a):
             return True
        else:
            return False
ob1 = A(2)
ob2 = A(3)
if(ob1>ob2):
    print("ob1 is greater than ob2")
else:
     print("ob2 is greater than ob1")

# Python program to overload equality
# and less than operators

class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if(self.a<other.a):
            return "ob1 is lessthan ob2"
        else:
            return "ob2 is less than ob1"
    def __eq__(self, other):
        if(self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"
ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)
ob3 = A(4)
ob4 = A(4)
print(ob1 == ob2)




