num1 = input("첫번째 수를 입력하세요. :")
num2 = input("두번째 수를 입력하세요. :")
num3 = input("세번째 수를 입력하세요. :")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 > num2 :
    if num1 > num3 :
        print("입력 받은 수 중 가장 큰 수는 %d 입니다."%num1)
    else :
        print("입력 받은 수 중 가장 큰 수는 %d 입니다."%num3)

else :
    if num2 > num3 :
        print("입력 받은 수 중 가장 큰 수는 %d 입니다."%num2)
    else :
        print("입력 받은 수 중 가장 큰 수는 %d 입니다."%num3)
