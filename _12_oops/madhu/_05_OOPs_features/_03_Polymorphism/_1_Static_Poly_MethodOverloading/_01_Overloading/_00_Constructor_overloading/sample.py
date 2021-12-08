class Employee:

    def __init__(self, eid, name='suma', sal=1000):  # constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal
        print(self.eid, self.name, self.sal)

# Constructor Overloading

suma = Employee(100)
suma = Employee(101, "suma")
priya = Employee(102, 'priya', 20000)