
'''
https://www.geeksforgeeks.org/operator-overloading-in-python/
'''
# Everything is an object in Python

# Operator overloading
# 10+20  10+20+30

"""x = 10
y = 20
print("Addition : ", x + y)  # x.__add__(y)

list1 = list()
x = 10.5
y = 20.2
print("Addition : ", x + y)  # x.__add__(y)

str1 = 'Hello'
str2 = 'World'
print("Addition  :", str1 + str2) # str1.__add__(str2)



# create 2 employee objects and add their salaries
class Employee(object):

"""


class Sample():

    def __init__(self, a):
        self.a = a

    @classmethod
    def addition(self, *args):
        x, y, z = args
        return x.a + y.a + z.a


s1 = Sample(10)
s2 = Sample(20)
s3 = Sample(30)

print(Sample.addition(s1, s2, s3))

