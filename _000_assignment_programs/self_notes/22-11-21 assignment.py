'''user should specify how many months your calaculating
months=12,3 etc
emp id and salary
house rent:
basic allowance ,special allowance,tax
res=ht+ba+sa
res-tax
net amoount/sal
expenditure-4,food,rent,
  for expenditure
    saving    netsaving in negative -u r loser
s find
    + yu are great'''

months=int(input("enter for how many months you are going to calaculating"))
name=input("enter the user name")
empid=int(input("enter the employee id"))
final1=0
li=[]
if months>=1:
    for i in range(months):
        basic= int(input("enter the salary"))
        hrent=int(input("enter the house rent"))
        basicallowance=int(input("enter he basic allowance"))
        specialallowance=int(input("enter the special allowance"))
        tax=int(input("enter the tax"))
        total=basic+hrent+basicallowance+specialallowance+tax
        final=(basic+hrent+basicallowance+specialallowance)-tax
        li.append(final)
        print(li)
        print(total)
    final1=sum(li)
exp=int(input("enter number of expenditure"))
final2=0
li2=[]
for j in range(exp):
    n = input("do u have expenditures")
    if n=='yes':
        n1 = int(input("how many types of expenditure you are having"))
        n2=input(str(" what type of expenditures you are having"))
        food=int(input("enter the food ammount"))
        shopping=int(input("enter the shooping ammount"))
        a=(food+shopping)
        li2.append(a)
        final2=sum(li2)
    #total=sum-salary
    #print(total)
    else:
     print("i dont want to continue further because i am not having any expenditures so i want to quite")
print("the final ammount we are having is",final1)
netsaving=final1-final2
print(netsaving)
#savings=total-salary
#print(savings)
#net sal-ammount=totalsavings
#print(total savings)
if netsaving<=0:
    print("you are a looser")
else:
    print("you are great")

'''
def cal():
    months = int(input("enter for how many months you are going to calaculating"))
    name = input("enter the user name")
    empid = int(input("enter the employee id"))
    final1 = 0
    li = []
    if months >= 1:
        for i in range(months):
            basic = int(input("enter the salary"))
            hrent = int(input("enter the house rent"))
            basicallowance = int(input("enter he basic allowance"))
            specialallowance = int(input("enter the special allowance"))
            tax = int(input("enter the tax"))
            final = (basic + hrent + basicallowance + specialallowance) - tax
            li.append(final)
            print(li)
        final1 = sum(li)
    exp = int(input("enter number of expenditure"))
    final2 = 0
    li2 = []
    for j in range(exp):
        food = int(input("enter the food ammount"))
        shopping = int(input("enter the shooping ammount"))
        a = (food + shopping)
        li2.append(a)
        final2 = sum(li2)
        total=sum-salary
        print(total)
    netsaving = final1 - final2
    print(netsaving)
    #savings=total-salary
    # print(savings)
    # net sal-ammount=totalsavings
    # print(total savings)
    if netsaving <= 0:
        print("you are a looser")
    else:
        print("you are great")
cal()
'''
'''
months=int(input("enter for how many months you are going to calaculating"))
name=input("enter the user name")
empid=int(input("enter the employee id"))
to=0
l1=[]
while months>=1:
   # for i in range(months):
        basic= int(input("enter the salary"))
        hrent=int(input("enter the house rent"))
        basicallowance=int(input("enter he basic allowance"))
        specialallowance=int(input("enter the special allowance"))
        tax=int(input("enter the tax"))
        total=basic+hrent+basicallowance+specialallowance+tax
        final=(basic+hrent+basicallowance+specialallowance)-tax
        l1.append(final)
        print(l1)
        print(total)
to=sum(l1)
print(to)
exp=int(input("enter number of expenditure"))
fi=0
l2=[]
for j in range(exp):
        n = input("do u have expenditures")
        if n=='yes':
            n1 = int(input("how many types of expenditure you are having"))
            n2=input(str(" what type of expenditures you are having"))
            food=int(input("enter the food ammount"))
            shopping=int(input("enter the shooping ammount"))
            a=(food+shopping)
            l2.append(a)
            fi=sum(l2)
    #total=sum-salary
    #print(total)
        else:
             print("i dont want to continue further because i am not having any expenditures so i want to quite")
print("the final ammount we are having is",to)
netsaving=to-fi
print(netsaving)
#savings=total-salary
#print(savings)
#net sal-ammount=totalsavings
#print(total savings)
if netsaving<=0:
    print("you are a looser")
else:
    print("you are great")
'''
