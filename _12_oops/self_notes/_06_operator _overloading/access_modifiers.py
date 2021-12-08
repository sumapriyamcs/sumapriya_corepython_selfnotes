'''

'''

'''
Access modifiers : public private protected default
'''
'''
class Employee:
     Employee(eid,name,sal):  # constructor
         this.eid = eid
         this.name = name
         this.sal = sal

     private void getedata(): 
         println("Emp data")

suma= Employee(100, 'suma', 10000)
suma.getedata()

'''


class Employee:
    def __init__(self):
        pass

    def _getx(self):
        return "hello"

    def get_edata(self):
        val = self._getx()
        print(val)

    def update_edata(self):
        val = self._getx()
        print(val)


emp = Employee()
emp.get_edata()

"""
1.Public Access Modifier:
The members of a class that are declared public are easily accessible from any part
of the program. All data members and member functions of a class are public by default.


"""

# program to illustrate public access modifier in a class


class Geek:

    # constructor
    def __init__(self, name, age):
        # public data members
        self.geekName = name
        self.geekAge = age

    # public member function
    def displayAge(self):
        # accessing public data member
        print("Age: ", self.geekAge)


# creating object of the class
obj = Geek("R2J", 20)

# accessing public data member
print("Name: ", obj.geekName)

# calling public member function of the class
obj.displayAge()

class Student:
    schoolName = 'netaji school' # class attribute

    def __init__(self, name, age):
        self.name=name # instance attribute
        self.age=age # instance attribute

std = Student("suma", 25)
print(std.schoolName)
print(std.name)
std.age = 20
print(std.age)

class employee:
    def __init__(self, name, sal):
        self.name=name
        self.salary=sal

e1=Employee("Kiran",10000)
print(e1.salary)  # salary is public attribute

# we can access employee class's attributes and also modify their values
e1.salary=20000
print(e1.salary)


class Modifiers:

    def __init__(self,name):
        self.public_member = name

mod = Modifiers("SKAUL05")
print(mod.public_member) #Accessing the Public Attribute of Modifier Class
mod.public_member = "Github" #Changing it's value
print(mod.public_member)

"""
2.Protected Access Modifier:

The members of a class that are declared protected are only accessible
to a class derived from it. Data members of a class are declared protected by adding a single
underscore ‘_’ symbol before the data member of that class.
"""


 # program to illustrate protected access modifier in a class

# super class
class Student:
    # protected data members
    _name = None
    _roll = None
    _branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    # protected member function
    def _displayRollAndBranch(self):
        # accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)


# derived class
class Geek(Student):

    # constructor
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

    # public member function
    def displayDetails(self):
        # accessing protected data members of super class
        print("Name: ", self._name)

        # accessing protected member functions of super class
        self._displayRollAndBranch()


# creating objects of the derived class
obj = Geek("R2J", 1706256, "Information Technology")

# calling public member functions of the class
obj.displayDetails()




class Student:
    _schoolName = 'netaji school'  # protected class attribute

    def __init__(self, name, age):
        self._name = name  # protected instance attribute
        self._age = age  # protected instance attribute

std = Student("Suma", 25)
print(std._name)
std._name = 'priya'
print(std._name)

class Student:
	def __init__(self,name):
		self._name = name
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self,newname):
		self._name = newname
std = Student("Swati")
print(std.name)
std.name = 'Dipa'
print(std.name)
std._name # still accessible

class employee:
    def __init__(self, name, sal):
        self._name=name    # name and sal are protected
        self._salary=sal

e1=employee("Kiran",10000)
print(e1._salary)  # salary is protected attribute

e1._salary=20000
print(e1._salary)


class Modifiers:

    def __init__(self, name):
        self._protected_member = name  # Protected Attribute


m = Modifiers("SKAUL05")
print(m._protected_member)


class Modifiers:

    def __init__(self, name):
        self._protected_member = name  # Protected Attribute

m = Modifiers("SKAUL05")
print(m._protected_member)
m._protected_member = "Github" # Changing Protected Attribute values
print(m._protected_member)

"""
3.Private Access Modifier:

The members of a class that are declared private are accessible within the class only,
private access modifier is the most secure access modifier. Data members
of a class are declared private by adding a double underscore ‘__’ symbol
before the data member of that class.
"""

'''
# program to illustrate private access modifier in a class

class Geek:
        # private members
        __name = None
        __roll = None
        __branch = None

        # constructor
        def __init__(self, name, roll, branch):
            self.__name = name
            self.__roll = roll
            self.__branch = branch

        # private member function
        def __displayDetails(self):
            # accessing private data members
            print("Name: ", self.__name)
            print("Roll: ", self.__roll)
            print("Branch: ", self.__branch)

        # public member function
        def accessPrivateFunction(self):
            # accesing private member function
            self.__displayDetails()

    # creating object
obj = Geek("R2J", 1706256, "Information Technology")
    # calling public member function of the class## # obj.accessPrivateFunction()'''


'''class Student:
    __schoolName = 'XYZ School' # private class attribute

    def __init__(self, name, age):
        self.__name=name  # private instance attribute
        self.__salary=age # private instance attribute
    def __display(self):  # private method
	        print('This is private method.')
std = Student("Bill", 25)
std.__schoolName
std.__name
std.__display()'''

'''
#Below is a program to illustrate the use of all the above three access
#modifiers (public, protected, and private) of a class in Python:
# program to illustrate access modifiers of a class

# super class
class Super:
    # public data member
    var1 = None

    # protected data member
    _var2 = None

    # private data member
    __var3 = None

    # constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # public member function
    def displayPublicMembers(self):
        # accessing public data members
        print("Public Data Member: ", self.var1)

    # protected member function
    def _displayProtectedMembers(self):
        # accessing protected data members
        print("Protected Data Member: ", self._var2)

    # private member function
    def __displayPrivateMembers(self):
        # accessing private data members
        print("Private Data Member: ", self.__var3)

    # public member function
    def accessPrivateMembers(self):
        # accessing private member function
        self.__displayPrivateMembers()'''


# derived class
class Sub(Super):

    # constructor
    def __init__(self, var1, var2, var3):
        Super.__init__(self, var1, var2, var3)

    # public member function
    def accessProtectedMembers(self):
        # accessing protected member functions of super class
        self._displayProtectedMembers()


# creating objects of the derived class
obj = Sub("Geeks", 4, "Geeks !")

# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

# Object can access protected member
print("Object is accessing protected member:", obj._var2)

# object can not access private member, so it will generate Attribute error
# print(obj.__var3)


