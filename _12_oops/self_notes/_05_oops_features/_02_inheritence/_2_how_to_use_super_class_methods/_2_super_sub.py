"""
#python super:?

One of the important OOP features is Inheritance in Python. When a class inherits some or all of the behaviors from another class is known as Inheritance.
In such a case, the inherited class is the subclass and the latter class is the parent class.
In an inherited subclass, a parent class can be referred to with the use of the super() function.
The super function returns a temporary object of the superclass that allows access
to all of its methods to its child class.

super() is a built - in method which is useful to call the super class constructors, variables and
methods from the child class .

There  are 3 constraints to use the super function: -

The class and its methods which are referred by the super function
The arguments of the super function and the called function should match.
Every occurrence of the method must include super() after you use it.

#Syntax:

super(type, object)

"""

#Super function in single inheritance:?
# Python program to demonstrate
# super function


class Animals:

    # Initializing constructor
    def __init__(self):
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.mammals = True

    def isMammal(self):
        if self.mammals:
            print("It is a mammal.")

    def isDomestic(self):
        if self.domestic:
            print("It is a domestic animal.")


class Dogs(Animals):
    def __init__(self):
        super().__init__()

    def isMammal(self):
        super().isMammal()


class Horses(Animals):
    def __init__(self):
        super().__init__()

    def hasTailandLegs(self):
        if self.tail and self.legs == 4:
            print("Has legs and tail")


# Driver code
Tom = Dogs()
Tom.isMammal()
Bruno = Horses()
Bruno.hasTailandLegs()


class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')


class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')


d1 = Dog()
super().__init__('Dog')
Mammal.__init__(self, 'Dog')


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


#Super function in multiple inheritance :?

class Mammal():

    def __init__(self, name):
        print(name, "Is a mammal")


class canFly(Mammal):

    def __init__(self, canFly_name):
        print(canFly_name, "cannot fly")

        # Calling Parent class
        # Constructor
        super().__init__(canFly_name)


class canSwim(Mammal):

    def __init__(self, canSwim_name):
        print(canSwim_name, "cannot swim")

        super().__init__(canSwim_name)


class Animal(canFly, canSwim):

    def __init__(self, name):
        # Calling the constructor
        # of both thr parent
        # class in the order of
        # their inheritance
        super().__init__(name)


# Driver Code
Carol = Animal("Dog")


class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.');


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)


class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)


class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)


class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.');
        super().__init__('Dog')


d = Dog()
print('')
bat = NonMarineMammal('Bat')

#sample example for super
class person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self):
        print(firstname, ' ', lastname)


class student(person):
    def __init__(self, firstname, lastname, grade):
        self.grade = grade
        super().__init__(firstname, lastname)  # calling base constructor

    def display_details():
        super().fullname()  # calling base class method
        print('Grade ', self.grade)


std = student('James', 'Bond', '10')
std.display_details()


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

square = Square(4)
square.area()

#what super() can do?
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length
cube = Cube(3)
cube.surface_area()
cube.volume()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks

    def display(self):
       super().display()
       print('Roll No:',self.rollno)
       print('Marks:',self.marks)

s1=Student('Durga',22,101,90)
s1.display()
class P:
    a=10
    def __init__(self):
      self.b=10
    def m1(self):
        print('Parent instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')
class C(P):
    a=888
    def __init__(self):
        self.b=999
        super().__init__()
        print(super().a)
        super().m1()
        super().m2()
        super().m3()

c=C()





