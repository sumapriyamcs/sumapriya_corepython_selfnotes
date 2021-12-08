my_file = open("content.txt", 'r')   # 1
# Read data from file
f_data = my_file.read()                                        # 2
print("content type :", type(f_data))
print("File content :", f_data)
print("After splitting :", f_data.split("\n"))
print("--------------")
my_file.close()


lines = []
with open('append.text') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    print(f'line {count}: {line}')

with open('content.txt') as f:
    line = f.readline()
    while line:
        line = f.readline()
        print(line)
with open('append.text') as f:
    for line in f:
        print(line)

with open('write_data1.txt', encoding='utf8') as f:
    for line in f:
        print(line.strip())
# Program to show various ways to
# read data from a file.

# Creating a file
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Writing data to a file
file1.write("Hello \n")
file1.writelines(L)
file1.close() # to change file access modes

file1 = open("myfile.txt", "r+")

print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth
# bite from the beginning.
file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(9))
print()

file1.seek(0)

# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()


# Program to show various ways to
# read data from a file.

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Creating a file
with open("myfile.txt", "w") as file1:
	# Writing data to a file
	file1.write("Hello \n")
	file1.writelines(L)
	file1.close() # to change file access modes

with open("myfile.txt", "r+") as file1:
	# Reading form a file
	print(file1.read())
