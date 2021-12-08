print(
    "------1.Normal Inheritance: - 1.1 - Reuse super class methods  AS IS-------")


class A:

    def m1(self):
        print("A  m1()")

    def m2(self):
        print("A  m2()")


class B(A):
    def m3(self):
        print("B  m3()")


b = B()
b.m1()
b.m2()
b.m3()

print("------1.Normal Inheritance: - 1.2 Override super class methods--------")


class A:
    def m1(self):
        print("A  m1()")  # method implementation/method body

    def m2(self):
        print("A  m2()")


class B(A):
    def m1(self):
        print("B  m1()")  # my own implementation

    def m2(self):  # my own implementation
        print("B  m2()")

    def m3(self):
        print("B m3()")


b = B()
b.m1()
b.m2()
b.m3()

print(
    "------1.Normal Inheritance: - 1.3 Few Super classmeethods AS IS, few unique--------")


class A:
    def m1(self):  # Required AS IS in sub class
        print("A  m1()")

    def m2(self):  # Required in unique way in sub class
        print("A  m2()")


class B(A):
    def m3(self):
        print("B  m3()")


b1 = B()
b1.m1()
b1.m2()
b1.m3()


class Pendrive:
    def usb_mesaure(self):
        print("Pendrive  m1()")


class Kingston(Pendrive):
    def usb_mesaure(self):
        print("Pendrive  my own design")


k = Kingston()
k.usb_mesaure()

'''
  1. 2L of Can <== 2L water - YES
  2. 5L of Can <== 5L water - YES
  3. 5L of Can <== 2L water - YES  (Memory Loss)  90%
  4. 2L of Can <== 5L water - NO  (Data Loss) 
x = 10
int x = 10
'''
'''
class Animal:
    def m1()

class Tiger(Animal):
    def m2()

Tiger tiger = new Tiger()    # 1    tiger.m1()
                                    tiger.m2()

Animal animal = new Animal() # 2    animal.m1()

Animal animal = new Tiger()  # 3**    animal.m1()
                                      animal.m2()  ==> Will give error


Tiger tiger = new Animal()   # 4    Error Downcasting



x = 10
print(x)  - 10
x = 10.5
print(x)  - 10.5

int x   = 10     # 1
float x = 10.5   # 2
float x = 10     # 3 Implicit casting   ==> float x = (float)10(internally converts)
int x = 10.5  XX # 4 Explict casting    ==> int x = (int)10.5 (externally you have to write)

'''

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


# Python program to demonstrate
# single inheritance


# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class
class Child(Parent):
	def func2(self):
		print("This function is in child class.")

# Driver's code
object = Child()
object.func1()
object.func2()


# Parent class created
class Parent:
    parentname = ""
    childname = ""

    def show_parent(self):
        print(self.parentname)


# Child class created inherits Parent class
class Child(Parent):
    def show_child(self):
        print(self.childname)


ch1 = Child()  # Object of Child class
ch1.parentname = "Mark"  # Access Parent class attributes
ch1.childname = "John"
ch1.show_parent()  # Access Parent class method
ch1.show_child()  # Access Child class method


class Parent():
    def first(self):
        print('Parent function')


class Child(Parent):
    def second(self):
        print('Child function')


object1 = Child()
object1.first()
object1.second()


class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages


    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"



harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Programmer("Shubham", 555, "Programmer", ["python"])
karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])
print(karan.no_of_holiday)

