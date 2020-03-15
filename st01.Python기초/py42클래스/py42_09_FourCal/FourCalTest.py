
# 작업 순서
# 1. 모듈 또는 클래스 import
# 2. main() 메서드 만들기
#     인스턴스 생성
# 3. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()

# 코딩 하기

import FourCal


def main():
    fnum = input("First num : ")
    snum = input("Second num : ")
    result = FourCal.FourCal(int(fnum), int(snum))
    """
    result = FourCal.FourCal(2, 4)
    print("First num : ", result.first)
    print("Second num : ", result.second)
    """
    print("Add : ", result.add())
    print("Minus : ", result.minus())
    print("Mul : ", result.mul())
    print("Div : %6f" % result.div())


if __name__ == "__main__":
    main()
