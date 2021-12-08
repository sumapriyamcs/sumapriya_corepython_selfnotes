
#inheritence:

"""Inheritance is the capability of one class to derive or inherit the properties from another class.

The benefits of inheritance are
1.It represents real-world relationships well.

2.It provides reusability of a code. We don’t have to write the same code again and again.
Also, it allows us to add more features to a class without modifying it.

3.It is transitive in nature, which means that if class B inherits from another class A,
then all the subclasses of B would automatically inherit from class A.


# forms of Inheritance:

1. Single inheritance: When a child class inherits from only one parent class,
it is called single inheritance.


2. Multiple inheritance: When a child class inherits from multiple parent classes,
it is called multiple inheritance.

3. Multilevel inheritance: When we have a child and grandchild relationship.

4. Hierarchical inheritance: More than one derived classes are created from a single base.

5. Hybrid inheritance: This form combines more than one form of inheritance.
Basically, it is a blend of more than one type of inheritance.

Using members of one class inside another class:
We can use members of one class inside another class by using the following ways
1. By Composition (Has-A Relationship)
2. By Inheritance (IS-A Relationship)
1. By Composition (Has-A Relationship):
By using Class Name or by creating object we can access members of one class inside another class
is nothing but composition (Has-A Relationship).
The main advantage of Has-A Relationship is Code Reusability.

example:
class Engine:
    a=10
    def __init__(self):
       self.b=20
    def m1(self):
       print('Engine Specific Functionality')
class Car:
   def __init__(self):
       self.engine=Engine()
   def m2(self):
      print('Car using Engine Class Functionality')
      print(self.engine.a)
      print(self.engine.b)
      self.engine.m1()
c=Car()
c.m2()

example2:


class Car:
   def __init__(self,name,model,color):
       self.name=name
       self.model=model
       self.color=color
   def getinfo(self):
       print("Car Name:{} , Model:{} and Color:{}".format(self.name, self.model,self.color))
class Employee:
    def __init__(self, ename, eno, car):
        self.ename = ename
        self.eno = eno
        self.car = car
    def empinfo(self):
        print("Employee Name:", self.ename)
        print("Employee Number:", self.eno)
        print("Employee Car Info:")
        self.car.getinfo()
c = Car("Innova", "2.5V", "Grey")
e = Employee('Durga', 10000, c)
e.empinfo()


example3:

class X:
  a=10
  def __init__(self):
     self.b=20
  def m1(self):
     print("m1 method of X class")
class Y:
   c=30
  def __init__(self):
     self.d=40
  def m2(self):
     print("m2 method of Y class")
  def m3(self):
     x1=X()
     print(x1.a)
     print(x1.b)
     x1.m1()
     print(Y.c)
     print(self.d)
     self.m2()
     print("m3 method of Y class")
y1=Y()
y1.m3()

2.By Inheritance(IS-A Relationship):


What ever variables, methods and constructors available in the parent class by
default available to the child classes and we are not required to rewrite.
Hence the main advantage of inheritance is Code Reusability and we can extend existing
functionality with some more extra functionality.

#Syntax :
class childclass(parentclass):

example:

class P:
    a = 10
    def __init__(self):
        self.b = 10
    def m1(self):
        print('Parent instance method')
    @classmethod

     def m2(cls):
        print('Parent class method')
    @staticmethod

    def m3():
        print('Parent static method')
class C(P):
    pass
c = C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()


#IS-A vs HAS-A Relationship::


If we want to extend existing functionality with some more extra functionality then we should go
for IS-A Relationship

If we dont want to extend and just we have to use existing functionality then we should go for
HAS-A Relationship
"""

#single inheritence:

"""
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







