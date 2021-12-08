'''
                           Animal
                  Cat    Dog   Tiger    Lion

'''


class Animal:
    def __init__(self):
        print("In Animal object")

    # Generic behavior
    def eating(self):
        print("Animal Eating")


class Cat(Animal):

    def __init__(self):
        print("In CAT object")

    # Specific behavior
    def sleeping(self):
        print("Cat is sleeping")

    # method overriding
    def eating(self):
        print("Cat is Eating")

cat = Cat()
cat.sleeping()
cat.eating()


# SCENARIOS
print("--------------------------")
class Dog(Animal):
    def __init__(self):
        print("In DOG object")

    # Specific behavior
    def barking(self):
        print("DOG is barking")

dog = Dog()
dog.barking()
dog.eating()

print("----------------------")
class Lion(Animal):
    def __init__(self):
        print("In LION object")

lion = Lion()
lion.eating()


# Python program to demonstrate
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


# Python program to demonstrate
# calling the parent's class method
# inside the overridden method using
# super()


class Parent():

    def show(self):
        print("Inside Parent")


class Child(Parent):

    def show(self):
        # Calling the parent's class
        # method
        super().show()
        print("Inside Child")


# Driver's code
obj = Child()
obj.show()

class Robot:
    def action(self):
        print('Robot action')

class HelloRobot(Robot):
    def action(self):
        print('Hello world')

r = HelloRobot()
r.action()


class Robot:
    def action(self):
        print('Robot action')

class HelloRobot(Robot):
    def action(self):
        print('Hello world')

class DummyRobot(Robot):
    def start(self):
        print('Started.')

r = HelloRobot()
d = DummyRobot()

r.action()
d.action()


class Animal:
    def Walk(self):
        print('Hello, I am the parent class')


class Dog(Animal):
    def Walk(self):
        print('Hello, I am the child class')


print('The method Walk here is overridden in the code')

# Invoking Child class through object r

r = Dog()
r.Walk()

# Invoking Parent class through object r

r = Animal()
r.Walk()

