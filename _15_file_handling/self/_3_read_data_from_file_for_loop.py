a_file = open("example.py")

for line in a_file:
    print(line)

data=open("content.txt")
for line in data:
    print(line)

filename = 'write.text'
with open(filename,) as file_object:
    for line in file_object:
        print(line)
