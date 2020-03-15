# 딕셔너리의 CRUD3S
# C: create.
# R: read
# U: update
# D: delete
# S: search
# S: sort
# S: shuffle

# 딕셔너리 선언하기
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "소금", "치자"],
    "origin": "필리핀"
}
# 요소 추가 전에 내용을 출력해봅니다.
print(dictionary)
"""
print("name : ", dictionary["name"])
print("type : ", dictionary["type"])
print("ingredient : ", dictionary["ingredient"])
print("origin : ", dictionary["origin"])
print()
# C: 딕셔너리 추가
dictionary["head"] = "새로운"
#print("head : ", dictionary["head"])
dictionary["body"] = "몸"
#print("body : ", dictionary["body"])
# 선택 연사자[]로 딕셔너리 읽기
# dictionary의 head값을 출력하시오.
print("head : ", dictionary["head"])
print("head : ", dictionary.get("head"))
# 존재하지 않는 키: 선택 연산자로 없는 키에 접근하면 에러 발생.
try:
    dictionary["존재하지 않는 키"]
    # KeyError
except KeyError as ex:
    pass
    print(ex)  # 화면에 에러 출력하고 다음 라인 실행.
# 딕셔너리 수정
# name 값을 8D 망고로 수정
dictionary["name"] = "8D 망고"
print("name : ", dictionary["name"])
# 딕셔너리 삭제.
# 1. 연산자 방식 ==> del
# 2. 매서드 방식 ==> .pop("key") 추천
# name키를 삭제
# type키를 삭제
dictionary.pop("name")
print(dictionary)
del dictionary["type"]
print(dictionary)
# 딕셔너리 키 존재 여부 확인
# 방법1.  .get()메서드
# .get() 메서드 키가 존재하지 않는 경우에  None 사용
# 방법2. in 연산자를 사용
# value = dictionary("존재하지 않는 키")  # KeyError
value = dictionary.get("head")  # value = 값이 None이면 키가 없다는 의미
if value == None:
    print("키가 존재하지 않습니다.")
else:
    print("키가 존재합니다.")
# 방법2. in 연산자를 사용
if "존재하지 않는 키" in dictionary:
    print("키가 존재합니다.")
    print(dictionary["존재하지 않는 키"])
else:
    print("키가 존재하지 않습니다.")
print()
# S : 정렬, 딕셔너리는 정렬하는 방법이 없다.
# 단, key 값 정렬은 가능, value값만 정렬은 가능


# S : 검색, 특별한 방법은 없다. 선택 연산자 사용
# 선택연산자를 사용하면 바로 검색되기 때문
########################################
# 딕셔너리 열거
########################################
# key 만 열거, keys()  메서드 사용
for key in dictionary.keys():
    print("keys >>> ", key)
# value 만 열거, values() 메서드 사용
for value in dictionary.values():
    print("values >>> ", value)
# key, value를 쌍으로 열거, items() 메서드 사용
for item in dictionary.items():
    print("items >>> ", item)
"""