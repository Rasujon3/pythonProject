#map
def square(x):
    return x*x

num = [1,2,3,4,5]

result = list(map(square,num))
print(result)

#List Comprehensions : [expression for item in list]
result = [x*x for x in num]
print(result)

#filter function

num = [1,2,3,4,5]
result = list(filter(lambda x:x%2==0,num))
print(result)

#List Comprehensions : [expression for item in list]
#result = [x%2==0 for x in num]
result = [x for x in num if x%2==0]
print(result)

# Zip Function
roll = [2001,2024,2057]
name = ["Sujon","Naim","Arin"]
print(list(zip(roll,name,"ABC")))

#Recursion

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))

#Exception Handling (part-1)
try:
    list = [20,0,4]
    result = list[0] / list[3]
    print(result)
    print('Done')
except ZeroDivisionError:
    print("Dividing by zero is not possible.")
finally:
    print("Successfully.")
"""except IndexError:
    print("Index error.")
"""

#Swapping
a=10
b=20
a,b = b,a
print("a = ",a)
print("b = ",b)

