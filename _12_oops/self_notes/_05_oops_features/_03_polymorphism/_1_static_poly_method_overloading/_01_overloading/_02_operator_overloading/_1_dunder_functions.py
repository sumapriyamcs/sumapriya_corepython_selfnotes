"""
Dunder or magic methods in Python are the methods having two prefix and
suffix underscores in the method name. Dunder here means “Double Under (Underscores)”.
These are commonly used for operator overloading.

Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.

The __init__ method for initialization is invoked without any call,
when an instance of a class is created, like constructors in certain other programming
languages such as C++, Java, C#, PHP etc. These methods are the reason we can
add two strings with ‘+’ operator without any explicit typecasting.

"""

# declare our own string class
class String:

    # magic method to initiate object
    def __init__(self, string):
        self.string = string


# Driver Code
if __name__ == '__main__':
    # object creation
    string1 = String('Hello')

    # print object location
    print(string1)


# declare our own string class
class String:

    # magic method to initiate object
    def __init__(self, string):
        self.string = string

    # print our string object
    def __repr__(self):
        return 'Object: {}'.format(self.string)


# Driver Code
if __name__ == '__main__':
    # object creation
    string1 = String('Hello')

    # print object location
    print(string1)


# declare our own string class
class String:

    # magic method to initiate object
    def __init__(self, string):
        self.string = string

    # print our string object
    def __repr__(self):
        return 'Object: {}'.format(self.string)


# Driver Code
if __name__ == '__main__':
    # object creation
    string1 = String('Hello')

    # concatenate String object and a string
    print(string1 + ' world')

#Now add __add__ method to String:#class:
# declare our own string class
class String:

    # magic method to initiate object
    def __init__(self, string):
        self.string = string

        # print our string object

    def __repr__(self):
        return 'Object: {}'.format(self.string)

    def __add__(self, other):
        return self.string + other


# Driver Code
if __name__ == '__main__':
    # object creation
    string1 = String('Hello')

    # concatenate String object and a string
    print(string1 + ' Geeks')

def __init__(self,names):
    if names:
        self.names = names.copy()
        for name in names:
            self.versions[name] = 1
    else:
        raise Exception("Please Enter the names")
p = softwares (['S1','S2','S3'])
p1 =softwares([])

#str
def __str__(self):
    s ="The current softwares and their versions are listed below: \n"
    for key,value in self.versions.items():
        s+= f"{key} : v{value} \n"
    return s
print(p)

#setitem
def __setitem__(self,name,version):
    if name in self.versions:
        self.versions[name] = version
    else:
        raise Exception("Software Name doesn't exist")
p['S1'] = 2
p['2'] = 2

#getitem
def __getitem__(self,name):
    if name in self.versions:
        return self.versions[name]
    else:
        raise Exception("Software Name doesn't exist")
print(p['S1'])
print(p['1'])

#delitem
def __delitem__(self,name):
    if name in self.versions:
        del self.versions[name]
        self.names.remove(name)
    else:
        raise Exception("Software Name doesn't exist")
del p['S1']


#len
def __len__(self):
    return len(self.names)
print(len(p))

#contains
def __contains__(self,name):
    if name in self.versions:
        return True
    else:
        return False
if 'S2' in p:
    print("Software Exists")
else:
    print("Software DOESN'T exist")
#complete code
class softwares:
    names = []
    versions = {}

    def __init__(self, names):
        if names:
            self.names = names.copy()
            for name in names:
                self.versions[name] = 1
        else:
            raise Exception("Please Enter the names")

    def __str__(self):
        s = "The current softwares and their versions are listed below: \n"
        for key, value in self.versions.items():
            s += f"{key} : v{value} \n"
        return s

    def __setitem__(self, name, version):
        if name in self.versions:
            self.versions[name] = version
        else:
            raise Exception("Software Name doesn't exist")

    def __getitem__(self, name):
        if name in self.versions:
            return self.versions[name]
        else:
            raise Exception("Software Name doesn't exist")

    def __delitem__(self, name):
        if name in self.versions:
            del self.versions[name]
            self.names.remove(name)
        else:
            raise Exception("Software Name doesn't exist")

    def __len__(self):
        return len(self.names)

    def __contains__(self, name):
        if name in self.versions:
            return True
        else:
            return False
#some more dunder functions
class point:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        s = f'({self.x},{self.y})'
        return s


p1 = point(5, 4)
p2 = point(2, 3)

#add
def __add__(self,p2):
    x = self.x + p2.x
    y = self.y + p2.y
    return point(x,y)
p3 = p1 + p2
#iadd
def __iadd__(self,p2):
    self.x += p2.x
    self.y += p2.y
    return self
p1 += p2
print(p1)

#complete code
class point:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        s = f'({self.x},{self.y})'
        return s

    def __add__(self, p2):
        print("In add")
        x = self.x + p2.x
        y = self.y + p2.y
        return point(x, y)

    def __iadd__(self, p2):
        self.x += p2.x
        self.y += p2.y
        return self

    def __isub__(self, p2):
        self.x -= p2.x
        self.y -= p2.y
        return self

    def __imul__(self, p2):
        self.x *= p2.x
        self.y *= p2.y
        return self

    def __itruediv__(self, p2):
        self.x /= p2.x
        self.y /= p2.y
        return self

    def __ifloordiv__(self, p2):
        self.x //= p2.x
        self.y //= p2.y
        return self

    def __call__(self):
        print(f"Called Point {self.x},{self.y}")



