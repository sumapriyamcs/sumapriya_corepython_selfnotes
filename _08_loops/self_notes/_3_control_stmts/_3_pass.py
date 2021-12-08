# Python program to demonstrate
# pass statement


s = "geeks"

# Empty loop
for i in s:
	# No error will be raised
	pass

# Empty function
def fun():
	pass

# No error will be raised
fun()

# Pass statement
for i in s:
	if i == 'k':
		print('Pass executed')
		pass
	print(i)


for letter in 'Python':
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)

print ("Good bye!")


def my_func():
    print('pass inside function')
    pass
my_func()


# Pass statement in for-loop
test = "Guru"
for i in test:
    if i == 'r':
        print('Pass executed')
        pass
    print(i)


a=1
if a==1:
    print('pass executed')
    pass


months = ['January', 'June', 'March', 'April']
for mon in months:
    pass
print(months)


x = 0
for x in range(10):
    if x == 4:
        pass
    print(x)

