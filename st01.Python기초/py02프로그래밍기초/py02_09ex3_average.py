value1 = input("첫번째 과목 점수를 입력하세요")  # 첫번째 과목 입력 str으로 저장
value2 = input("두번째 과목 점수를 입력하세요")  # 두번째 과목 입력 str으로 저장

value1 = int(value1)  # value1 값을 형변환 str -> int
value2 = int(value2)  # value2 값을 형변환 str -> int

sum = value1+value2
average = sum/2

print("--------------------")
if average >= 95:
    print("very good")
else:
    print("just good")
print("--------------------")