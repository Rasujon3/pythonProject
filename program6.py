
subjects = ["A","B","C","D","E","F","G","H","I","J"]

'''
print(subjects)
print(subjects[0])
print(subjects[2:])
print(subjects[-1:])

'''

print("L" in subjects)
print("L" not in subjects)

print(subjects + ["K",27])
print(len(subjects))
subjects.append("G")
print(subjects)
subjects.insert(2,"L")
print(subjects)
subjects.remove("G")
print(subjects)
subjects.sort()
print(subjects)
subjects.pop()
print(subjects)
#subjects.clear()
#print(subjects)
subjects2 = subjects.copy()
print(subjects2)
pos = subjects2.index("I")+1
print(pos)
pos1 = subjects2.count("I")
print(pos1)

num = list(range(20))
print(num)
print(num[2])

num = list(range(5,11))
print(num)

num = list(range(1,11,2))
print(num)

for x in subjects2:
    print(x)

#1 + 2 + 3 + 4 ...... + n

sum = 0
n = int(input("Enter the last number : "))
for x in range(1,n+1,1):
    sum = sum + x
print(sum)

#2 + 4 + 6 + 8 + 10 ...... + n

sum = 0
n = int(input("Enter the last number : "))
for x in range(2,n+1,2):
    sum = sum + x
print(sum)