'''seek() method
In Python, seek() function is used to change the position of the File Handle
to a given specific position. File handle is like a cursor, which defines
from where the data has to be read or written in the file.'''
# Python program to demonstrate
# seek() method
'''

# Opening "GfG.txt" text file
f = open("GfG.txt", "r")

# Second parameter is by default 0
# sets Reference point to twentieth
# index position from the beginning
f.seek(20)

# prints current position
print(f.tell())

print(f.readline())
f.close()

# Python code to demonstrate
# use of seek() function


# Opening "GfG.txt" text file
# in binary mode
f = open("data.txt", "rb")

# sets Reference point to tenth
# position to the left from end
f.seek(-10, 2)

# prints current position
print(f.tell())

# Converting binary to string and
# printing
print(f.readline().decode('utf-8'))

f.close()

f = open("file.text", "r")
print(f.tell())'''

f=open("geek.txt","r")
f.seek(10)
print(f.tell())
print(f.readline())
f.close()

'''The tell() method returns the current file position in a file stream.

Tip: You can change the current file position with the seek() method.'''


f = open("gfg.txt", "r")
print(f.readline())
print(f.tell())


f=open("data.txt","r")
f.seek(5)
g=f.tell()
print(g)
print(f.read())
'''
Python seek() method is used for changing the current location of the file handle. The file handle is like a cursor, which is used for defining the location of the data which has to be read or written in the file.

#Syntax:
fi.seek(offset, from_where), where fi is the file pointer  

#Parameters:

Offset: This is used for defining the number of positions to move forward.

from_where: This is used for defining the point of reference.'''

fi = open("myfile.txt", "r+")
print("Name of the file: ", fi.name)

line_1 = fi.readline()
print("Read Line: %s" % (line_1))

# Again, set the pointer to the beginning
fi.seek(0, 1)
line_2 = fi.readline()
print("Read Line: %s" % (line_2))

# Close opend file
fi.close()

fi = open("write_data1.txt", "rb")

# the user is setting the reference point to thirtieth position to the left from
# end
fi.seek(-10, 2)

# now print the current position
print(fi.tell())

# now the user will Convert the binary to string
print(fi.readline().decode('utf-8'))

fi.close()


f = open("data.txt", "r")
cursor_position = f.tell()
print("Cursor Position is :",cursor_position)
data = f.read(5)
print("After reading 5 data from file")
cursor_position = f.tell()
print("Cursor Position is :",cursor_position)


f=open("append.text","r")
cursor_position=f.tell()
print("curson position is:",cursor_position)
data=f.read(5)
print("after reading 5 data from file")
cursor_position=f.tell()
print("cursor position:",cursor_position)