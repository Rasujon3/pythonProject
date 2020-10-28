"""class Student: #class create
    roll = ""
    gpa = ""

rahim = Student() #object create hoye geche vaba jay...
print(isinstance(rahim,Student)) #make sure this is obj or not
rahim.roll = 2001
rahim.gpa = 3.83
print(f"Roll : {rahim.roll}, GPA : {rahim.gpa}")

class Student2: #class create
    roll = ""
    gpa = ""

rahim2 = Student2() #object create hoye geche vaba jay...
print(isinstance(rahim2,Student2)) #make sure this is obj or not
rahim2.roll = 2002
rahim2.gpa = 3.82
print(f"Roll : {rahim2.roll}, GPA : {rahim2.gpa}")

#method
class Student: #class create
    roll = ""
    gpa = ""

    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")
rahim = Student() #object create hoye geche vaba jay...
#print(isinstance(rahim,Student)) #make sure this is obj or not
rahim.set_value(2001,3.83)
rahim.display()

#Constructor

class Student: #class create
    roll = ""
    gpa = ""

    def __init__(self,roll,gpa): #creating constructor
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")
rahim = Student(2001,3.83) #object create hoye geche vaba jay...
#print(isinstance(rahim,Student)) #make sure this is obj or not
rahim.display()

#Exercise

class triangle: #class create

    def __init__(self,base,height): #creating constructor
        self.base = base
        self.height = height

    def calculate_area(self):
        area= self.base * self.height * 0.5
        print("Area : ",area)


t1 = triangle(10,20) #object create hoye geche vaba jay...
t1.calculate_area()
t2 = triangle(20,30) #object create hoye geche vaba jay...
t2.calculate_area()

#inheritance
class phone:
    def call(self):
        print("call me")
    def mgs(self):
        print("mgs me")

class nokia(phone):
    def photo(self):
        print("photo me")

n = nokia()
n.call()
n.mgs()
n.photo()"""

#Method Overriding

class phone:
    def __init__(self):
     print("in phone class")

class samsang(phone):
    def __init__(self):
        print("In samsang class")#override
        super().__init__()#super class call

s = samsang()










