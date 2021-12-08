from collections import OrderedDict

d1 = OrderedDict({1: 1, 3: 3, 2: 2})
print("Order dictionary : ", d1)

# A Python program to show different
# ways to create Counter
from collections import Counter

# With sequence of items
print(Counter(['B','B','A','B','C','A','B',
			'B','A','C']))

# with dictionary
print(Counter({'A':3, 'B':5, 'C':2}))

# with keyword arguments
print(Counter(A=3, B=5, C=2))



# A Python program to demonstrate working
# of OrderedDict

from collections import OrderedDict

print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key, value in d.items():
	print(key, value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
	print(key, value)

# A Python program to demonstrate working
# of OrderedDict

from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

print('Before Deleting')
for key, value in od.items():
    print(key, value)

# deleting element
od.pop('a')

# Re-inserting the same
od['a'] = 1

print('\nAfter re-inserting')
for key, value in od.items():
    print(key, value)

# Python program to demonstrate
# defaultdict


from collections import defaultdict

# Defining the dict
d = defaultdict(int)

L = [1, 2, 3, 4, 2, 4, 1, 2]

# Iterate through the list
# for keeping the count
for i in L:
    # The default value is 0
    # so there is no need to
    # enter the key first
    d[i] += 1

print(d)

# Python program to demonstrate
# defaultdict


from collections import defaultdict

# Defining a dict
d = defaultdict(list)

for i in range(5):
    d[i].append(i)

print("Dictionary with values as list:")
print(d)

# Python program to demonstrate
# ChainMap


from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap
c = ChainMap(d1, d2, d3)

print(c)

# Python program to demonstrate
# ChainMap


from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap
c = ChainMap(d1, d2, d3)

# Accessing Values using key name
print(c['a'])

# Accessing values using values()
# method
print(c.values())

# Accessing keys using keys()
# method
print(c.keys())

# Python code to demonstrate namedtuple()

from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student',['name','age','DOB'])

# Adding values
S = Student('Nandini','19','2541997')

# Access using index
print ("The Student age using index is : ",end ="")
print (S[1])

# Access using name
print ("The Student name using keyname is : ",end ="")
print (S.name)

# Python code to demonstrate deque


from collections import deque

# Declaring deque
queue = deque(['name','age','DOB'])

print(queue)

# Python code to demonstrate working of
# pop(), and popleft()

from collections import deque

# initializing deque
de = deque([6, 1, 2, 3, 4])

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print ("The deque after deleting from right is : ")
print (de)

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print ("The deque after deleting from left is : ")
print (de)



# Python program to understand frozenset() function

# tuple of numbers
nu = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# converting tuple to frozenset
fnum = frozenset(nu)

# printing details
print("frozenset Object is : ", fnum)

# Python program to understand use
# of frozenset function

# creating a dictionary
Student = {"name": "Ankit", "age": 21, "sex": "Male",
		"college": "MNNIT Allahabad", "address": "Allahabad"}

# making keys of dictionary as frozenset
key = frozenset(Student)

# printing keys details
print('The frozen set is:', key)

from collections import Counter
list1 = ['x','y','z','x','x','x','y', 'z']
print(Counter(list1))

from collections import Counter
my_str = "Welcome to Guru99 Tutorials!"
print(Counter(my_str))


from collections import Counter
dict1 =  {'x': 4, 'y': 2, 'z': 2, 'z': 2}
print(Counter(dict1))

from collections import Counter
print(Counter("Welcome to Guru99 Tutorials!"))   #using string
print(Counter(['x','y','z','x','x','x','y', 'z'])) #using list
print(Counter({'x': 4, 'y': 2, 'z': 2})) #using dictionary
print(Counter(('x','y','z','x','x','x','y', 'z'))) #using tuple


from collections import Counter
dict1 =  {'x': 4, 'y': 2, 'z': 2}
del dict1["x"]
print(Counter(dict1))


