"""
Inheritance Types:
-------------------
Simple / Single  : Super 1 , Sub 1
Multi level      : Super 1, Sub 1,  SubSub 1
Hierarchial      : Super 1,  Sub 2 or more
Hybrid           : Comb of multi level + Hierarchial
Multiple**       : One sub class with 2 or more super classes

# Simple / Single  : Super 1 Sub 1

A
|
B

print("-----------1. Simple Inheritance----------")


class A:
    def m1(self):
        print("A m1()")


class B(A):
    def m2(self):
        print("B m2()")



B class has 2 methods - m1() inherited method
                      - m2() its own method


print("-----------2. Multi level Inheritance----------")

# Multi level Inheritance      : Super 1 Sub 1  SubSub 1

A     Polygon
|
B       Quadrilateral
|
C            Square



class A:
    def m1(self):
        print("A m1()")


class B(A):
    def m2(self):
        print("B m2()")


class C(B):
    def m3(self):
        print("C m3()")



C has 3 behaviors - m1() inherited method from A
                  - m2() inherited method from B
                  - m3() its own method
'''
a = A()
a.m1()
# a.m2()  # ERROR

b = B()
b.m1()
b.m2()
# b.m3() # ERROR

c = C()
c.m1()
c.m2()
c.m3()
# c.m4()  # ERROR

print("-----------3. Hierarchial Inheritance----------")

# Hierarchial      : Super 1 Sub 2 or more

   A
/  |  \
B  C   D   




class A:
    def m1(self):
        print("A m1()")


class B(A):
    def m2(self):
        print("B m2()")


class C(A):
    def m3(self):
        print("B m3()")


print("-----------4. Hybrid Inheritance----------")

# Hybrid           : Comb of multi level + Hierarchial
'''
     A 
     |
     B
    / \
   C   D    
  /     \ 
  E     F
'''

print("-----------5. Multiple Inheritance----------")

# Multiple  **       : One sub class with 2 or more super classes
'''
  A     B
   \   / 
     C
'''


class A:
    def m1(self):
        print("A m1()")


class B:
    def m2(self):
        print("B m2()")


class C(A, B):  # Order of precendence is first A,then B
    def m3(self):
        print("C m3()")


'''
C has 3 behaviors   - m1()  inherited from A
                    - m2()  inherited from B
                    - m3()  speicific or own method
'''

c = C()
c.m1()
c.m2()
c.m3()

print("--------Problem with mulitple inheritance---------")


class A:
    def m1(self):
        print("A m1()")


class B:
    def m1(self):
        print("B m1()")


# method resolution order principle
class C(A, B):  # MRO principle Left --> Right
    def m3(self):
        print("C m3()")


c = C()
c.m3()
c.m1()


class A:
    a = 100

    def __init__(self):
        print("in A init method")

    def m1(self):
        print("A - m1() method")

    def download_file(self):
        print("A - download_file() method ==> pdf ")


class B(A):
    def __init__(self):
        A.__init__(self)  # first initialize super class state **
        print("in B init method")

    def m3(self):
        print("B - m3() method")

    def download_file(self):  # Method overriding
        print("B - download_file() method ==> excel ")


b = B()
b.m1()
b.download_file()
b.m3()
# b.m4()

'''
a = A()
a.m1()
a.m2()
#a.m3()
'''
print("-------Simple inheritance--------------")


class A:
    def m1(self):
        print("A m1()")

    def a(self):
        print("A a()")


class B(A):
    def m1(self):  # Method overriding
        print("B m1()")

    def m2(self):
        print("B m2()")


b = B()
b.m1()
b.m2()
b.a()

print("--------Multi level inheritance-----------------")


class A:
    def m1(self):
        print("A m1()")

    def a(self):
        print("A a()")


class B(A):
    def m1(self):
        print("B m1()")

    def m2(self):
        print("B m2()")


class C(B):
    def m3(self):
        print("C m3()")


c = C()
c.m1()
c.m2()
c.a()
c.m3()
print(c)  # c.__str__()

print("--------Multiple inheritance-----------------")


class A:
    def m1(self):
        print("A m1()")


class B:
    def m1(self):
        print("B m1()")


class C(B, A):  # MRO - Method Resolution Order*
    pass


c = C()
c.m1()

'''
diamond problem
   A 
 B    C
   D 
'''

'''
#single inheritence:

class P:
   def m1(self):
     print("Parent Method")
class C(P):
   def m2(self):
      print("Child Method")
c=C()
c.m1()
c.m2()


class Parent:
    def func1(self):
        print("this is function one")


class Child(Parent):
    def func2(self):
        print(" this is function 2 ")


ob = Child()
ob.func1()
ob.func2()

#multilevel inheritence
class Animal:
    def speak(self):
        print("Animal Speaking")
#The child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("dog barking")
#The child class Dogchild inherits another child class Dog
class DogChild(Dog):
    def eat(self):
        print("Eating bread...")
d = DogChild()
d.bark()
d.speak()
d.eat()


class P:
   def m1(self):
     print("Parent Method")
class C(P):
   def m2(self):
      print("Child Method")
class CC(C):
    def m3(self):
      print("Sub Child Method")
c=CC()
c.m1()
c.m2()
c.m3()


#Hierarchical Inheritance:

class P:
    def m1(self):
        print("Parent Method")
class C1(P):
    def m2(self):
       print("Child1 Method")
class C2(P):
    def m3(self):
print("Child2 Method")
c1=C1()
c1.m1()
c1.m2()
c2=C2()
c2.m1()
c2.m3()


#multiple inheritence:
class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d = Derived()
print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20)

class P1:
   def m1(self):
      print("Parent1 Method")
class P2:
    def m2(self):
       print("Parent2 Method")
class C(P1,P2):
    def m3(self):
       print("Child2 Method")
c=C()
c.m1()
c.m2()
c.m3()


class P1:
    def m1(self):
        print("Parent1 Method")
class P2:
     def m1(self):
         print("Parent2 Method")
class C(P1,P2):
     def m2(self):
        print("Child Method")
c=C()
c.m1()
c.m2()

#Hybrid Inheritance:

# Creating a Base class named University:
class University:
  def __init__(self):
    print("Contructor of the Base class")
    # Initializing a class variable named univ to store university name:
    self.univ = "MIT"
  def display(self):  # Method to print the University Name:
    print(f"The University name is: {self.univ}")

# 1st Derived or Child Class of University Class:
class Course(University):
  def __init__(self):
    # using "super" keyword to access members of the parent class having same name:
    print("Constructor of the Child Class 1 of Class University")
    University.__init__(self)
    self.course = "CSE"
  def display(self):  # Method to print the Course Name:
    # using "super" keyword to access display method defined in the parent class:
    print(f"The Course name is: {self.course}")
    University.display(self)

# 2nd Derived or Child Class of University Class:
class Branch(University):
  def __init__(self):
    print("Constructor of the Child Class 2 of Class University")
    self.branch = "Data Science"
  def display(self):  # Method to print the Branch Name:
    print(f"The Branch name is: {self.branch}")

# Derived or Child Class of Class Course and Branch:
class Student(Course, Branch):
  def __init__(self):
    print("Constructor of Child class of Course and Branch is called")
    self.name = "Tonny"
    Branch.__init__(self)
    Course.__init__(self)
  def display(self):
    print(f"The Name of the student is: {self.name}")
    Branch.display(self)
    Course.display(self)

# Object Instantiation:
ob = Student()  # Object named ob of the class Student.
print()
ob.display()    # Calling the display method of Student class.


class GrandPa:
    def __init__(self):
        print("Grand Pa")

class Father(GrandPa):
    def __init__(self):
        super().__init__()
        print("Father")

class Mother(GrandPa):
    def __init__(self):
        super().__init__()
        print("Mother")


class child(Father, Mother):
    def __init__(self):
        super().__init__()
        print("Child")

c = child()

#hybrid inheritance example with init method:?
# creating parent class
class Parent:
    BloodGroup = 'A'
    Gender = 'Male'
    Hobby = 'Chess'


# creating child class
class Child(Parent):  # inheriting parent class
    BloodGroup = 'A+'
    Gender = 'Female

    def print_data():
        print(BloodGroup, Gender, Hobby)


# creating object for child class
child1 = Child()
# as child1 inherits it's parent's hobby printed data would be it's parent's
child1.print_data()
"""
