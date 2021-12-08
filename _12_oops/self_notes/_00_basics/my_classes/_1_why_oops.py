"""
#Python OOPs Concepts:

1.Like other general-purpose programming languages, Python is also an object-oriented
language since its beginning. It allows us to develop applications using an
Object-Oriented approach. In Python,we can easily create and use classes and objects.

2.An object-oriented paradigm is to design the program using classes and objects.
The object is related to real-word entities such as book, house, pencil, etc.
The oops concept focuses on writing the reusable code. It is a widespread technique
to solve the problem by creating objects.

Major principles of object-oriented programming system are given below.

1.Class
2.Object
3.Method
4.Inheritance
5.Polymorphism
6.Data Abstraction
7.Encapsulation

#Class:

The class can be defined as a collection of objects. It is a logical entity
that has some specific attributes and methods. For example: if you have an employee class,
then it should contain an attribute and method, i.e. an email id, name, age, salary, etc.

#Syntax:

class ClassName:
        <statement-1>
        .
        .
        <statement-N>
#Object:

The object is an entity that has state and behavior. It may be any real-world
object like the mouse, keyboard, chair, table, pen, etc.
Everything in Python is an object, and almost everything has attributes and methods.
All functions have a built-in attribute __doc__.

#Method:

The method is a function that is associated with an object.
In Python, a method is not unique to class instances. Any object type can have methods.

#Inheritance:

Inheritance is the most important aspect of object-oriented programming, which
simulates the real-world concept of inheritance. It specifies that the child object
acquires all the properties and behaviors of the parent object.By using inheritance,
we can create a class which uses all the properties and behavior of another class.
The new class is known as a derived class or child class,and the one whose properties
are acquired is known as a base class or parent class.

#Polymorphism:

Polymorphism contains two words "poly" and "morphs". Poly means many,
and morph means shape. By polymorphism, we understand that one task can be performed
in different ways. For example - you have a class animal, and all animals speak.
But they speak differently. Here, the "speak" behavior is polymorphic in a sense
and depends on the animal. So, the abstract "animal" concept does not actually "speak",
but specific animals (like dogs and cats) have a concrete implementation of the action "speak".

#Encapsulation:

Encapsulation is also an essential aspect of object-oriented programming.
It is used to restrict access to methods and variables. In encapsulation,
code and data are wrapped together within a single unit from being modified by accident.

#Data Abstraction:

Data abstraction and encapsulation both are often used as synonyms.
Both are nearly synonyms because data abstraction is achieved through encapsulation.
Abstraction is used to hide internal details and show only functionalities. Abstracting
something means to give names to things so that the name captures the core of what
a function or a whole program does.It provides the re-usability of the code.

#differences:

Object-oriented Programming

1.	Object-oriented programming is the problem-solving approach and used where
 computation is done by  using objects.
2.	It makes the development and maintenance easier.
3.	It simulates the real world entity. So real-world problems can be easily solved through oops.
4.	It provides data hiding. So it is more secure than procedural languages.
You cannot access private data from anywhere.
5.	Example of object-oriented programming languages is C++, Java, .Net, Python, C#, etc.
Procedural Programming
1.Procedural programming uses a list of instructions to do computation step by step.
2.In procedural programming, It is not easy to maintain the codes when the project becomes lengthy.
3.It doesn't simulate the real world.
It works on step by step instructions divided into small parts called functions.
4.Procedural language doesn't provide any proper way for data binding, so it is less secure.
5.Example of procedural languages are: C, Fortran, Pascal, VB etc.



#Creating an instance of the class:

A class needs to be instantiated if we want to use the class attributes in another
class or method. A class can be instantiated by calling the class using the class name.

The syntax to create the instance of the class is given below.

<object-name> = <class-name>(<arguments>)

#Delete the Object:

We can delete the properties of the object or object itself by using the del keyword.

#Python Constructor:

A constructor is a special type of method (function) which is used to initialize
the instance members of the class.In C++ or Java, the constructor has the same
name as its class, but it treats constructor differently in Python. It is used to create an object.

Constructors can be of two types.

1.Parameterized Constructor
2.Non-parameterized Constructor

#Creating the constructor in python:

In Python, the method the __init__() simulates the constructor of the class.
This method is called when the class is instantiated. It accepts the self-keyword as a
first argument which allows accessing the attributes or method of the class.
We can pass any number of arguments at the time of creating the class object,
depending upon the __init__() definition. It is mostly used to initialize the
class attributes. Every class must have a constructor, even if it simply relies
on the default constructor.

#Python Non-Parameterized Constructor:

The non-parameterized constructor uses when
we do not want to manipulate the value or the constructor that has only self as an argument.

#Python Parameterized Constructor:

The parameterized constructor has multiple parameters along with the self.

#Python Default Constructor:

When we do not include the constructor in the class or forget to declare it, then
that becomes the default constructor. It does not perform any task but initializes the objects.


#Python built-in class functions:


1   getattr(obj,name,default)	It is used to access the attribute of the object.
2	setattr(obj, name,value)	It is used to set a particular value to the specific
                                attribute of an object.
3	delattr(obj, name)	        It is used to delete a specific attribute.
4	hasattr(obj, name)	        It returns true if the object contains some specific attribute.


#Built-in class attributes:

1	__dict__	It provides the dictionary containing the information about the class namespace.
2	__doc__	    It contains a string which has the class documentation
3	__name__	It is used to access the class name.
4	__module__	It is used to access the module in which, this class is defined.
5	__bases__	It contains a tuple including all base classes.

#Python Inheritance:

Inheritance is an important aspect of the object-oriented paradigm.
Inheritance provides code reusability to the program because we can use an
existing class to create a new class instead of creating it from scratch.
In inheritance, the child class acquires the properties and can access all
the data members and functions defined in the parent class.
A child class can also provide its specific implementation to the functions of the parent class.
In python, a derived class can inherit base class by
just mentioning the base in the bracket after the derived class name.

#Syntax:

class derived-class(base class):
    <class-suite>

1. Single inheritance
2. multiple
3. multi level
4.hybrid
5.hyrarchical

#The isinstance (obj, class) method:

The isinstance() method is used to check the relationship between the objects
and classes. It returns true if the first parameter, i.e., obj is the instance
of the second parameter, i.e., class.

#Method Overriding:

We can provide some specific implementation of the parent class method in our
child class. When the parent class method is defined in the
child class with some specific implementation, then the concept is called method overriding.

#why oops:

Developers often choose to use OOP in their Python programs because
it makes code more reusable and makes it easier to work with larger programs. OOP programs
prevent you from repeating code because a class can be defined once and reused many times.

#oops is neccesary:

OOP in Python. Python is a great programming language that supports OOP.
You will use it to define a class with attributes and methods,
which you will then call. ... This also makes Python easier to understand
and learn for beginners, its code being more readable and intuitive.





"""