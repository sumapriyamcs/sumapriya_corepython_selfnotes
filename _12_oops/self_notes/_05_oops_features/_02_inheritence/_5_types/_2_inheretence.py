'''

http://www.python-course.eu/python3_inheritance.php
http://www.python-course.eu/inheritance_example.php
'''
"""
                    Polygon
                       p1()
     Triangle                   Quadrilateral                         Petagon Hexagon 
        t1()                        q1()   
    ET      RA    IS         Square Rhombus Rectangle Parll 
    e1()    r1()  i1()       s1()   r1()    re1()      pa1()

Sub class ---is a -- super class
RA is a Polygon 
RA is a Triangle 
R  is a Polygon 
R  is a Qaudrilateral
Re is a Polygon 
Re is a Quadrilateral
Re is a Pentagon

wrt Polygon
Polygon is super class
T Q P H are sub classes wrt Polygon 

wrt to Triangle 
Triangle is super class
E RA Is sub classes of Triangle
E RA Is sub classes of Polygon

    Employee:
        get_emp_deatails()
PermaE       ContrE 
 get_pf()       get_gratuity()



Student

Office 



Super/Parent/Base  class
Sub/Child/Derived  class

                    Pentagon
                       m1()         
        Triangle Quarilateral Pentagon Hexagon 




class Employee:

    def __init__(self, eid, name):
        self.eid = eid
        self.name = name

    def get_emp_details(self):
        print("In Super Class : get_emp_details()")

    def get_info(self):
        print("In Super class : get_info()")


class SoftwareEmployee(Employee):  # IS - A

    def __init__(self, eid, name, sal):
        Employee.__init__(self, eid,
                          name)  # super().__init__(self, fName, lName)
        self.sal = sal

    def get_sw_emp_details(self):
        print("-------In Sub Class : get_sw_emp_deetailsI()-------------")


madhu = Employee(100, 'Madhu N')
madhu.get_emp_details()
madhu.get_info()
madhu1 = SoftwareEmployee(101, 'N Madhu', 20000)

madhu = SoftwareEmployee(11, "Madhu Nettem", 1000)
print("*******************************")
madhu.get_sw_emp_details()
madhu.get_emp_details()
madhu.get_info()

pavan = Employee(110, "Pavan Kumar Balla")

pavan.get_emp_details()

print("Object   content is ", pavan)
print("Object   content is ", pavan.__str__())
print("Damu ojbect ", pavan.__str__())
gopi = Employee(111, "Gopi")

# print("Adding 2 objects of employee ", pavan + gopi)    #damu.__add__(gopi)


madhu.get_emp_details()
print("*******************************")
print("Type ", type(madhu))

dict1 = {1: 1, 2: 2}
print("fdasfs", dict1.values())


Inheritance Types :
------------------------
1. Simple Inheritance      Super class <---- Sub class
2. Multilevel Inheritance  Super class <---- Sub class  <---- Sub class
3. Hierarchial Inhiertance               Super class 
                                    SubClass    SubClass SubClass  

4. Mulitple Inheritance **     SuperClass   SuperClass
                                        SubClass

5. Hybrid Inheritance 
                                        S      S 
                                            S
                                        S      S 

     
#MRO - Method Resolution order
# Mulitiple Inheritance  
         A        B
         m1()     m2()   
              C
             m3()



print("----------Mulitiple Inheritance ---------")


class A:
    def m1(self):
        print("In A")


class B:
    def m2(self):
        print("In B")


class C(A, B):
    def m3(self):
        print("In C")


c = C()
c.m3()
c.m1()
c.m2()

print(C.mro())


class Father:
    def m1(self):
        print("Father : m1()")


class Mother:
    def m2(self):
        print("Mother : m2()")


class Son(Mother, Father):
    def m3(self):
        print("Son  : m3()")


s = Son()
s.m3()
s.m1()
s.m2()

# MRO  Method Resolution Order

     Father     Mother
        m1()       m1()

            Son 



class Father:
    def m1(self):
        print("Father : m1()")


class Mother:
    def m1(self):
        print("Mother : m2()")


class Son(Father, Mother):
    def m3(self):
        print("Son  : m3()")

    '''
    def m1(self):
        print("Son  : m1()")
    '''


s = Son()
s.m3()
s.m1()
print(Son.mro())

'''
    Animal :
      move():

    Cat         Dog           Snake      Tiger        
    move():      move():    move():    move():

# Normal Class
 For a method ( m1() ), the impl. is common for all sub classes

# Abstract class
Few methods need to be implemented in common way for all sub classes 
Other methods need to be implemented in unique way for all sub classes 

# Interface
For a method ( m1() ), the impl. is unique  for each sub class

'''
 Python program to demonstrate
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

#overriding with orguments
class Employee:

    def add(self, a, b):
        print('The Sum of Two = ', a + b)


class Department(Employee):

    def add(self, a, b, c):
        print('The Sum of Three = ', a + b + c)


emp = Employee()
emp.add(10, 20)

print('------------')
dept = Department()
dept.add(50, 130, 90)

# Python program to implement method overriding
class Animal:
    def sound(self):
        print('Animal makes sound.')


class Dog(Animal):
    def sound(self):
        print('Dog barks.')


d = Dog()
d.sound()

"""