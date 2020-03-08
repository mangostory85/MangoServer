import math  # PI=3.141592...값을 사용하기 위해


def circle(radius):
    면적 = math.pi * radius * radius
    둘레 = 2 * math.pi * radius
    return (면적, 둘레)  # 튜플 자료구조 1개를 리턴하는 것


def main():
    str = input("원의 반지름을 입력하시오")
    radius = float(str)  # 문자열을 실수로 형변환
    # 원의 넓이와 둘레를 계산
    (x, y) = circle(radius)
    tmp = "원의 넓이는 %10.4f, 둘레는 %10.4f입니다." % (x, y)
    print(tmp)

if __name__ == "__main__":
    main()
