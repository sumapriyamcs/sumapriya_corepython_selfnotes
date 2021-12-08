"""

#The self-parameter:

The self-parameter refers to the current instance of the class and accesses
the class variables. We can use anything instead of self,
but it must be the first parameter of any function which belongs to the class.
self represents the instance of the class.
By using the “self” keyword we can access the attributes and methods of the class in python.

Self:
--> Self is key word which represents the instance of the class.
--> By using the “self” keyword we can access the attributes and methods of the
 class in python
--> Self is a object which wraps the instance variables.
--> Self is a Special parameter.

# Write Python3 code here

class car():

    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model )
        print("color is", self.color )

# both objects have different self which
# contain their attributes
audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")

audi.show()     # same output as car.show(audi)
ferrari.show()  # same output as car.show(ferrari)

# Behind the scene, in every instance method
# call, python sends the instances also with
# that method call like car.show(audi)


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")
cat1 = Cat('Andy', 2)
cat2 = Cat('Phoebe', 3)


class Point(object):
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def distance(self):
        return (self.x**2 + self.y**2) ** 0.5
p1 = Point(6,8)
p1.distance()


class Rectangle ():
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def area (self):
        return (self.x * self.y)
rec1=Rectangle(6,10)
print ("Area is:", rec1.area())


class Person:

      def _init_(self, name, age):

        self.name = name
        self.age = age

      def myfunc(self):
          print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()



class Person:

      def _init_(self, name, age):

        self.name = name
        self.age = age

      def myfunc(self):
          print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()

Class Variable:
--> The Variable which is created inside the class.

--> We can access the class variable anywhere in the class and any method
inside the class can access the class variable.

--> The better way to access the Class variable is "class name.variable name"

--> But we can also access the variable using self keyword too.
"self.variable name"

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

"""