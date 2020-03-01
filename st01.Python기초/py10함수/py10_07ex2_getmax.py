# coding=<utf-8>
# 사용자 함수 만들기
# 두 개의 정수가 주어지면 두수 중에서 더 큰 수를 찾아서 이것을 반환하는 함수를 만들어보자.

#x : 매개변수
#y : 매개변수


def getmax(x, y):
    result = None  # None : 값이 없음

    if x > y:
        return = x  # x반환
    else:
        return = y  # y반환

    return result


def myinput(mesg):
    try:
        n1 = input(mesg)
        n1 = int(n1)
    except ValueError as ex:
        print(ex)

    return n1

# main()함수를 사용하는 이유?
# 프로그래밍에서 지향하는 방식 -> 전역변수 사용X


def main():
    # 입력처리
    n1 = myinput("첫번째 정수 입력 : ")
    n2 = myinput("두번째 정수 입력 : ")
    # 최대 값 출력
    val = getmax(n1, n2)
    print("최대값은 : ", val)


main()
