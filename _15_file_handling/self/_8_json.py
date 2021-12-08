'''JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.
Python has a built - in package called json, which can be used to work
with JSON data.'''

import json

# some JSON:
x = '{ "name":"priya", "age":24, "city":"nellore"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(y["name"])
'''
Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.'''

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

import json
y="suma is a good girl and kind hearted"

z=json.dumps(y)
print(z)

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
'''
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python              	JSON
dict	                Object
+list	                Array
tuple	                Array
str	                    String
int	                    Number
float	                Number
True	                true
False	                false
None	                null'''


import json

x = {
  "name": "John",
  "age": 30,
  "married": False,
  "divorced": False,
  "children": ("null","null"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

'''
The json.dumps() method has parameters to make it easier to read the result:
You can also define the separators, default value is (", ", ": "), which means 
using a comma and a space to separate each object, and a colon and a space to
separate keys from values:

The dumps () function:

The dumps() function is used to store serialized data in the Python file.
It accepts only one argument that is Python data for serialization. 
The file-like argument is not used because we aren't not writing data to disk.
 
json.load() vs json.loads()
The json.load() function is used to load JSON file, whereas json.loads() 
function is used to load string.

json.dump() vs json.dumps()
The json.dump() function is used when we want to serialize the Python objects 
into JSON file and json.dumps() function is used to convert JSON data as a 
string for parsing and printing.

Deserializing JSON : 
Deserialization is the opposite of Serialization, i.e. conversion of JSON objects
into their respective Python objects. The load() method is used for it. 
If you have used JSON data from another program or obtained it as a string format 
of JSON, then it can easily be deserialized with load(), 
which is usually used to load from string, otherwise, the root object is in a list or dict. 
'''
#Python JSON to dict:?

import json

person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print( person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])

#Convert dict to JSON:?


import json

person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)
'''
Python	            JSON Equivalent
dict	            object
list, tuple	        array
str	                string
int, float, int	    number
True	            true
False	            false
None	            null

#Writing JSON to a file:

import json

person_dict = {"name": "Bob",
"languages": ["English", "Fench"],
"married": True,
"age": 32
}

with open('person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)

#Python pretty print JSON:?

import json

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 4, sort_keys=True)
'''
