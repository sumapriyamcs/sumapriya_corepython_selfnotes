a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
  print(key)

dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key, value in dt.items():
    print(key, value)

dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key in dt:
    print(key, dt[key])

dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key, value in dt.iteritems():
    print(key, value)

dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key in dt.keys():
    print(key)

for value in dt.values():
    print(value)


#Python Program to Multiply All the Items in a Dictionary
d={'A':10,'B':10,'C':239}
tot=1
for i in d:
    tot=tot*d[i]
print(tot)

