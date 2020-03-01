# -*- coding: utf-8 -*-


# 도전 2. 형변환. 문자열을 정수로 바꾸기.
# 문자열 "3"을 정수 3으로 바꾸시오. 구글 검색
# temp2 = "3"

# 도전 3. 문자열에서 가장 큰 수를 찾으시오.
# a. 문자열 자르기 --> 리스트를 얻게 됨.
# b. 문자열을 정수 리스트로 만든다.
# c. 정수리스트를 오름차순 정렬하시오
# d. 정수리스트에서 최대값을 찾는다.
"""
temp3 = "74 874 9883 73 9 73646 774"
array1 = temp3.strip().split(" ")
print(array1)  # ['74', '874', '9883', '73', '9', '73646', '774']

array2 = []
for n in array1:
    n = int(n)
    array2.append(n)

print(array2)  # [74, 874, 9883, 73, 9, 73646, 774]
"""
'''
temp3 = "74 874 9883 73 9 73646 774"
array1 = temp3.split(" ")
sortArray = list(map(int, array1))
print(sorted(sortArray))
'''


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
    print(lst[len(lst)-1])
    print(max(lst))


if __main__ == "__name__":
    main()
