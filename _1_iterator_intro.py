'''

Python Iterators :
Iterators are objects that can be iterated upon.
Let us see how iterator works and how you can build your own iterator using __iter__ and __next__ methods.

1.What are iterators in Python?
==================================
  => Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.
  => Iterators are everywhere in Python. They are elegantly implemented within for loops, comprehensions, generators etc. but hidden in plain sight.
  => Technically speaking, Python iterator object must implement two special methods,
                  __iter__() and
                  __next__(),
                  collectively called the iterator protocol.
  => An object is called iterable if we can get an iterator from it.
     Most of built-in containers in Python like: list, tuple, string etc. are iterables.
  => iter() function (which in turn calls the __iter__() method) returns an iterator from them.

2. Iterating Through an Iterator in Python
==========================================
  => We use the next() function to manually iterate through all the items of an iterator.
     When we reach the end and there is no more data to be returned, it will raise StopIteration

Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
The iterator object is initialized using the iter() method. It uses the next() method for iteration.

1.__iter(iterable)__ method that is called for the initialization of an iterator.
This returns an iterator object

2.next ( __next__ in Python 3) The next method returns the next value for the iterable.
When we use a for loop to traverse any iterable object, internally it uses the iter()
method to get an iterator object which further uses next() method to iterate over.
This method raises a StopIteration to signal the end of the iteration.
'''
# Here is an example of a python inbuilt iterator
# value can be anything which can be iterate
iterable_value = 'Geeks'
iterable_obj = iter(iterable_value)

while True:
	try:

		# Iterate by calling next
		item = next(iterable_obj)
		print(item)
	except StopIteration:

		# exception will happen when iteration will over
		break

# A simple Python program to demonstrate
# working of iterators using an example type
# that iterates from 10 to given value

# An iterable user defined type
class Test:

	# Constructor
	def __init__(self, limit):
		self.limit = limit

	# Creates iterator object
	# Called when iteration is initialized
	def __iter__(self):
		self.x = 10
		return self

	# To move to next element. In Python 3,
	# we should replace next with __next__
	def __next__(self):

		# Store current value ofx
		x = self.x

		# Stop iteration if limit is reached
		if x > self.limit:
			raise StopIteration

		# Else increment and return old value
		self.x = x + 1;
		return x

# Prints numbers from 10 to 15
for i in Test(15):
	print(i)

# Prints nothing
for i in Test(5):
	print(i)

# Sample built-in iterators

# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s %d" % (i, d[i]))

'''Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. 
They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator:'''

print('---------Iterator For loop Mechanism-----------')
my_list = [4, 7, 0, 3]
print(my_list)  #  my_list.__str__()
for each in my_list:
    print(each)

my_list = [4, 7, 0, 3]        # 1. Define a list
my_iter = my_list.__iter__()  # 2. Get an iterator using iter()  OR   iter(my_list)
print("ITERATOR object : ", my_iter)
print("Consecutive elements")
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())

print("---------Iterator Internal Mechanism-----------")

try:
    print(my_iter.__next__())  # 3. Iterate through it using __next()__
    print(my_iter.__next__())
    print(my_iter.__next__())
    print(my_iter.__next__())
    print(my_iter.__next__()) # This will raise exception, as no items left in my_list
except StopIteration as si:
    print("Stopping iterations")
'''
3. How for loop actually works?
  =>  the for loop was able to iterate automatically through the list.
  => In fact the for loop can iterate over any iterable. 
     Let's take a closer look at how the for loop is actually implemented in Python.
     
  for element in iterable:
    # do something with element
                                       Is actually implemented as.


iter_obj = iter(iterable)            # create an iterator object from that iterable

while True:                          # infinite loop
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
        
    So internally, the for loop creates an iterator object, iter_obj by calling iter() on the iterable.

Ironically, this for loop is actually an infinite while loop.

Inside the loop, it calls next() to get the next element and executes the body of the for loop with this value. 
After all the items exhaust, StopIteration is raised which is internally caught and the loop ends. 
Note that any other kind of exception will pass through.
'''

'''
4. Building Your Own Iterator in Python
    => Building an iterator from scratch is easy in Python. 
       We just have to implement the methods __iter__() and __next__().
    => The __iter__() method returns the iterator object itself. 
       If required, some initialization can be performed.
    => The __next__() method must return the next item in the sequence. 
       On reaching the end, and in subsequent calls, it must raise StopIteration.

'''
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

mystr = "banana"

for x in mystr:
  print(x)
'''
#create iterator:
To create an object/class as an iterator you have to implement the
methods __iter__() and __next__() to your object.
all classes have a function called __init__(), which allows you to do some 
initializing when the object is being created.

The __iter__() method acts similar, you can do operations (initializing etc.), 
but must always return the iterator object itself.

The __next__() method also allows you to do operations, 
and must return the next item in the sequence.'''

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num
a = iter(InfIter())
next(a)
next(a)
next(a)

mystring = "ABC"
for letter in mystring:
        print(letter)

mylist = ['A', 'B', 'C']
print(letter)


class EvenNumbers:
    last = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.last += 2

        if self.last > 8:
            raise StopIteration

        return self.last

en = EvenNumbers()

for num in en:
    print(num)

class natural_numbers:
    def __init__(self, max = 0):
        self.max = max
    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):
        if self.max == self.number:
            raise StopIteration
        else:
            number = self.number
            self.number += 1
            return number

numbers = natural_numbers(10)
i = iter(numbers)
print("# Calling next() one by one:")
print(next(i))
print(next(i))
print("\n")

# Call next method in a loop
print("# Calling next() in a loop:")
for i in numbers:
    print(i)
