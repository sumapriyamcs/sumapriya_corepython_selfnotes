'''
#Encoding and Decoding:

Encoding is the technique for transforming the text or values into an
encrypted form. Encrypted data can only be used by the preferred user by
decoding it. Encoding is also known as serialization and decoding is also
called deserialization. Encoding and decoding are done for JSON(object) format.
Python provides a popular package for such operations.
We can install it on Windows by the following command:

pip install demjson

Encoding - The demjson package provides encode() function that is used to
convert the Python object into a JSON string representation.
The syntax is given below:

demjson.encode(self,obj,nest_level = 0)

#Example:1 - Encoding using demjson package

import demjson
a = [{"Name": 'Peter',"Age":20, "Subject":"Electronics"}]
print(demjson.encode(a))

Decoding-The demjson module provides decode() function, which is used to
convert JSON object into Python format type.
The syntax is given below:



Import demjson
a = "['Peter', 'Smith', 'Ricky', 'Hayden']"
print(demjson.decode(a))

complex_json = json.dumps(4 + 17j, cls=ComplexEncoder)
json.loads(complex_json)
'''
'''
import json
#File I/O Open function for read data from JSON File
with open('file.json') as file_object:
        # store file data in object
    # data = json.load(file_object)
    print(file_object.readlines())

import json
# Create a List that contains dictionary
lst = ['a', 'b', 'c',{'4': 5, '6': 7}]
# separator used for compact representation of JSON.
# Use of ',' to identify list items
# Use of ':' to identify key and value in dictionary
compact_obj = json.dumps(lst, separators=(',', ':'))
print(compact_obj)


import json
dic = { 'a': 4, 'b': 5 }
#To format the code use of indent and 4 shows number of space and use of
#separator is not necessary but standard way to write code of particular function.
formatted_obj = json.dumps(dic, indent=4, separators=(',', ': '))
print(formatted_obj)


import json

x = {
  "name": "Ken",
  "age": 45,
  "married": True,
  "children": ("Alice", "Bob"),
  "pets": [ 'Dog' ],
  "cars": [
    {"model": "Audi A1", "mpg": 15.1},
    {"model": "Zeep Compass", "mpg": 18.1}
  	],
}
# sorting result in asscending order by keys:
sorted_string = json.dumps(x, indent=4, sort_keys=True)
print(sorted_string)
'''
#import JSONEncoder class from json
from json.encoder import JSONEncoder
colour_dict = { "colour": ["red", "yellow", "green" ]}
# directly called encode method of JSON
JSONEncoder().encode(colour_dict)
print(colour_dict)
'''
Overview of JSON Deserialization class JSONDecoder
JSONDecoder class is used for deserialization of any Python object while 
performing decoding. It contains three different methods of decoding which are

default(o) – Implemented in the subclass and return deserialized object o object.
decode(o) – Same as json.loads() method return Python data structure of JSON string or data.
raw_decode(o) – Represent Python dictionary one by one and decode object o.
With the help of decode() method of JSONDecoder class, we can also decode JSON 
string as shown in below Python JSON decoder example.
'''

import json
# import JSONDecoder class from json
from json.decoder import JSONDecoder
colour_string = '{ "colour": ["red", "yellow"]}'
# directly called decode method of JSON
JSONDecoder().decode(colour_string)
print(colour_string)

