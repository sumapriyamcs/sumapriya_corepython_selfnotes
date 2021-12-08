"""

#Method overriding:

What ever members available in the parent class are bydefault available to the child class through
inheritance. If the child class not satisfied with parent class implementation then child class is
allowed to redefine that method in the child class based on its requirement. This concept is called
overriding.
Overriding concept applicable for both methods and constructors.

"""

#Program for Method overriding:

class P:
    def property(self):
        print('Gold+Land+Cash+Power')
    def marry(self):
        print('PRIYA')
class C(P):
    def marry(self):
         print('SUMA')
c=C()
c.property()
c.marry()

#From Overriding method of child class,we can call parent class method also by using super() method.

class P:
    def property(self):
        print('Gold+Land+Cash+Power')
    def marry(self):
        print('PRIYA')
class C(P):
    def marry(self):
        super().marry()
        print('SUMA')
c=C()
c.property()
c.marry()

#Program for Constructor overriding:

class P:
    def __init__(self):
        print('Parent Constructor')
class C(P):
    def __init__(self):
        print('Child Constructor')
c=C()

#Program to call Parent class constructor by using super():

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
