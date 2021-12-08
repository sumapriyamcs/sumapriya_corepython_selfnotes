

"""
  Super class       Sub class
  ================================
class SuperA:      class SubB:
  m1()              0                : Sub class will inherit method from super class
  m1()              m1()             : Sub class overriden inherited method
  m1() m2()         0                : Sub class inherits 2 super class methods
  m1() m2()         m3() m4()        : Sub class inherits 2 super class methods,its own 2 methods
  m1() m2()         m1()* m3() m4()  : Sub class inherits 2 super class methods,its own 2 methods
                                        overriden method m1()
                                        inherited method m2()
                                        own specific methods m3() m4()



    Water              Watercan
    =====================================================
    1. 2L of water      2L Can   -  OK
    2. 5L of water      5L Can   -  OK
    3. 2L of water      5L Can   -  OK      Memory wastage
    4. 5L of water      2L Can   - NOT OK   Data Loss

    class Employee:    # 5L can

    class SoftEmp(Employee):   # 2L can


        can    water
        --------------
     1. int x = 10       # 2L can <--- 2L water
     2. float x = 10.5   # 5L can <--- 5L water
     3. float x = 10     # 5L can <--- 2L water    # Implicit casting  ==> 10.0
 XX  4. int x = 10.5     # 2L can <--- 5L water    # Explicit casting  ==> 10    int x = (int)10.5


    Employee
      |  m1()
      |
    Software Employee
         m2()

    Capacity          Content
    --------------------------------------------
    1. SoftEmp emp  = SoftEmp(100, 'MadhuN', 15000)     2L Can  <--- 2L Water
    2. Employee emp = Employee(100, 'MadhuN', 15000)    5L Can  <--- 5L Water
    3. Employee emp = SoftEmp(100, 'MadhuN', 15000)     5L Can  <--- 2L Water   Memory loss # Upcasting
    4. SoftEmp emp  = Employee(100, 'MadhuN', 15000)    2L Can  <--- 5L Water   Data loss   # Downcasting




Specification

IEEE standards 

SoftEmp semp  = SoftEmp(100, 'MadhuN', 15000)
semp.m1()
semp.m2()

Employee emp  = Employee(100, 'MadhuN', 15000)
emp.m1()

SUPER CLASS:
============
As a sub class, use my super class methods AS IS   (or) 
                                           Override my super class method
                        but don't write your own methods

Employee emp = SoftEmp(100, 'MadhuN', 15000) 
emp.m1()
emp.m2()  # ERROR





# Python Program to call base class overridden method using super()
class Animal:
    def sound(self):
        print('Animal makes sound.')


class Dog(Animal):
    def sound(self):
        super().sound()
        print('Dog barks.')


d = Dog()
d.sound()


class P:
   def property(self):
        print('Gold+Land+Cash+Power')
   def marry(self):
        print('Appalamma')
class C(P):
   def marry(self):
        print('Katrina Kaif')

c=C()
c.property()
c.marry()

#From Overriding method of child class,we can call parent class method also by using super()
method.

class P:
   def property(self):
       print('Gold+Land+Cash+Power')
   def marry(self):
       print('Appalamma')
class C(P):
   def marry(self):
      super().marry()
      print('Katrina Kaif')

c=C()
c.property()
c.marry()

#Demo Program to call Parent class constructor by using super():

class Person:
     def __init__(self,name,age):
             self.name=name
             self.age=age
class Employee(Person):
     def __init__(self,name,age,eno,esal):
             super().__init__(name,age)
             self.eno=eno
             self.esal=esal

     def display(self):
         print('Employee Name:',self.name)
         print('Employee Age:',self.age)
         print('Employee Number:',self.eno)
         print('Employee Salary:',self.esal)

e1=Employee('Durga',48,872425,26000)
e1.display()
e2=Employee('Sunny',39,872426,36000)
e2.display()


# Python program to demonstrate
# calling the parent's class method
# inside the overridden method using
# super()


class Parent():

    def show(self):
        print("Inside Parent")


class Child(Parent):

    def show(self):
        # Calling the parent's class
        # method
        super().show()
        print("Inside Child")


# Driver's code
obj = Child()
obj.show()

# Inherited or Sub class (Note Parent in bracket)
class Child(Parent):

    # Child's show method
    def show(self):
        print("Inside Child")


# Inherited or Sub class (Note Child in bracket)
class GrandChild(Child):

    # Child's show method
    def show(self):
        print("Inside GrandChild")


# Driver code
g = GrandChild()
g.show()
g.display()

#How to call parent class static method from child class static method by using super():
class A:
    @staticmethod
    def m1():
        print('Parent static method')
class B(A):
   @staticmethod
   def m2():
   super(B,B).m1()

B.m2()

"""