
#oops programs:

class Student:

    # 1. STATE
    def __init__(self, r_no, name, marks):
        self.r_no = r_no
        self.name = name
        self.marks = marks

    # 2. BEHAVIOR
    def get_sinfo(self):
        print("Student details are ", self.r_no, self.name, self.marks)

suma= Student(84, 'sumapriya puchalapalli', 75)
suma.get_sinfo()


class Employee:

    # 1. STATE
    def __init__(self, empid, name, sal):
        self.empid = empid
        self.name = name
        self.sal = sal

    # 2. BEHAVIOR
    def get_einfo(self):
        print("Employee details are ", self.empid, self.name, self.sal)

# object creation
suma = Employee(100, 'suma priya', 30000)    # x = 10
suma.get_einfo()


class Laptop:
    #1.STATE
    def __init__(self,lname,cost,ram,windows):
        self.lname= lname
        self.cost=cost
        self.ram=ram
        self.windows=windows
    #2. BEHAVIOUR
    def get_linfo(self):
        print("laptop details are",self.lname,self.cost,self.ram,self.windows)
#object creation
acer=Laptop("acer",30000,4,10)
acer.get_linfo()


class Dress:
    #1.STATE
    def __init__(self,dtype,size,colour,cost):
          self.dtype=dtype
          self.size=size
          self.colour=colour
          self.cost=cost

    # 2. BEHAVIOR
    def get_dinfo(self):
        print("Dress details are ", self.dtype, self.size, self.colour,self.cost)

# object creation
punjabhi = Dress("punjabhi", "s","green",1500)
punjabhi.get_dinfo()



class Bag:

    #1.STATE
    def __init__(self,btype,colour,price,brand):
         self.btype=btype
         self.colour=colour
         self.price=price
         self.brand=brand
    #2.BEHAVIOUR
    def get_binfo(self):
        print("bag deatils are", self.btype,self.colour,self.price,self.brand)
#object creation
clgbag=Bag("collegebag","pink",1000,"genie")
clgbag.get_binfo()



class Bottle:
    #1.STATE
    def __init__(self,brand,colour,price,btype,shape):
        self.brand=brand
        self.colour=colour
        self.price=price
        self.btype=btype
        self.shape=shape
    #2.BEHAVIOUR
    def get_binfo(self):
        print("bottle details are", self.brand,self.btype,self.price,self.colour,self.shape)
water=Bottle("milton","plastic","200","white","cylinder")
water.get_binfo()


class Chair():
    #1.STATE
    def __init__(self,brand,colour,price,ctype):
        self.brand=brand
        self.colour=colour
        self.price=price
        self.ctype=ctype
    #2.BEHAVIOUR
    def get_cinfo(self):
        print("chair details are",self.brand,self.colour,self.price,self.ctype)
wheel=Chair("ergonomic","black",5000,"adjustable")
wheel.get_cinfo()



class Table():
    #1.STATE
    def __init__(self,ttable,colour,brand,price,weight,width,warranty):
         self.ttable=ttable
         self.colour=colour
         self.brand=brand
         self.price=price
         self.weight=weight
         self.width=width
         self.warranty=warranty
    #2.BEHAVIOUR
    def get_tinfo(self):
        print("Table details are",self.ttable,self.colour,self.brand,self.price,self.weight, self.width, self.warranty)

#object creation
computer=Table("wood","white","EFC",10000,"18kg","36inch","1year")
computer.get_tinfo()

class Baloon():
    #1.STATE
    def __init__(self,brand,colour,shape,price,bdesign):
            self.brand=brand
            self.colour=colour
            self.shape=shape
            self.price=price
            self.bdesign=bdesign
    #2.BEHAVIOUR
    def get_binfo(self):
        print("Baloon details are", self.brand,self.colour,self.shape,self.price,self.bdesign)

##object creation
bborn=Baloon("anayatech","red","heart",400,"plain")
bborn.get_binfo()


class Fan():
    #1.STATE
    def __init__(self,brand,price,colour,shape,ftype,warranty,material):
        self.brand=brand
        self.price=price
        self.colour=colour
        self.shape=shape
        self.ftype=ftype
        self.warranty=warranty
        self.material=material
    #2.BEHAVIOUR
    def get_finfo(self):
        print("fan details are",self.brand,self.price,self.colour,self.shape,self.ftype,self.warranty,self.material)
#object creation
home=Fan("usha",3000,"white","round","wall mount","1 year","plastic")
home.get_finfo()


class Door():
    #1. STATIC
    def __init__(self,price,colour,shape,dtype):
        self.price=price
        self.colour=colour
        self.shape=shape
        self.dtype=dtype
    #2.BEHAVIOUR
    def get_dinfo(self):
        print("door details are", self.price,self.colour,self.shape,self.dtype)
#object creation
usage=Door(40000,"brown","rectangular","wood")
usage.get_dinfo()



class Projector():
    #1.STATE
    def __init__(self,brand,colour,shape,price,controlmodel,warranty):
        self.brand=brand
        self.colour=colour
        self.shape=shape
        self.price=price
        self.controlmodel=controlmodel
        self.warranty=warranty
    #2.BEHAVIOUR
    def get_pinfo(self):
        print("projector details are",self.brand,self.colour,self.price,self.controlmodel,self.warranty,self.shape)
#object creation
pro=Projector("epson","white",80000,"remote","1 year","rectangular")
pro.get_pinfo()


class Theatre():
    #1.STATE
    def __init__(self,tname,location,screens,showtiming,ticketprice,moviename):
        self.tname=tname
        self.location=location
        self.screens=screens
        self.showtiming=showtiming
        self.ticketprice=ticketprice
        self.moviename=moviename

    #2. BEHAVIOUR
    def get_tinfo(self):
        print("theatre details are", self.tname,self.location,self.screens,self.showtiming,self.ticketprice,self.moviename)
#object creation
the=Theatre("svc","nellore",3,"9am and 1 pm and 6pm and 9pm",200,"pelli sandhadi")
the.get_tinfo()


class College():
    #1.STATE
    def __init__(self,cname,location,departments,clgtype,principal):
        self.cname=cname
        self.location=location
        self.departments=departments
        self.clgtype=clgtype
        self.principal=principal
    #2.BEHAVIOUR
    def get_cinfo(self):
        print("college details are",self.cname,self.location,self.departments,self.clgtype,self.principal)
#object creation
clg=College("jntua","anantapur","cse and mech and civil and ece and eee","autonomus","dr.shankara raju")
clg.get_cinfo()


class Market():
    #1.STATE
    def __init__(self,mname,location,timings,availablethings):
        self.mname=mname
        self.location=location
        self.timings=timings
        self.availablethings=availablethings
    #2.BEHAVIOUR
    def get_minfo(self):
          print("market details are",self.mname,self.location,self.timings,self.availablethings)
#object creation
mar=Market("kr market","bangalore","always open","vegetables,fruits,flowers,homemade things etc..")
mar.get_minfo()


class Home():
    #1.STATE
    def __init__(self,location,htype,area,livingpeople,jobholders):
        self.location=location
        self.htype=htype
        self.area=area
        self.livingpeople=livingpeople
        self.jobholders=jobholders
    #2.BEHAVIOUR
    def get_hinfo(self):
        print("home details are",self.location,self.htype,self.livingpeople,self.jobholders,self.area)
#object creation
live=Home("nellore","villa",4,"three","balaji nagar")
live.get_hinfo()


class Busstand():
    #1.STATE
    def __init__(self,name,location,typesofbusstand,timingsforrunning,platforms,busnos,brandsofbuses):
        self.name=name
        self.location=location
        self.typesofbusstand=typesofbusstand
        self.timingsforrunning=timingsforrunning
        self.platforms=platforms
        self.busnos=busnos
        self.brandsofbuses=brandsofbuses
    #2.BEHAVIOUR
    def get_binfo(self):
        print("bus details are", self.location,self.typesofbusstand,self.timingsforrunning,self.platforms,self.busnos,self.brandsofbuses)
##object creation
running=Busstand("kempegowda","bangalore","gov and private","6 to 11 for private and gov for always","6542 and 3423etc","40 and 41 ,43 etc","garuda and amaravathi etc")
running.get_binfo()


class Railway():
    #1.STATE
    def __init__(self,name,location,platforms,importandexporting,birthtype,ticketprice,typeoftrains):
        self.name=name
        self.location=location
        self.platforms=platforms
        self.importandexporting=importandexporting
        self.birthtype=birthtype
        self.ticketprice=ticketprice
        self.typeoftrains=typeoftrains
    #2.BEHAVIOUR
    def get_tinfo(self):
        print("railwaydetails details are", self.name,self.location,self.platforms,self.importandexporting,self.birthtype,self.ticketprice,self.typeoftrains)
##object creation
run=Railway("yeswanthpur junc , bangalorecant,krishnarajapuram etc","karnataka,bangalore","5","available","general ,a/c, sleeper","based on birthtype ,starting from 150","express,general etc")
run.get_tinfo()


class Hotel():
    #1.STATE
    def __init__(self,name,area,rating,typeoffood,orderavail,taste):
        self.name=name
        self.area=area
        self.rating=rating
        self.typeoffood=typeoffood
        self.orderavail=orderavail
        self.taste=taste
    #2.BEHAVIOUR
    def get_hinfo(self):
        print("hotel details are",self.name,self.area,self.rating,self.typeoffood,self.orderavail,self.taste)

#object creation
htl=Hotel("amaravathi","vrc center","4.5","veg/nonveg","yes","good")
htl.get_hinfo()

class Pen():
    #1.STATE
    def __init__(self,brand,colour,price,typeofpen,shape):
        self.brand=brand
        self.colour=colour
        self.price=price
        self.typeofpen=typeofpen
        self.shape=shape
    #2.BEHAVIOUR
    def get_pdet(self):
        print("pen details are",self.brand,self.colour,self.price,self.typeofpen,self.shape)
#object creation
p=Pen("ballpoint","blue,green,orange,black etc","10 and 20 etc","red/black/green/blue","cylinder")
p.get_pdet()


class Earphone():
    #1.STATE
    def __init__(self,brandsn,typeofe,colours,warranty,price):
        self.brandsn=brandsn
        self.typeofe=typeofe
        self.colours=colours
        self.warranty=warranty
        self.price=price
    #2.BEHAVIOUR
    def get_ed(self):
        print("earphone details are",self.brandsn,self.typeofe,self.colours,self.warranty,self.price)
#object creation
ear=Earphone("iphone/oneplus/realme/oppo/samsung etc","earphones/earbuds/wirelessbluetooth etc","black/blue/white etc","min 6 to 1 year","based on brand")
ear.get_ed()


class Bike():
    #1.STATE
    def __init__(self,biken,price,model,mileage):
        self.biken=biken
        self.price=price
        self.model=model
        self.mileage=mileage
    #2.BEHAVIOUR
    def get_bdetail(self):
        print("bike details are",self.biken,self.price,self.model,self.mileage)
#object creation
bi=Bike("bmw/yamaha/herohonda/r15","min 1 lac","x7/v3/xtreme 160r","10.5kmpl/48.75kmpletc")
bi.get_bdetail()


class phone():
    #1.STATE
    def __init__(self,name,price,gb,colour,warranty):
         self.name=name
         self.price=price
         self.gb=gb

         self.colour=colour
         self.warranty=warranty
    #2.BEHAVIOUR
    def get_pd(self):
         print("phone details are",self.name,self.price.self.gb,self.colour,self.warranty)
#object creation
ph=phone("iphonexr","720000","128gb","peach","1year")
ph.get_pd()










































"""