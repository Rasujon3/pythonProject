def add(a,b):
    sum = a+b
    return sum

result = add(10,20)
print("Result = ",result)
result2 = add(20,20)
print("Result2 = ",result2)

# xxargs

def student(*details):
    print(details)

student(2001,"Sujon",3.82) #print as a tuples
student(2001,"Sujon",3.82,"Grade A in 9th semister.") #print as a tuples

def addition(*number):
    sum = 0
    for num in number:
       sum = sum + num
    print(sum)

addition(10,20)
addition(10,20,20)

#xxxargs

def students(**details):
    #print(details)
    print(details["name"])

students(id=2001,name="Sujon",cgpa=3.82) #print as a dictionary looks key value
students(id=173012001,name="RA Sujon",cgpa=3.82,results="Grade A in 9th semister.") #print as a dictionary looks key value

#lamda function

print((lambda a,b :a*a + 2*a*b + b*b)(2,3))




