num1 = input("첫번째 수를 입력하세요. :")
num2 = input("두번째 수를 입력하세요. :")
num3 = input("세번째 수를 입력하세요. :")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 < num2 < num3:
    print("가장 작은 수는 %d" % num1)
elif num2 < num1 < num3:
    print("가장 작은 수는 %d" % num2)
else:
    print("가장 작은 수는 %d" % num3)
"""
if num1 < num2:
    if num1 < num3:
        print("가장 작은 수는 %d" % num1)
    elif num1 > num3:
        print("가장 작은 수는 %d" % num3)
    else:
        print("가장 작은 수는 %d" % num2)

if num2 < num1:
    if num2 < num3:
        print("가장 작은 수는 %d" % num2)
    elif num2 > num3:
        print("가장 작은 수는 %d" % num3)
    else:
        print("가장 작은 수는 %d" % num1)

if num3 < num1:
    if num3 < num2:
        print("가장 작은 수는 %d" % num3)
    elif num3 > num2:
        print("가장 작은 수는 %d" % num2)
    else:
        print("가장 작은 수는 %d" % num1)
"""
