"""
Python too supports file handling and allows users to handle files i.e., to read and write files,
along with many other file handling options, to operate on files.

#Working of open() function:

Before performing any operation on the file like read or write,
first we have to open that file. For this, we should use Python’s inbuilt function open()

f = open(filename, mode)

#Where the following mode is supported:

r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
a:  open an existing file for append operation. It won’t override existing data.
r+:  To read and write data into the file. The previous data in the file will not be deleted.
w+: To write and read  data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data.

"""

# a file named "geek", will be opened with the reading mode.
file = open('geek.txt',"r")
# This will print every line one by one in the file
for each in file:
	print (each)

# Python code to illustrate read() mode
file = open("file.text", "r")
print (file.read())

# Python code to illustrate read() mode character wise
file = open("file.text", "r")
print (file.read(5))

#Creating a file using write() mode:
# Python code to create a file
file = open('write.text','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.write("hello evryone all the best for ur interviews")
file.close()

#Working of append() mode:?
# Python code to illustrate append() mode
file = open('append.text','a')
file.write("This will add this line")
file.close()

'''
rstrip(): This function strips each line of a file off spaces from the right-hand side.
lstrip(): This function strips each line of a file off spaces from the left-hand side.
'''
# Python code to illustrate with()
with open("file.text") as file:
	data = file.read()
# do something with data

# Python code to illustrate with() alongwith write()
with open("file.text", "w") as data:
	data.write("Hello World!!!")

# Python code to illustrate split() function
with open("file.text", "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		print (word)


f = open("geek.txt")      # equivalent to 'r' or 'rt'
f = open("write.text",'w')  # write in text mode
f = open("img.png",'r+b') # read and write in binary mode

try:
   f = open("img.png", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()

with open("content.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
