"""
The process of wrapping up variables and methods into a single entity is known as Encapsulation.
It is one of the underlying concepts in object-oriented programming (OOP).
It acts as a protective shield that puts restrictions on accessing variables
and methods directly, and can prevent accidental or unauthorized modification of data.
Encapsulation also makes objects into more self-sufficient, independently functioning pieces.

Access modifiers

Access modifiers limit access to the variables and functions of a class.
Python uses three types of access modifiers; they are - private, public and protected.

Public members
Public members are accessible anywhere from the class.
All the member variables of the class are by default public.
"""
# program to illustrate public access modifier in a class

class edpresso:
    # constructor
    def __init__(self, name, project):
        self.name = name;
        self.project = project;

    def displayProject(self):
        # accessing public data member
        print("Project: ", self.project)

# creating object of the class
edp = edpresso("TeamPhoenix", 1);

# accessing public data member
print("Name: ", edp.name)

# calling public member function of the class
edp.displayProject()

"""
Protected members
Protected members are accessible within the class and also available to its sub-classes.
To define a protected member, prefix the member name with a single underscore “_”.

"""

# program to illustrate protected access modifier in a class

class edpresso:
    def __init__(self, name, project):
        self._name = name
        self._project = project

# creating object of the class
edp = edpresso("TeamPhoenix", 2)

# direct access of protected member
print("Name:",edp._name)
print("project:",edp._project)

"""
Private members
Private members are accessible within the class.
To define a private member, prefix the member name with a double underscore “__”.


"""

# program to illustrate private access modifier in a class

class edpresso:
   def __init__(self, name, project):
      # public variable
      self.name = name
      # private variable
      self.__project = project

# creating an instance of the class Sample
edp = edpresso('TeamPhoenix', 3)

# accessing public variable name
print("Name:",edp.name)

# accessing private variable __project using
# _Edpresso__project name
print("Project:",edp._edpresso__project)

#protected members
# Python program to
# demonstrate protected members


# Creating a base class
class Base:
    def __init__(self):
        # Protected member
        self._a = 2


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Outside class will  result in
# AttributeError
print(obj2.a)

#private members
# Python program to
# demonstrate private members

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class

class Employee:
    # STATE --> data members  *  logical
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    # BEHAVIOR --> member methods   * physical
    def get_details(self):
        print("Employee details")

# Employee.get_details()
obj = Employee(1001,'priya p',10000)   # data physical methods logical
obj.get_details()



