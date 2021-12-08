# scope of variable  LEGB Rule in python 

x = 100
print("Value of x1 :", x)

def get_data():
    # print("Value of x2 :", x)
    x = 25
    z = 200
    print("Value of x3 :", x)
    print("Value of z : ", z)

get_data()
##print("Value of z :", z)

print("Value of x4 :", x)

