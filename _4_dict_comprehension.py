# Python code to demonstrate dictionary
# comprehension

# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]

# but this line shows dict comprehension here
myDict = { k:v for (k,v) in zip(keys, values)}

# We can use below too
# myDict = dict(zip(keys, values))

print (myDict)

# Python code to demonstrate dictionary
# creation using list comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)

# Python code to demonstrate dictionary
# comprehension using if.
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)

# dictionary comprehension example
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)

#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dollar_to_pound = 0.76
new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(new_price)

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict)


original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict_1 = {k: ('old' if v > 40 else 'young')
    for (k, v) in original_dict.items()}
print(new_dict_1)

dictionary = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
}
print(dictionary)

my_list = ['hello', 'hi', 'hello', 'today', 'morning', 'again', 'hello']
my_dict = {k:my_list.count(k) for k in my_list}
print(my_dict)

values=[1,2,3,4,5,6,7,8,9,10]
NewDictionary = {x: x**2 for x in values if x**2 % 4 == 0}
print(NewDictionary)


rollNumbers =[122,233,353,456]
names = ['alex','bob','can', 'don']
NewDictionary={ i:j for (i,j) in zip (rollNumbers,names)}
print(NewDictionary)

