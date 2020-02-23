num1 = input("숫자 1 입력 : ")
num2 = input("숫자 2 입력 : ")

try:
    num1 = int(num1)
    num2 = int(num2)

except ValueError as ex:
    print(ex)