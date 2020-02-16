a = input("첫번째 점수")
b = input("두번째 점수")

try:
    a = int(a)
    b = int(b)
    avg = a+b/2
except ValueError:
    pass


if avg >= 160 :
    print("합격")
else :
    print("불합격")