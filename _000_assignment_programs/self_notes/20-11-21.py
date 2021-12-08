'''We have to take input of subjects and marks from user
If No.of subjects is between 3 - 7
	We have to find percentage of all subjects
	If total percentage is greater than 90 --> awarded distinction
	If total percentage is between 75 to 90 --> awarded average
	If total percentage is less than 75:
		chance is given only if he score less than 75% in 3 subjects
		if he score less than 75% in more than 3 subjects he is given fail


If No.of subjects is greater than 7
	we have to find percentage of all subjects
	If total percentage is greater than 90 --> awarded distinction
	If total percentage is between 75 to 90 --> awarded average
	If total percentage is less than 75:
		chance is given only if the fail subjects average should be between 65 - 75
		else he will be given fail
		if he fail in more than 5 subjects he should be debard'''
'''
sub1=int(input("enter the science marks"))
sub2=int(input("enter the maths marks"))
sub3=int(input("enter the social marks"))
sub4=int(input("enter the english marks"))
sub5=int(input("enter the telugu marks"))
sub6=int(input("enter the hindi marks"))
sub7=int(input("enter the malayalam marks"))
total=(sub1+sub2+sub3+sub4+sub5+sub6+sub7)
print(total)
mar1=int(input("enter the marks"))
mar2=int(input("enter the marks"))
mar3=int(input("enter the marks"))
mar4=int(input("enter the marks"))
mar5=int(input("enter the marks"))
mar6=int(input("enter the marks"))
mar7=int(input("enter the marks"))
to=mar1+mar2+mar3+mar4+mar5+mar6+mar7
pint(to)
per=(mar1+mar2+mar3+mar4+mar5+mar6+mar7/700)*100
print(per)
if per>=90:
    print("distinction")
elif per>=75 and per<=90:
    print("average")
elif per<=75:
    print("fail")
avg=to/7
print(avg)
count=0
for i in range(total):
  if per>=75:
      count+=1
if count>=3:
    print("fail")'''

'''
count=0
for i in range(n):
    if marks_list[i]>=95:
        count+=1
if avg>=90:
    if count>=3:
        print("gold medal")
    else:
        print("distinction")
elif avg>75 and avg<90:
    print("average")
else:
    print("fail")'''


def func1(n):
    marks_dict = dict()
    marks_list = []
    for i in range(1, n + 1):
        subject = input(f'enter the name of the subject {i} : ')
        marks = int(input(f'enter the marks for the {subject} : '))
        marks_dict.update({subject: marks})
        marks_list.append(marks)

    avg = (sum(marks_list)) / n

    count = 0
    for i in marks_list:
        if i >= 75.0:
            count = count + 1

    if avg >= 90.0:
        print('distinction')

    elif avg >= 75.0 and avg <= 90.0:
        print('average')

    elif avg < 75.0:
        if count <= 3:
            print('pass')
        else:
            print('failed')

    for i, j in marks_dict.items():
        print(i, ' : ', j)


def func2(n):
    marks_dict = dict()
    marks_list = []
    for i in range(1, n + 1):
        subject = input(f'enter the name fo the  subject {i}  : ')
        marks = int(input(f'enter the marks for the {subject} : '))
        marks_dict.update({subject: marks})
        marks_list.append(marks)

    avg = (sum(marks_list) / n)

    count = 0
    for i in marks_list:
        if i >= 65.0 and i <= 75.0:
            count = count + 1

    if avg >= 90.0:
        print('distinction')

    elif avg >= 75.0 and avg <= 90.0:
        print('average')

    elif avg <= 75.0:
        if count == 3:
            print('passed')

        elif count == 4:
            print('failed')

        elif count >= 5:
            print('debarred')

    for i, j in marks_dict.items():
        print(i, ' : ', j)


number = int(input('enter the number of subjects: '))

if 3 <= number <= 7:
    func1(number)

elif number > 7:
    func2(number)

elif number < 3:
    print('enter minimum subject 3')


num=int(input("Enter no of subjects : "))
sub_lst=[]
marks_lst=[]
if 3 <= num <= 7:
 for i in range(1, num + 1):
    subject = input("enter the name of " + str(i) + " subject  : ")
    marks = int(input("enter the marks of " + subject + " " + "subject :"))
    if  marks >=100:
     print("Please enter valid marks between 0 to 100")
    else:
     sub_lst.append(subject)
     marks_lst.append(marks)
 print(sub_lst)
 print(marks_lst)

avg = (sum(marks_lst) / num)
count = 0

for i in marks_lst:
    if i >= 75.0:
     count = count + 1
if avg >= 90:
    print("Distinction")
elif 75<=avg<=90:
  print("Average")
elif avg<75:
    if count > 3:
        print("Pass")
    else:
        print("Fail")


if num > 7:
    for i in range(1, num + 1):
        subject = input("Enter the name of " + str(i) + " subject  : ")
        marks = int(input("Enter the marks of " + subject + " " + "subject :"))
        if marks >= 100:
            print("Please enter valid marks between 0 to 100")
        else:
         sub_lst.append(subject)
         marks_lst.append(marks)
    print(sub_lst)
    print(marks_lst)

    avg = (sum(marks_lst) / num)
    count = 0
    avg1 = 0
    add=0
    for i in marks_lst:
        if i <= 65:
         add+=i
         count = count + 1
    avg1 = add/count
    if avg < 75:
     if 65 <= avg1 <= 75:
        print('passed')
     elif count >= 5:
         print('debarred')
     else:
        print('failed')

    elif avg >= 90:
        print("Distinction")

    elif 75 <= avg <= 90:
        print("Average")

if num < 3:
 print("Enter more than three subject")


