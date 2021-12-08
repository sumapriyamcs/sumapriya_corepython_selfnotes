"""
#PROGRAMS:

1.Python Program to Add a Key-Value Pair to the Dictionary?

key=int(input("Enter the key (int) to be added:"))
value=int(input("Enter the value for the key to be added:"))
d={}
d.update({key:value})
print("Updated dictionary is:")
print(d)

2.Python Program to Concatenate Two Dictionaries Into One?

d1={'A':1,'B':2}
d2={'C':3}
d1.update(d2)
print("Concatenated dictionary is:")
print(d1)

3.Python Program to Check if a Given Key Exists in a Dictionary or Not?

d={'A':1,'B':2,'C':3}
key=raw_input("Enter key to check:")
if key in d.keys():
      print("Key is present and value of the key is:")
      print(d[key])
else:
      print("Key isn't present!")


4.Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)

5.Python Program to Sum All the Items in a Dictionary?

d={'A':100,'B':540,'C':239}
print("Total sum of values in the dictionary:")
print(sum(d.values()))

6.Python Program to Remove the Given Key from a Dictionary?

d = {'a':1,'b':2,'c':3,'d':4}
print("Initial dictionary")
print(d)
key=raw_input("Enter the key to delete(a-d):")
if key in d:
    del d[key]
else:
    print("Key not found!")
    exit(0)
print("Updated dictionary")
print(d)


7.Python Program to Form a Dictionary from an Object of a Class?

class A(object):
     def __init__(self):
         self.A=1
         self.B=2
obj=A()
print(obj.__dict__)


8.Python Program to Map Two Lists into a Dictionary?

keys=[]
values=[]
n=int(input("Enter number of elements for dictionary:"))
print("For keys:")
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    keys.append(element)
print("For values:")
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    values.append(element)
d=dict(zip(keys,values))
print("The dictionary is:")
print(d)


9.Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary?

test_string=raw_input("Enter string:")
l=[]
l=test_string.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))


"""