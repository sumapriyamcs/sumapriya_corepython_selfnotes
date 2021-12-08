"""
#How to call method of a particular Super class

We can use the following approaches
1. super(D,self).m1()
It will call m1() method of super class of D.
2. A.m1(self)
It will call A class m1() method

"""
class A:
    def m1(self):
        print('A class Method')
class B(A):
    def m1(self):
         print('B class Method')
class C(B):
    def m1(self):

        print('C class Method')

class D(C):

    def m1(self):

        print('D class Method')

class E(D):

    def m1(self):
        A.m1(self)
e = E()
e.m1()

#From Class Method of Child class,how to call parent class instance
#methods and constructors:


class A:
     def __init__(self):
              print('Parent constructor')
     def m1(self):
          print('Parent instance method')
class B(A):
    @classmethod
    def m2(cls):
         super(B,cls).__init__(cls)
         super(B,cls).m1(cls)
B.m2()

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
#method overriding:?

Method overriding is an ability of any object-oriented programming language that allows
a subclass or child class to provide a specific implementation of a method that is
already provided by one of its super-classes or parent classes. When a method in a
subclass has the same name, same parameters or signature and same return type(or sub-type)
as a method in its super-class,then the method in the subclass is said to override
the method in the super-class.

"""
#example:

# Python program to demonstrate
# method overriding


# Defining parent class
class Parent():

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self.value)


# Defining child class
class Child(Parent):

    # Constructor
    def __init__(self):
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value)


# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()

"""
#Method overriding with multiple and multilevel inheritance
Multiple Inheritance: When a class is derived from more than one base class
it is called multiple Inheritance.
"""
# Python program to demonstrate
# overriding in multiple inheritance


# Defining parent class 1
class Parent1():

    # Parent's show method
    def show(self):
        print("Inside Parent1")


# Defining Parent class 2
class Parent2():

    # Parent's show method
    def display(self):
        print("Inside Parent2")


# Defining child class
class Child(Parent1, Parent2):

    # Child's show method
    def show(self):
        print("Inside Child")


# Driver's code
obj = Child()

obj.show()
obj.display()

#2.Multilevel Inheritance: When we have a child and grandchild relationship.


# Python program to demonstrate
# overriding in multilevel inheritance


# Python program to demonstrate
# overriding in multilevel inheritance


class Parent():

    # Parent's show method
    def display(self):
        print("Inside Parent")


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

"""
#Calling the Parent’s method within the overridden method:?

Parent class methods can also be called within the overridden methods.
This can generally be achieved by two ways.

Using Classname: Parent’s class methods can be called by using the Parent classname.
method inside the overridden method.

"""
# Python program to demonstrate
# calling the parent's class method
# inside the overridden method


class Parent():

    def show(self):
        print("Inside Parent")


class Child(Parent):

    def show(self):
        # Calling the parent's class
        # method
        Parent.show(self)
        print("Inside Child")


# Driver's code
obj = Child()
obj.show()

"""
*Using Super():

Python super() function provides us the facility to refer to the
parent class explicitly. It is basically useful where we have to call superclass functions.
It returns the proxy object that allows us to refer parent class by ‘super’.
"""
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


# Program to define the use of super()
# function in multiple inheritance
class GFG1:
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG1)')

    def sub_GFG(self, b):
        print('Printing from class GFG1:', b)


# class GFG2 inherits the GFG1
class GFG2(GFG1):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG2)')
        super().__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG2:', b)
        super().sub_GFG(b + 1)


# class GFG3 inherits the GFG1 ang GFG2 both
class GFG3(GFG2):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG3)')
        super().__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG3:', b)
        super().sub_GFG(b + 1)


# main function
if __name__ == '__main__':
    # created the object gfg
    gfg = GFG3()

    # calling the function sub_GFG3() from class GHG3
    # which inherits both GFG1 and GFG2 classes
    gfg.sub_GFG(10)


class Animal:
    # properties
    multicellular = True
    # Eukaryotic means Cells with Nucleus
    eukaryotic = True

    # function breathe
    def breathe(self):
        print("I breathe oxygen.")

    # function feed
    def feed(self):
        print("I eat food.")


class Herbivorous(Animal):

    # function feed
    def feed(self):
        print("I eat only plants. I am vegetarian.")
herbi = Herbivorous()
herbi.feed()
# calling some other function
herbi.breathe()


class Parent(object):
    def __init__(self):
        self.value = 4

    def get_value(self):
        return self.value


class Child(Parent):
    def get_value(self):
        return self.value + 1

c = Child()
c.get_value()


# Python Method Overriding

class Employee:

    def message(self):
        print('This message is from Employee Class')


class Department(Employee):

    def message(self):
        print('This Department class is inherited from Employee')


emp = Employee()
emp.message()

print('------------')
dept = Department()
dept.message()


class Employee:

    def message(self):
        print('This message is from Employee Class')


class Department(Employee):

    def message(self):
        print('This Department class inherited from Employee')


class Sales(Employee):

    def message(self):
        print('This Sales class is also inherited from Employee')


emp = Employee()
emp.message()

print('------------')
dept = Department()
dept.message()

print('------------')
sl = Sales()
sl.message()


#multiple inheretence
class Employee:

    def message(self):
        print('This message is from Employee Class')


class Department(Employee):

    def message(self):
        print('This Department class is inherited from Employee')


class Sales(Department):

    def message(self):
        print('This Sales class is inherited from Employee')


emp = Employee()
emp.message()

print('------------')
dept = Department()
dept.message()

print('------------')
sl = Sales()
sl.message()

#overriding with arguments
class Employee:

    def add(self, a, b):
        print('The Sum of Two = ', a + b)


class Department(Employee):

    def add(self,a,b,c):
        print('The Sum of Three = ', a + b + c)


emp = Employee()
emp.add(10, 20)

print('------------')
dept = Department()
dept.add(50, 130, 90)

#Calling Parent Function within the Method Overriding:?
class Employee:

    def message(self):
        print('This message is from Employee Class')


class Department(Employee):

    def message(self):
        Employee.message(self)
        print('This Department class is inherited from Employee')


emp = Employee()
emp.message()

print('------------')
dept = Department()
dept.message()

"""
#Instead of using the class name, you can use the super() function
to call the parent class method.
"""
class Employee:

    def message(self):
        print('This message is from Employee Class')


class Department(Employee):

    def message(self):
        super().message()
        print('This Department class is inherited from Employee')


emp = Employee()
emp.message()

print('------------')
dept = Department()
dept.message()


# Python program to implement method overriding
class Animal:
    def sound(self):
        print('Animal makes sound.')


class Dog(Animal):
    def sound(self):
        print('Dog barks.')


d = Dog()
d.sound()


# Python Program to call base class overridden method using class name
class Animal:
    def sound(self):
        print('Animal makes sound.')


class Dog(Animal):
    def sound(self):
        Animal.sound(self)
        print('Dog barks.')


d = Dog()
d.sound()


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
#method.

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

#Demo Program for Constructor overriding:

class P:
    def __init__(self):
       print('Parent Constructor')
class C(P):
    def __init__(self):
        print('Child Constructor')
c=C()

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




