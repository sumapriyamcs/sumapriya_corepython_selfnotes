"""
#DICTIONARY:

1.Python Dictionary is used to store the data in a key-value pair format.
2.dictionary is the data type in Python,
3.which can simulate the real-life data arrangement where some specific value exists for some particular key.
4.It is the mutable data-structure. The dictionary is defined into element Keys and values.

    ==>Keys must be a single element
    ==>Value can be any type such as list, tuple, integer, etc.

5.In other words, we can say that a dictionary is the collection of key-value pairs
where the value can be any Python object.
6.In contrast, the keys are the immutable Python object, i.e., Numbers, string, or tuple.

#Creating the dictionary:

1.The dictionary can be created by using multiple key-value pairs enclosed with the curly brackets {}
and each key is separated from its value by the colon (:)

#Accessing the dictionary values:

1.the values can be accessed in the dictionary by using the keys as keys are unique in the dictionary.

#Adding dictionary values:

1.The dictionary is a mutable data type, and its values can be updated by using the specific keys.
2.The value can be updated along with key Dict[key] = value.
3.The update() method is also used to update an existing value.

Note: If the key-value already present in the dictionary, the value gets updated.
Otherwise, the new keys added in the dictionary.

#Deleting the elements in the dictionary:
1.The items of the dictionary can be deleted by using the del keyword

@Using pop() method:

1.The pop() method accepts the key as an argument and remove the associated value

#Properties of Dictionary keys:

1. In the dictionary, we cannot store multiple values for the same keys.
If we pass more than one value for a single key,
then the value which is last assigned is considered as the value of the key.

2. In python, the key cannot be any mutable object. We can use numbers, strings, or tuples as the key,
but we cannot use any mutable object like the list as the key in the dictionary.

#Removing elements from Dictionary:

1.We can remove a particular item in a dictionary by using the pop() method.
This method removes an item with the provided key and returns the value.

2.The popitem() method can be used to remove and return an arbitrary (key, value) item pair from the dictionary.
All the items can be removed at once, using the clear() method.

3.We can also use the del keyword to remove individual items or the entire dictionary itself.


#Python Dictionary Comprehension:

1.Dictionary comprehension is an elegant and concise way to create a new dictionary
from an iterable in Python.

2.Dictionary comprehension consists of an expression pair (key: value)
followed by a for statement inside curly braces {}.

3.A dictionary comprehension can optionally contain more for or if statements.

4.An optional if statement can filter out items to form the new dictionary




"""