'''
'''
'''
SC1: As a sub class, I. inherit all super class methods
                     II.create your own methods

SC2: As a sub class, I. inherit all super class methods,override if required
                     II.create your own methods
'''


# SC 1
class A:
    def __init__(self):
        print("SUPER : A constr")

    def read(self):
        print("A reading")


# A has one behavior read()
class B(A):

    def __init__(self):
        print("SUB : B constr")

    def write(self):
        print("B writing")


# B has two behaviors read() write()
a1 = A()
a1.read()

b1 = B()
b1.read()  # inherited method
b1.write()  # sub class specific method


# SC2
class A:
    def __init__(self):
        print("SUPER : A constr")

    def read(self):
        print("A reading")

    def execute(self):
        print("A executing")


# A has 2 behaviors read() execute()

class B(A):

    def __init__(self):
        print("SUB : B constr")

    def read(self):  # method overriding
        print("B reading")

    def write(self):
        print("B writing")


'''
B has 3 behaviors   - execute() from super class through inheritance
                    - read() i.e, from sub class overriden method
                    - write() from sub class(its  own method)

a1 = A()
a1.read()

b1 = B()
b1.read()
b1.write()

Inherited method  : execute()
Overriden method  : read()
Own method        : write()

'''


#examples:


# superclass
class Person():
    def display1(self):
        print("This is superclass")


# subclass
class Employee(Person):
    def display2(self):
        print("This is subclass")


emp = Employee()  # creating object of subclass

emp.display1()
emp.display2()


# superclass
class Person():
    def __init__(self, per_name, per_age):
        self.name = per_name
        self.age = per_age

    def display1(self):
        print("In superclass method: name:", self.name, "age:", self.age)


# subclass
class Employee(Person):
    def display2(self):
        print("In subclass method: name:", self.name, "age:", self.age)


emp = Employee("John", 20)  # creating object of superclass

emp.display1()
emp.display2()
print("Outside both methods: name:", emp.name, "age:", emp.age)


#using super
# superclass
class Person():
    def __init__(self, per_name, per_age):
        self.name = per_name
        self.age = per_age

    def display1(self):
        print("name:", self.name)
        print("age:", self.age)


# subclass
class Employee(Person):
    def __init__(self, emp_name, emp_age, emp_salary):
        self.salary = emp_salary
        super().__init__(emp_name, emp_age)

    def display2(self):
        print("salary:", self.salary)
        super().display1()


emp = Employee("John", 20, 8000)  # creating object of subclass
emp.display2()

#isinstance():?
# superclass
class Person():
    pass

# subclass
class Employee(Person):
    pass

per = Person()  # creating object of superclass
emp = Employee()  # creating object of subclass

print(isinstance(per, Person))
print(isinstance(per, Employee))
print(isinstance(emp, Person))
print(isinstance(emp, Employee))

#issubclass():
# superclass
class Person():
    pass

# subclass
class Employee(Person):
    pass

print(issubclass(Person, Employee))
print(issubclass(Employee, Person))


class Rectangle():
    def __init__(self,leng,br):
        self.length = leng
        self.breadth = br
    '''while calling a method in a class python
    automatically passes an instance( object ) of it.
    so we have to pass sef in area i.e. area(self)'''
    def area(self):
        '''length and breadth are not globally defined.
        So, we have to access them as self.length'''
        return self.length*self.breadth
class Square(Rectangle):
    def __init__(self,side):
        Rectangle.__init__(self,side,side)
        self.side = side
s = Square(4)
print(s.length)
print(s.breadth)
print(s.side)
print(s.area())# It appears as nothing is passed but python will pass an instance of class.



