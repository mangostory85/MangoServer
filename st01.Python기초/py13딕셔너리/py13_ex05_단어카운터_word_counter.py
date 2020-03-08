# 1. 문자열을 split()해서 리스트로 만든다.
# 2. 반복문을 이용해서 array 리스트의 루프를 돌면서 딕셔너리 table에서 찾는다.
# table에서 찾을 때는 get()메서드나 in 연산자를 사용한다.
# 3. 찾았다면 바꾼다 replace()
# 4. 출력 print() join() 메서드를 사용하는 것으로 작성

str = input("번역할 문장을 입력하시오 : ")

table = {
    "B4": "Before",
    "TX": "Thanks",
    "BBL": "Be Back Later",
    "BCNU": "Be Seeing You",
    "HAND": "Have A Nice Day",
}

array = str.split(" ")
"""
for i in range(0, len(array), 1):
    print(array[i])
"""
result = " "
for i in array:
    value = table.get(i)
    if value == None:
        result = result+i +" "
    else:
        result = result+value +" "

print(result)
