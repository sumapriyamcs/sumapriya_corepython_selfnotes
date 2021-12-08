# Python program to illustrate
# *kargs for variable number of keyword arguments

def myFun(**kwargs):
	for key, value in kwargs.items():
		print ("%s == %s" %(key, value))

# Driver code
myFun(first ='suma', mid ='for', last='life')


def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Suma", Lastname="puchalapalli", Age=24, Phone=9701517934)
intro(Firstname="ravi", Lastname="puchalapalli", Email="puchalapalliravikumar@gmail.com", Country="india", Age=53, Phone=9704904723)

def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="priya")
name = "priya"

def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(my_name="Suma", your_name="baba")
def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(
            name_1="suma priya",
            name_2="nayana",
            name_3="sirisha",
            name_4="moni",
            name_5="geetha",
            name_6="kavitha"
        )


def team(**details):
    print(type(details))

    for key, value in details.items():
        print("{}: {}".format(key, value))


team(Name="suma", Project="spark", Number="one Member")
