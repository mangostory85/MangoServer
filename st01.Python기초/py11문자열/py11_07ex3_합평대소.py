# ���ڿ����� ���� ū ���� ã���ÿ�.
# a. ���ڿ� �ڸ��� --> ����Ʈ�� ��� ��.
# b. ���ڿ��� ���� ����Ʈ�� �����.
# c. ��������Ʈ�� �������� �����Ͻÿ�
# d. ��������Ʈ���� �ִ밪�� ã�´�.
# e. ��������Ʈ�� �հ�, ���, �ִ밪 �׸��� �ּҰ��� ���Ͻÿ�.

def main():
    temp3 = "74 874 9883 73 9 73646 774"
    lst = temp3.split(" ")
    print(type(lst), lst)
    print(lst[0], type(lst[0]))
    print(lst[1], type(lst[1]))
    print(lst[2], type(lst[2]))

    lst[0] = int(lst[0])
    print(type(lst[0]), lst[0])

    for i in range(0, len(lst), 1):
        lst[i] = int(lst[i])
    print(type(lst), lst)
    lst = sorted(lst)
    
    print(max(lst))
    print(min(lst))
    print(sum(lst))
    print(sum(lst)/len(lst))
if __name__ == "name":
    main()