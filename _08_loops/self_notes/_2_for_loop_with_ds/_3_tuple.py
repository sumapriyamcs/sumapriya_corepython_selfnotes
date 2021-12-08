thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

tuple1 = ('a', 'e', 'i', 'o', 'u')

for item in tuple1:
    #do something
    print(item)

tuple1 = (5, 3, 2, 8, 4, 4, 6, 2)

sum = 0

for num in tuple1:
    sum += num

print(sum)

colorSet = set(["red", "green", "blue"])

for color in colorSet:
    print(color)

my_data = (1, 2, "Kevin", 8.9)

# accessing last element
# prints 8.9
print(my_data[-1])

# prints 2
print(my_data[-3])



mixed_type = ('C',0,0,'K','I','E')

for i in mixed_type:
    print(i,":",type(i))