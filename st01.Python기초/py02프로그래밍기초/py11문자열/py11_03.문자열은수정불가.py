# 문자열은 수정할 수 없다.
# 새롭게 메모리가 할당된다는 의미

str1 = "abc"
print("str1 주소값 출력", id(str1))
print()

str2 = str1
print("str2 주소값 출력", id(str2))
print()

str1 = "efg"
print("str1 주소값 출력", id(str1))
print("str2 주소값 출력", id(str2))
print()