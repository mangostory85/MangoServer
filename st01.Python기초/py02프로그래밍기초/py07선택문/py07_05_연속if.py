# py04_02_ifelse

# 하나의 점수를 입력 받고, 입력 받은 점수에 해당하는 학점을 출력하는 프로그램을 작성하시오.
# 입력 받는 정수는 0~100까지이고
num = input("점수를 입력하세요")
num = int(num)
# 90점 이상이면 A,
if num >= 101:
    print("숫자를 잘못 입력하셨습니다.")
elif num >= 90:
    print("A")
# 80점 이상이면 B,
elif num >= 80:
    print("B")
# 70점 이상이면 C,
elif num >= 70:
    print("C")
# 60점 이상이면 D,
elif num >= 60:
    print("D")
# 나머지는 F
else:
    print("F")


    
