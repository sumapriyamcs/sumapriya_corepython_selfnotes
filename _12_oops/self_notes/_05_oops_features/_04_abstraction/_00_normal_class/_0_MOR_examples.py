

"""
class A:
    def m1(self):
        print("In A : m1() ")

class B(A):
    def m2(self):
        print("In B :m2()")

a1 = A()
a1.m1()
print("-----------")
b1 = B()
b1.m1()
b1.m2()
#b1.m3()


class A:
    def m1(self):
        print("In A : m1() ")

class B(A):

    def m2(self):
        print("In B :m2()")   # 2

    #method overriding
    def m1(self):
        print("In B :m1()")   # 1.2

a1 = A()
a1.m1()
print("-----------")
b1 = B()
b1.m1()
b1.m2()
#b1.m3()

class A:
  def method(self):
    print("A.method() called")

class B(A):
  def method(self):
    print("B.method() called")

b = B()
b.method()

class A:
  def method(self):
    print("A.method() called")

class B:
  pass

class C(B, A):
  pass

c = C()
c.method()


lass A:
  def method(self):
    print("A.method() called")

class B:
  def method(self):
    print("B.method() called")

class C(A, B):
  pass

class D(C, B):
  pass

d = D()
d.method()

class A:
  def method(self):
    print("A.method() called")

class B:
  def method(self):
    print("B.method() called")

class C(A, B):
  pass

class D(C, B):
  pass

d = D()
d.method()


class A:
    def myname(self):
        print("I am a class A")


class B(A):
    def myname(self):
        print("I am a class B")


class C(A):
    def myname(self):
        print("I am a class C")


c = C()
print(c.myname())


class A:
    def myname(self):
        print(" I am a class A")


class B(A):
    def myname(self):
        print(" I am a class B")


class C(A):
    def myname(self):
        print("I am a class C")

    # classes ordering


class D(B, C):
    pass


d = D()
d.myname()
"""