file_obj = open("write_data1.txt", 'w')   # C:/Users/madhu/Desktop/write_data.txt
print("File type ", file_obj, type(file_obj))
data = input("Enter text : ")
file_obj.write(data)  # TextIOWrapper.write(file_obj, data)  emp.getdata(10) ==> Employee.getdata(emp,10)
file_obj.close()

file=open("write_data1.txt",'r')
print("file type",file,type(file))
#file.read(file)
#file.close()
f= open("data","w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
f.close()

f=open("write.text", "a+")
for i in range(2):
     f.write("Appended line %d\r\n" % (i+1))
f.close()

f=open("write_data1.txt", "r")
if f.mode == 'r':
    contents = f.read()
    print(contents)

def main():
   f = open("write_data1.txt", "r")
   f1=f.readline()
   #f1=f.readlines()
   for i in f1:
       print(i)
main()

python_file = open("example.py", "w")

python_file.write('print("Hello World!")')
python_file.close()

