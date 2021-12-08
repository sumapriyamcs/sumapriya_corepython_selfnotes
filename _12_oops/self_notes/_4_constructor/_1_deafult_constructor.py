"""
# Constructors in Python

Constructors are generally used for instantiating an object. The task of constructors is
to initialize(assign values) to the data members of the class when an object of the
class is created. In Python the _init_() method is called the constructor and is always
called when an object is created.

The constructor is a method that is called when an object is created.
This method is defined in the class and can be used to initialize basic variables.

Syntax of constructor declaration :

def _init_(self):
# body of the constructor

Types of constructors :

default constructor: The default constructor is a simple constructor which doesn’t
accept any arguments. Its definition has only one argument which is a reference to
the instance being constructed.

parameterized constructor: constructor with parameters is known as
parameterized constructor. The parameterized constructor takes its first argument
as a reference to the instance being constructed known as self and the rest
of theparameterized constructor

Features of Python Constructors:

In Python, a Constructor begins with double underscore () and is always named as __init_().
In python Constructors, arguments can also be passed.
In Python, every class must necessarily have a Constructor.
If there is a Python class without a Constructor, a default Constructor is
automatically created without any arguments and parameters.

Counting the number of objects of a class
The constructor is called automatically when we create the object of the class.
"""
class Student:
    count = 0
    def _init_(self):
        Student.count = Student.count + 1
s1=Student()
s2=Student()
s3=Student()
print("The number of students:",Student.count)



class Employees():

    def _init_(self, Name, Salary):
        self.Name = Name
        self.Salary = Salary

    def details(self):
        print("Employee Name : ", self.Name)
        print("Employee Salary: ", self.Salary)
        print("\n")


first = Employees("Khush", 10000)
second = Employees("Raam", 20000)
third = Employees("Lav", 10000)
fourth = Employees("Sita", 30000)
fifth = Employees("Lucky", 50000)

first.details()
second.details()
third.details()
fourth.details()
fifth.details()



class Employee:
    def _init_(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))


emp1 = Employee("John", 101)
emp2 = Employee("David", 102)

# accessing display() method to print employee 1 information

emp1.display()

# accessing display() method to print employee 2 information
emp2.display()


class GeekforGeeks:

# default constructor
    def _init_(self):
        self.geek = "GeekforGeeks"
# a method for printing data members
    def print_Geek(self):
        print(self.geek)
# creating object of the class
obj = GeekforGeeks()
# calling the instance method using the object obj
obj.print_Geek()


class Employee:
    pass


'''
converts as below
                        class Employee:
                            def _init_(self):
                                pass
'''
print("Employee class @ ", Employee)
obj = Employee()


# Default constructor
class Employee:

    def _init_(self):  # Default constructor
        pass  # to perform any generic action

    def getedata(self, eid, sal):
        print("Employee Data", eid, sal)


suma = Employee()
suma.getedata(101, 10000)  # Employee.getedata(madhu,101,10000)

# while defining class, default constructor is not mandatory. Python give automatically

"""

# Employee CRUD Operations


REQUIREMENT :
1. Create an employee with eid,name,sal  #
2. Retrieve emp details
3. Give hike for employee based on experience
    Acceptance Criteria : 0 to 2 exp  => 5% hike
                          2 to 3 exp  => 10% hike
                          3 to 5 exp  => 20% hike
                          5+          => 30% hike

4. Delete emp once he exits from company

GUI  -->  Backend             ---> Database

UI  --->  Python/Java/.Net    --->  Oracle/Postgresql/Mysql/Mongodb

"""


print("-----------Employee hike---------------")


class Employee:
    # create employee
    def _init_(self, eid, name,
               sal):  # emailid,mobiileno,perm_address,pre_add,joining_date,bloodgr,gendder
        self.eid = eid
        self.name = name
        self.sal = sal

    # 2. Retrieve emp details
    def get_emp_info(self):
        print("Employee details : ", self.eid, self.name, self.sal)

    # 3. Update emp sal based on exp
    '''
        3. Give hike for employee based on experience
        Acceptance Criteria : 0 to 2 exp  => 5% hike
                              2 to 3 exp  => 10% hike
                              3 to 5 exp  => 20% hike
                              5+          => 30% hike
    '''

    def update_emp_sal(self, exp):
        # Server validations
        if exp < 0:
            print("Please enter valid experience.")
            return None
        if exp >= 0 and exp < 2:
            hike = (self.sal * 5) // 100
            self.sal = self.sal + hike
        elif exp >= 2 and exp < 3:
            hike = (self.sal * 10) // 100
            self.sal = self.sal + hike
        elif exp >= 3 and exp < 5:
            hike = (self.sal * 20) // 100
            self.sal = self.sal + hike
        elif exp >= 5:
            hike = (self.sal * 30) // 100
            self.sal = self.sal + hike
        print("Employee  after hike : ", self.eid, self.name, self.sal)

    def delete_emp(self):
        pass


# Data hard coding
suma = Employee(100, 'suma', 1500000)
suma.get_emp_info()
suma.update_emp_sal(4)

'''
UI PAGE:
---------
EmmpID: 101
name  : satish
exp   : -10
Mobileno : 34232443243

# client validations
# server validations
'''

# Positional arguments


class Employee:
    # Parameterized Constructor
    def _init_(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def getedata(self):
        pass

suma = Employee(200, 'suma', 10000)


'''
# Defining Constructor
    - Default constructor
    - Parameterized constructor
            - Positional arguments
            - Default arguments
            - keyword arguments

'''
# Default arguments example

class Employee:
    # parameterized constructors
    def _init_(self, eid=None, name=None, sal=None):  # Constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal

    def getedata(self):
        print("Employee info : ", self.eid, self.name, self.sal)


suma = Employee()
suma.getedata()

sam = Employee(201)
sam.getedata()

suma = Employee(201, 'sunandha')
suma.getedata()

ravi = Employee(200, 'yeswanth', 10000)
ravi.getedata()

raju= Employee(name='Farooq', sal=20000)
raju.getedata()


class Student:
        def _init_(self):
             print("The First Constructor")

        def _init_(self):
             print("The second contructor")


st = Student()
"""
"""
class Student:
    def _init_(self, name, id, age):  
        self.name = name  
        self.id = id  
        self.age = age  

    # creates the object of the class Student  
s = Student("John", 101, 22)  

# prints the attribute name of the object s  
print(getattr(s, 'name'))  

# reset the value of attribute age to 23  
setattr(s, "age", 23)  

# prints the modified value of age  
print(getattr(s, 'age'))  

# prints true if the student contains the attribute with name id  

print(hasattr(s, 'id'))  
# deletes the attribute age  
delattr(s, 'age')  

# this will give an error since the attribute age has been deleted  
print(s.age)  

class Student:    

    def _init_(self,name,id,age):    
        self.name = name;    
        self.id = id;    
        self.age = age    

    def display_details(self):    
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id,self.age))

s = Student("suma",46,24)
print(s._doc_)    
print(s._dict_)    
print(s._module_)


class Plane:
    def __init__(self):
        self.wings = 2

        # fly
        self.drive()
        self.flaps()
        self.wheels()

    def drive(self):
            print('Accelerating')

    def flaps(self):
            print('Changing flaps')

    def wheels(self):
            print('Closing wheels')

ba = Plane()


#default value
class Bug:
   def __init__(self):
       self.wings = 4

class Human:
   def __init__(self):
       self.legs = 2
       self.arms = 2

bob = Human()
tom = Bug()

print(tom.wings)
print(bob.arms)
#default constructor

class Addition:
    # Defininf a constructor
    def __init__(self):
        # with the help of self.xyz
		# we are initializing instance variable
        self.num1=1000
        self.num2=2000
        self.num3=3000

    def result(self):
        self.num=self.num1+self.num2+self.num3
        print('Output:',self.num)


# Here we create the object for call
# which calls the constructor
Sum = Addition()

# calling the instance method
# using the object Sum
Sum.result()

class DemoClass:
    num = 101

    # a method
    def read_number(self):
        print(self.num)


# creating object of the class
obj = DemoClass()

# calling the instance method using the object obj
obj.read_number()


class DemoClass:
    num = 101

    # non-parameterized constructor
    def __init__(self):
        self.num = 999

    # a method
    def read_number(self):
        print(self.num)


# creating object of the class
obj = DemoClass()

# calling the instance method using the object obj
obj.read_number()

class demo:
        def show(self):
            print("Thank you for instantiating me :)")
d=demo()
d.show()





