# 힌트. 문자열에서 0번째 문자를 추출하는 방법.
cnt = input("문자를 입력하세요. : ")
table = {"alp": 0, "dig": 0, "space": 0}
# 문자로 산술연산을 하는 경우 정수로 형변환되어 비교된다.
# isalpha() : 문자 체크
# isdigit() : 숫자 체크
# space() : 공백 체크
for i in cnt:
    # "0" == 48, "9" == 57
    if i.isalpha():
        table["alp"] = table["alp"]+1
    if i.isdigit():
        table["dig"] = table["dig"]+1
    if i.isspace():
        table["space"] = table["space"]+1
print(table)
# 문자로 산술연산을 하는 경우 정수로 형변환되어 비교된다.
