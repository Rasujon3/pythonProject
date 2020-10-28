num = {1,2,3,4,5,5,9}
num2 = set([1,2,3,4,5,5,0,9])
num2.add(7)
print(num2)
num2.remove(7)
print(7 in num2)
print(4 in num2)
print(4 not in  num2)
print(num | num2) #union
print(num & num2) #intersection
print(num - num2) #difference