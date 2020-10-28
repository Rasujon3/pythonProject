
num1 = 20
num2 = 30
num3 = 80

max = num1 if num1>num2 else num2
print(max)

if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
if num2>num1:
    if num2>num3:
        print(num2)
    else:
        print(num3)