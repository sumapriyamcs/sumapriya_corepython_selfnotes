"""
#Create Instance Variables:

Instance variables are declared inside a method using the self keyword.
We use a constructor to define and initialize the instance variables.

"""

1.
class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create first object
s1 = Student("Jessa", 20)

# access instance variable
print('Object 1')
print('Name:', s1.name)
print('Age:', s1.age)

# create second object
s2= Student("Kelly", 10)

# access instance variable
print('Object 2')
print('Name:', s2.name)
print('Age:', s2.age)

#modifying instance variables

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create object
stud = Student("Jessa", 20)

print('Before')
print('Name:', stud.name, 'Age:', stud.age)

# modify instance variable
stud.name = 'Emma'
stud.age = 15

print('After')
print('Name:', stud.name, 'Age:', stud.age)

#accessing instance variables:
class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method access instance variable
    def show(self):
        print('Name:', stud.name, 'Age:', stud.age)

# create object
stud = Student("Jessa", 20)

# call instance method
stud.show()

#accessing instance variables by using getattr():

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create object
stud = Student("Jessa", 20)

# Use getattr instead of stud.name
print('Name:', getattr(stud, 'name'))
print('Age:', getattr(stud, 'age'))

#dynamically add instance  variable to object?

class Student:
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create object
stud = Student("Jessa", 20)

print('Before')
print('Name:', stud.name, 'Age:', stud.age)

# add new instance variable 'marks' to stud
stud.marks = 75
print('After')
print('Name:', stud.name, 'Age:', stud.age, 'Marks:', stud.marks)

#dynamically delete instance variable:?

class Student:
    def __init__(self, roll_no, name):
        # Instance variable
        self.roll_no = roll_no
        self.name = name

# create object
s1 = Student(10, 'Jessa')
print(s1.roll_no, s1.name)

# del name
del s1.name
# Try to access name variable
print(s1.name)

#by using delattr() function:?

class Student:
    def __init__(self, roll_no, name):
        # Instance variable
        self.roll_no = roll_no
        self.name = name

    def show(self):
        print(self.roll_no, self.name)

s1 = Student(10, 'Jessa')
s1.show()

# delete instance variable using delattr()
delattr(s1, 'roll_no')
s1.show()

#access instance variable  from another class:?
class Vehicle:
    def __init__(self):
        self.engine = '1500cc'

class Car(Vehicle):
    def __init__(self, max_speed):
        # call parent class constructor
        super().__init__()
        self.max_speed = max_speed

    def display(self):
        # access parent class instance variables 'engine'
        print("Engine:", self.engine)
        print("Max Speed:", self.max_speed)

# Object of car
car = Car(240)
car.display()

#list all istance variables of a object
class Student:
    def __init__(self, roll_no, name):
        # Instance variable
        self.roll_no = roll_no
        self.name = name

s1 = Student(10, 'Jessa')
print('Instance variable object has')
print(s1.__dict__)

# Get each instance variable
for key_value in s1.__dict__.items():
    print(key_value[0], '=', key_value[1])


#class variable
class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 5

new_shark = Shark()
print(new_shark.animal_type)
print(new_shark.location)
print(new_shark.followers)


class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age

new_shark = Shark("Sammy", 5)

#class variable similarly call to print instant variable
class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age

new_shark = Shark("Sammy", 5)
print(new_shark.name)
print(new_shark.age)

class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age

new_shark = Shark("Sammy", 5)
print(new_shark.name)
print(new_shark.age)

stevie = Shark("Stevie", 8)
print(stevie.name)
print(stevie.age)
"""
2.Instance methods

In Object-oriented programming, we use instance methods and class methods.
Inside a Class, we can define the following three types of methods.

1.Instance method:
Used to access or modify the object state. If we use instance variables inside a method, such methods are called instance methods. It must have a self parameter to refer to the current object.

2.Class method: Used to access or modify the class state. In method implementation,
if we use only class variables, then such type of methods we should declare
as a class method. The class method has a cls parameter which refers to the class.

3.Static method: It is a general utility method that performs a task in isolation.
Inside this method, we don’t use instance or class variable because this static
method doesn’t take any parameters like self and cls.

#Instance method in Python

A class is a user-defined blueprint or prototype from which objects are created.
Classes provide a means of bundling data and functionality together.
Creating a new class creates a new type of object, allowing new instances of that type to be made.
Each class instance can have attributes attached to it for maintaining its state.
Class instances can also have methods (defined by its class) for modifying its state.

#Instance Method

Instance attributes are those attributes that are not shared by objects. Every object
has its own copy of the instance attribute.
For example, consider a class shapes that have many objects like circle, square,
triangle, etc. having its own attributes and methods. An instance attribute refers to the
properties of that particular object like edge of the triangle being 3, while the edge of
the square can be 4.An instance method can access and even modify the value of attributes
of an instance.

#It has one default parameter:-

self – It is a keyword which points to the current passed instance. But it need not be
passed every time while calling an instance method.

"""
class shape:
# Instance Method

     def finEdges(self):
      return self.edge

# Instance Method

     def modifyEdges(self, newedge):
      self.edge = newedge
# Driver Code
circle = shape(0, 'red')
square = shape(4, 'blue')
# Calling Instance Method
print("No. of edges for circle: "+ str(circle.finEdges()))
# Calling Instance Method
square.modifyEdges(6)
print("No. of edges for square: "+ str(square.finEdges()))


# Python program to demonstrate
# classes

class Person:

    # init method or constructor
    def _init_(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Nikhil')
p.say_hi()


class Employee:
    # local variables   - eid, name, sal
    # instance variables - self.eid self.name self.sal - instance variables

    def _init_(self, eid, name, sal):
        print("Self address : ", self)
        self.eid = eid
        self.name = name
        self.sal = sal

    # instance methods
    def get_edata(self):
        print("Employee information : ", self.eid, self.name, self.sal)


suma = Employee(100, 'yeswanth', 15000)
suma.get_edata()  # Employee.get_edata(madhu)


#instance methods
class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method to access instance variable
    def show(self):
        print('Name:', self.name, 'Age:', self.age)

#calling instance method
class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method access instance variable
    def show(self):
        print('Name:', self.name, 'Age:', self.age)

# create first object
print('First Student')
emma = Student("Jessa", 14)
# call instance method
emma.show()

# create second object
print('Second Student')
kelly = Student("Kelly", 16)
# call instance method
kelly.show()

#Modify Instance Variables inside Instance Method

class Student:
    def __init__(self, roll_no, name, age):
        # Instance variable
        self.roll_no = roll_no
        self.name = name
        self.age = age

    # instance method access instance variable
    def show(self):
        print('Roll Number:', self.roll_no, 'Name:', self.name, 'Age:', self.age)

    # instance method to modify instance variable
    def update(self, roll_number, age):
        self.roll_no = roll_number
        self.age = age

# create object
print('class VIII')
stud = Student(20, "Emma", 14)
# call instance method
stud.show()

# Modify instance variables
print('class IX')
stud.update(35, 15)
stud.show()

#Create Instance Variables in Instance Method?
class Student:
    def __init__(self, roll_no, name, age):
        # Instance variable
        self.roll_no = roll_no
        self.name = name
        self.age = age

    # instance method to add instance variable
    def add_marks(self, marks):
        # add new attribute to current object
        self.marks = marks

# create object
stud = Student(20, "Emma", 14)
# call instance method
stud.add_marks(75)

# display object
print('Roll Number:', stud.roll_no, 'Name:', stud.name, 'Age:', stud.age, 'Marks:', stud.marks)

#Dynamically Add Instance Method to a Object?
import types

class Student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def show(self):
        print('Name:', self.name, 'Age:', self.age)

# create new method
def welcome(self):
    print("Hello", self.name, "Welcome to Class IX")


# create object
s1 = Student("Jessa", 15)

# Add instance method to object
s1.welcome = types.MethodType(welcome, s1)
s1.show()

# call newly added method
s1.welcome()

#dynamically delete instance methods
class Student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def show(self):
        print('Name:', self.name, 'Age:', self.age)

    # instance method
    def percentage(self, sub1, sub2):
        print('Percentage:', (sub1 + sub2) / 2)

emma = Student('Emma', 14)
emma.show()
emma.percentage(67, 62)

# Delete the method from class using del operator
del emma.percentage

# Again calling percentage() method
# It will raise error
emma.percentage(67, 62)

"""
# classmethod() in Python:

The classmethod() is an inbuilt function in Python, which returns a class method
for a given function.

Syntax: classmethod(function)


Parameter :This function accepts the function name as a parameter.
Return Type:This function returns the converted class method.
Syntax:

@classmethod
   def fun(cls, arg1, arg2, ...):


   Where,

fun: the function that needs to be converted into a class method
returns: a class method for function.
classmethod() methods are bound to a class rather than an object.
Class methods can be called by both class and object.
These methods can be called with a class or with an object.
We use @classmethod decorator in python to create a class method
and we use @staticmethod decorator
to create a static method in python.


"""
#Example 1: Create a simple classmethod:

class geeks:
    course = 'DSA'

    def purchase(obj):
        print("Puchase course : ", obj.course)


geeks.purchase = classmethod(geeks.purchase)
geeks.purchase()


#Example 2: Create class method using classmethod():

# Python program to understand the classmethod

class Student:

    # create a variable
    name = "Geeksforgeeks"

    # create a function
    def print_name(obj):
        print("The name is : ", obj.name)


# create print_name classmethod
# before creating this line print_name()
# It can be called only with object not with class
Student.print_name = classmethod(Student.print_name)

# now this method can be called as classmethod
# print_name() method is called a class method
Student.print_name()

#Example 3: Factory method using Class method:

# Python program to demonstrate
# use of a class method and static method.
from datetime import date

class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    def display(self):
        print("Name : ", self.name, "Age : ", self.age)

person = Person('mayank', 21)
person.display()
"""


#The @classmethod Decorator:

The @classmethod decorator is a built-in function decorator which is an expression that gets
evaluated after your function is defined. The result of that evaluation shadows your
function definition.A class method receives the class as the implicit first argument,
just like an instance method receives the instance.

Syntax:

class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):
       ....


Where,

fun: the function that needs to be converted into a class method
returns: a class method for function.

"""


# Python program to demonstrate
# use of a class method and static method.
from datetime import date

class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a
    # Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))

class Class:
    pass
    # STATE
        # ==> Fields(1,2)  which represents data
"""

        1. Class variables
        2. Instance variables
        3. local variables

    # BEHAVIOR
        # ==> Methods which represents implementation

       1. Class Method
       2. Instance Method
       3. Static method
"""


# Get employee count at a given point of time.


class Employee:
    comp = 'ORACLE'  # sharing
    emp_count = 0  # sharing + Modifying

    def _init_(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal
        Employee.emp_count += 1

    # instance method(can access instance,class variables)
    def get_edata(self):
        print("Employee information : ", self.eid, self.name, self.sal)

    # class method (can access only class variables)
    @classmethod
    def get_ecount(cls):
        print("Employee count : ", cls.comp, " -- ", cls.emp_count)


Employee.get_ecount()
suma = Employee(100, 'suma', 10000)
suma.get_edata()  # instance method ==> Employee.get_edata(madhu)
Employee.get_ecount()  # class method    ==> Employee.get_ecount(Employee)

# To call class method, we can call using object,But don't do it.
# suma.get_ecount()

yeswanth = Employee(101, 'yeswanth puchalapalli', 20000)
yeswanth.get_edata()
Employee.get_ecount()

ravi = Employee(102, 'ravi kumar', 45000)
yeswanth.get_edata()
Employee.get_ecount()

"""
btech : stu_id, name, marks ==> instance variables
        college name        ==> class variables(share)
        attendance          ==> class variable (share+Modify)


employees : eid,name,sal   Instance vars  UNIQUE(INDIVIDUAL DATA)
            comp_name      class vars     SHARABLE to all employees
            emp_count      class vars     SHARABLE + MODIFY
            attendance     class vars     SHARABLE + MODIFY



class variables    : data which is sharable to all objects
                     data which is SHARE + MODIFY actions
class methods      : 1. To act only on class variables


instance variables : data is unique for each object
instance methods   : 1. To act only on instance variables OR
                     2. Both instance and class variables



CV   - ClassMethod, InstanceMethod
IV   - InstanceMethod


"""

#class method?
#Example 1: Create class method using classmethod()

class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)

# create printAge class method
Person.printAge = classmethod(Person.printAge)

Person.printAge()

#How the class method works for the inheritance?

from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex = 'Male'

man = Man.fromBirthYear('John', 1985)
print(isinstance(man, Man))

man1 = Man.fromFathersAge('John', 1965, 20)
print(isinstance(man1, Man))

#create class method using classmethod():?

class School:
    # class variable
    name = 'ABC School'

    def school_name(cls):
        print('School Name is :', cls.name)

# create class method
School.school_name = classmethod(School.school_name)

# call class method
School.school_name()
#Access Class Variables in Class Methods:
class Student:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, school_name):
        # class_name.class_variable
        cls.school_name = school_name

    # instance method
    def show(self):
        print(self.name, self.age, 'School:', Student.school_name)

jessa = Student('Jessa', 20)
jessa.show()

# change school_name
Student.change_school('XYZ School')
jessa.show()
"""
Class Variable:
--> The Variable which is created inside the class.

--> We can access the class variable anywhere in the class and any method
inside the class can access the class variable.

--> The better way to access the Class variable is "class name.variable name"

--> But we can also access the variable using self keyword too.
"self.variable name"

"""

class Addition:

    def _init_(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):

        add1 = self.a + self.b + self.c
        return add1


x = Addition(20, 30, 40)
print("The addition".ljust(40, '.'), ':', x.add())


class Addition:
    d = 40 # Class Variable

    def _init_(self, a, b, c):
        self.a = a  # Instance Variable
        self.b = b  # Instance Variable
        self.c = c  # Instance Variables

    def add(self):  # Instance Method
        add1 = self.a + self.b + self.c + Addition.d
        # Class Variable accessing Method 1
        return add1


x = Addition(20, 30, 40)
print("The addition".ljust(40, '.'), ':', x.add())


class Addition:
    d = 50

    def _init_(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        add1 = self.a + self.b + self.c + self.d
        '''self.d --> since its a Class Variable so we can access this using
        self object'''
        return add1


x = Addition(20, 30, 40)
print("The addition".ljust(40, '.'), ':', x.add())


class Addition:
    d = 70
    e = 80

    def _init_(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        add1 = self.a + self.b + self.c
        return add1

    @classmethod
    def getadd(cls):  # --> This is the syntax to get the class method
        add2 = Addition.d + Addition.e
        return add2


x = Addition(20, 30, 40)
print("The addition".ljust(40, '.'), ':', x.add() + x.getadd())
print("Hello Everyone".ljust(40, '.'),': ' , x.add())
str1 = "Madhu"  # str("Madhu")

#object method:?
#Demonstrating working of object()
# Python 3 code to demonstrate
# working of object()

# declaring the object of class object
obj = object()

# printing its type
print("The type of object class object is : ")
print(type(obj))

# printing its attributes
print("The attributes of its class are : ")
print(dir(obj))

#Demonstrating properties of object:
# Python 3 code to demonstrate
# properties of object()

# declaring the objects of class object
obj1 = object()
obj2 = object()

# checking for object equality
print("Is obj1 equal to obj2 : " + str(obj1 == obj2))

# trying to add attribute to object
obj1.name = "GeeksforGeeks"

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()




