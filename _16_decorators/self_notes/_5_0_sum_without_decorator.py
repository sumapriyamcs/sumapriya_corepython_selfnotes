def sum(num1, num2):
    res = num1 + num2
    return res

n1 = int(input("Enter number 1  :"))
n2 = int(input("Enter number 2  :"))

# validation logic
if n1 < 0 or n2 < 0:
    print("Please enter valid positive number")
else:
    print("Addition result :", sum(n1, n2))


def sum(n1,n2):
    res=n1+n2
    return res
if n1>=10 and n2<=20:
    print("valid result")
else:
    print("invalid data you entered")

def sum(l):
    res=0
    for i in l:
        res+=i
    return res
l=[1,2,3,4]
a=sum(l)
print(a)

def sum(t):
    res = 0
    for i in t:
        res += i
    return res


t = (4,6,8,9)
a = sum(t)
print(a)

def sum(set):
    res = 0
    for i in set:
        res += i
    return res


set={2,4,5,7,89,10}
a = sum(set)
print(a)