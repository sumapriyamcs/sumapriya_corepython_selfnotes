'''
First of all, what is a CSV ?
CSV (Comma Separated Values) is a simple file format used to store tabular data,
such as a spreadsheet or database. A CSV file stores tabular data (numbers and text)
in plain text. Each line of the file is a data record. Each record consists of
one or more fields, separated by commas.
The use of the comma as a field separator is the source of the name for this file format.
'''
'''
import csv

with open('name.csv', 'r') as fp:
    reader = csv.reader(fp)  # read file

    with open('new.csv', 'w') as fq:
        writer = csv.writer(fq)

        for line in reader:  # To iterrate over each row
            writer.writerow(line)  # write line to new file
print(fp)
print(fq)

import csv
with open("hello.csv","r")as p:
    reader=csv.reader(p)

    with open("new.csv","w")as s:
        writer=csv.writer(s)

        for line in reader:
            writer.writerow(line)
print(p)
print(s)

import csv
with open("name.csv","r")as p:
    reader=csv.reader(p)
    with open ("new.csv","w")as r:
        writer=csv.writer(r)
        for line in reader:
            writer.writerow(line)
print(p)
print(r)'''
'''
# importing the csv module
import csv

# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

# name of csv file
filename = "universityrecords.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)
print(csvfile)

# importing the csv module
import csv

# my data rows as dictionary objects
mydict = [{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
          {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
          {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]

# field names
fields = ['name', 'branch', 'year', 'cgpa']

# name of csv file
filename = "records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(mydict)
print(csvfile)

import csv
file = open("Salary_Data.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()

import csv
rows = []
with open("Salary_Data.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)
print(file)


with open('Salary.csv') as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]
print(header)
print(rows)
print(file)
'''
'''
header = ['Name', 'M1 Score', 'M2 Score']
data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]
filename = 'Student_scores.csv'
with open(filename, 'w') as file:
    for header in header:
        file.write(str(header)+', ')
    file.write('n')
    for row in data:
        for x in row:
            file.write(str(x)+', ')
        file.write('n')
print(file)'''

'''
import csv
with open('people.csv', 'r') as file:
    reader = csv.reader(file)

    with open('yash.csv','w')as file2:
        writer = csv.writer(file2)

    for row in reader:
        print(row)
   # for line in reader:  # To iterrate over each row
    #        writer.writerow(line)
print(file)
print(file2)
'''
