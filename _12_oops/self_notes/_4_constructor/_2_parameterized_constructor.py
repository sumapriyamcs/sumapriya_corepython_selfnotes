"""
Python Parameterized Constructor:

The parameterized constructor has multiple parameters along with the self.
"""

class Student:

    # Constructor - parameterized
    def _init_(self, name):
        print("This is parametrized constructor")
        self.name = name
    def show(self):
        print("Hello",self.name)
student = Student("John")
student.show()


class Addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()

# display result
obj.display()


class Student:
    # Defining a parameterized constructor having arguments
    def __init__(self, name, ids, college):
        print("This is a parmeterized costructor in python:")
        self.name = name
        self.ids = ids
        self.college = college

    def Display_Details(self):
        print("Student Details:")
        print("Student Name:", self.name)
        print("Student ids:", self.ids)
        print("Student college:", self.college)


# Here we create the object for call
# which calls the constructor
student = Student("Yash", 2023, "Kcc")

# calling the instance method
# using the object student
student.Display_Details()


class DemoClass:
    num = 101

    # parameterized constructor
    def __init__(self, data):
        self.num = data

    # a method
    def read_number(self):
        print(self.num)


# creating object of the class
# this will invoke parameterized constructor
obj = DemoClass(55)

# calling the instance method using the object obj
obj.read_number()

# creating another object of the class
obj2 = DemoClass(66)

# calling the instance method using the object obj
obj2.read_number()

#non-parameterized constructor
class Employee:
   def __init__(self):
       self.id = 1
       print("Employee id is: ", self.id)
e1 = Employee()
e2 = Employee()
e3 = Employee()

class Employee:
   def __init__(self, id):
       self.id = id
       print("Employee id is: ", self.id)
e1 = Employee(1)
e2 = Employee(2)

#parameterised constructor
class Employee:
   def __init__(self, id,name):
       self.id=id
       self.name=name
   def display(self):
       print("Hello my id is :", self.id)
       print("My name is :", self.name)
e1=Employee(1, 'Nithin')
e1.display()
e2=Employee(2, 'Arjun')
e2.display()



class demo:
       def __init__(self):
               self.color='red'
               self.drink='tea'
       def hello(self):
               print(f"Thank you for instantiating me, I'm all {self.color}.  you likeWould some {self.drink}? :)")
d=demo()
d.hello()


class demo:
    def __init__(self, age, country):
        self.age = age
        self.place = country

    def hello(self):
        print(f"Hello, I am a {self.age}yo from {self.place}")

d = demo(22, 'Romania')
d.hello()


