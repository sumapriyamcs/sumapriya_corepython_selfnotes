#write a program to get the student grades as per the marks .
#example: take inputs from the user and he/she should have  more than 95 marks in
# three subjects then you should print gold medal.if he is having more than 90 he get distinction
#and he is having more than 75 and less than 90 he is having average
# and if he is having less than 75 he is having fail grade
#take 6 subjects from theuser
'''if he scores more than 90% distinction must and should in three subjects he get 90%
a=90
b=90
c=92
res=90 distinction
95% distinction +gold

a student will be awarded he scores between 75 to 90 in all subjects average
< 75 fail'''

#solution 1:

n=int(input("enter the number of subject marks"))
marks_list=[]
for i in range(1,n+1):
    marks=float(input("enter the marks"))
    marks_list.append(marks)
    marks_list.sort()
print(marks_list)
avg=sum(marks_list)/n
print(avg)
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
    print("fail")

#solution 2:
