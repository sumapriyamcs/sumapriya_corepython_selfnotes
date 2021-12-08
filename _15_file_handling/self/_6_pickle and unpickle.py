'''The pickle module is used for implementing binary protocols for serializing and de-serializing
a Python object structure.

Pickling:
It is a process where a Python object hierarchy is converted into
a byte stream.

Unpickling:
It is the inverse of Pickling process where a byte stream is converted
into an object hierarchy.

dumps() – This function is called to serialize an object hierarchy.
loads() – This function is called to de-serialize a data stream.

#Constants provided by the pickle module :
1.pickle.HIGHEST_PROTOCOL
This is an integer value representing the highest protocol version available.
This is considered as the protocol value which is passed to the functions
dump(), dumps().

2.pickle.DEFAULT_PROTOCOL
This is an integer value representing the default  protocol used
for pickling whose value may be less than the value of the highest protocol.

#Functions provided by the pickle module :
pickle.dump(obj, file, protocol=None, *, fix_imports=True)
This function is equivalent to Pickler(file, protocol).dump(obj).This is used
to write a pickled representation of obj to the open file object file.
The optional protocol argument is an integer that tells the pickler to use
the given protocol.The supported protocols are 0 to HIGHEST_PROTOCOL.If
not specified, the default is DEFAULT_PROTOCOL.If a negative
number is specified, HIGHEST_PROTOCOL is selected.

pickle.dumps(obj, protocol = None, *, fix_imports = True)
This function returns the pickled representation of the object as a bytes object.

# Python program to illustrate
#Picle.dumps()
import pickle

data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
data_string = pickle.dumps(data)
print ('PICKLE:', data_string )

pickle.load(file, *, fix_imports = True, encoding = “ASCII”, errors = “strict”)
This function is equivalent to Unpickler(file).load(). This function is used to
read a pickled object representation from the open file object file and return
the reconstituted object hierarchy specified.

pickle.loads(bytes_object, *, fix_imports = True, encoding = “ASCII”, errors = “strict”)
This function is used to read a pickled  object representation from a bytes
object and return the reconstituted object hierarchy specified.'''

# Python program to illustrate
# pickle.loads()
import pickle
import pprint

data1 = [ { 'a':'A', 'b':2, 'c':3.0 } ]
print ('BEFORE:',)
pprint.pprint(data1)

data1_string = pickle.dumps(data1)

data2 = pickle.loads(data1_string)
print ('AFTER:',)
pprint.pprint(data2)

print ('SAME?:', (data1 is data2))
print ('EQUAL?:', (data1 == data2))

'''
Storing data with pickle
What can be pickled?
You can pickle objects with the following data types:

Booleans,
Integers,
Floats,
Complex numbers,
(normal and Unicode) Strings,
Tuples,
Lists,
Sets, and
Dictionaries that ontain picklable objects.
Pickle vs JSON
JSON stands for JavaScript Object Notation. It's a lightweight format for data-interchange, that is easily readable by humans. Although it was derived from JavaScript, JSON is standardized and language-independent.' \' This is a serious advantage over pickle. It's also more secure and much faster than pickle.
'''

# Python3 program to illustrate store
# efficiently using pickle module
# Module translates an in-memory Python object
# into a serialized byte stream—a string of
# bytes that can be written to any file-like object.

import pickle


def storeData():
    # initializing data to be stored in db
    Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak',
             'age': 21, 'pay': 40000}
    Jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak',
               'age': 50, 'pay': 50000}

    # database
    db = {}
    db['Omkar'] = Omkar
    db['Jagdish'] = Jagdish

    # Its important to use binary mode
    dbfile = open('examplePickle', 'ab')

    # source, destination
    pickle.dump(db, dbfile)
    dbfile.close()


def loadData():
    # for reading also binary mode is important
    dbfile = open('examplePickle', 'rb')
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()


if __name__ == '__main__':
    storeData()
    loadData()
#Pickling without a file

# initializing data to be stored in db
Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak',
'age' : 21, 'pay' : 40000}
Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
'age' : 50, 'pay' : 50000}

# database
db = {}
db['Omkar'] = Omkar
db['Jagdish'] = Jagdish

# For storing
b = pickle.dumps(db)	 # type(b) gives <class 'bytes'>

# For loading
myEntry = pickle.loads(b)
print(myEntry)

import pickle
mylist = ['a', 'b', 'c', 'd']
with open('datafile.txt', 'wb') as fh:
   pickle.dump(mylist, fh)

import pickle
pickle_off = open ("datafile.txt", "rb")
emp = pickle.load(pickle_off)
print(emp)

import pickle
mystring="good morning"
with open("string.txt",'wb')as fb:
    pickle.dump(mystring,fb)

import pickle
pickle_off=open("string.txt","rb")
data=pickle.load(pickle_off)
print(data)


import pickle
mytuple=(1,2,3,"suma")
with open("tuple.txt","wb")as tup:
    pickle.dump(mytuple,tup)
import pickle
pic=open("tuple.txt","rb")
info=pickle.load(pic)
print(info)

import pickle
myset={1,2,3,6,8,9,2}
with open("myset.txt","wb")as sett:
    pickle.dump(myset,sett)

import pickle
si=open("myset.txt","rb")
day=pickle.load(si)
print(day)

import pickle
dict={"name":"suma","age":24,"place":"nellore"}
with open("dict.txt","wb")as di:
    pickle.dump(dict,di)

import pickle
f=open("dict.txt","rb")
g=pickle.load(f)
print(g)

import pickle
string="suma priya puchalapalli"
with open ("str.txt","wb")as s:
    pickle.dump(string,s)
import pickle
p=open("str.txt","rb")
r=pickle.load(p)
print(r)

import pickle
n=10
with open("num.txt","wb")as m:
    pickle.dump(n,m)
import pickle
s=open("num.txt","rb")
y=pickle.load(s)
print(y)

import pickle
binary=1001
with open("bin.txt","wb") as n:
    pickle.dump(binary,n)

import pickle
r=open("bin.txt","rb")
i=pickle.load(r)
print(i)
