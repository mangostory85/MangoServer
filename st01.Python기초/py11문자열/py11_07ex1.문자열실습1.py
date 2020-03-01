
# 0번째부터 12번째 자리까지 있음.
# prov 길이는 13이다.
prov = "A barking Dog"


#################################
# 문자열 함수 / 문자열 메서드
#################################
"""
# 문자열 길이: len().  prov의 길이를 출력하시오
length = len(prov)
print("prove 문자열 길이:", length)
# 첫번째 b 문자를 찾고 위치를 출력하시오.
pos1 = prov.find("b")
print("첫번째 b 문자의 위치는:", pos1)
# 문자열에 "Dog"가 있으면 "Dog있음"을 없으면 "Dog없음" 을 출력하시오
# "Dog 있음"
# 문자열 치환: replace()
# prov 문자열에 Dog가 들어 있으면 Cat으로 바꾸어 출력하고
# 아니면 prov 출력하시오.
if prov.find("Dag") >= 0:
    s07 = prov.replace("Dog", "Cat")
    print(s07)
else:
    print(prov)
# 문자열 prov 를 공백을 기준으로 자르고 그 결과를 출력하시오.
arr = prov.split(" ")
for i in arr:
    print(i, end=", ")
"""
# 1
prov = "A birking Dog"
length = len(prov)
print("prove의 문자열 길이 : ", length)
# 2
find1 = prov.find("b")
print("첫번째 b 문자의 위치는 : ", find1)
# 3
find2 = prov.find("Dog")
if find2 == -1:
    print("Dog없음")
else:
    print("Dog있음")
# 4
if prov.find("Dog"):
    re1 = prov.replace("Dog", "Cat")
    print(re1)
# 5
array1 = prov.split(" ")
print(type(array1), array1)
print(array1[1])
"""
for i in array1:
    print(i, end=",")
"""
