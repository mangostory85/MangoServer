# coding=<utf-8>
# ����� �Լ� �����
# �� ���� ������ �־����� �μ� �߿��� �� ū ���� ã�Ƽ� �̰��� ��ȯ�ϴ� �Լ��� ������.

#x : �Ű�����
#y : �Ű�����


def getmax(x, y):
    result = None  # None : ���� ����

    if x > y:
        return = x  # x��ȯ
    else:
        return = y  # y��ȯ

    return result


def myinput(mesg):
    try:
        n1 = input(mesg)
        n1 = int(n1)
    except ValueError as ex:
        print(ex)

    return n1

# main()�Լ��� ����ϴ� ����?
# ���α׷��ֿ��� �����ϴ� ��� -> �������� ���X


def main():
    # �Է�ó��
    n1 = myinput("ù��° ���� �Է� : ")
    n2 = myinput("�ι�° ���� �Է� : ")
    # �ִ� �� ���
    val = getmax(n1, n2)
    print("�ִ밪�� : ", val)


main()
